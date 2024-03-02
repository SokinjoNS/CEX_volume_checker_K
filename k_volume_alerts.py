import requests
import os
import time
import json
import pandas as pd
from kucoin.client import Client
import datetime
import schedule
from alert_levels_tg import get_volume_alert_details
from telegram_alerts import send_telegram_message
from formatting_btk import format_number, generate_chart_url

now = datetime.datetime.now()
# Calculate the remaining time to the next full hour
remaining_minutes = 60 - now.minute - 1
remaining_seconds = 60 - now.second
remaining_time = remaining_minutes * 60 + remaining_seconds

# Load credentials and initialize client
with open('credentials_k.json') as f:
    credentials = json.load(f)
api_key = credentials['Kucoin_api_key']
api_secret = credentials['Kucoin_secret_key']
api_passphrase = credentials['Kucoin_passphrase']
client = Client(api_key, api_secret, api_passphrase)

def generate_kucoin_chart_url(symbol, interval="1h"):
    base_url = "https://www.tradingview.com/chart/"
    chart_params = f"symbol=KUCOIN:{symbol.replace('-USDT', 'USDT')}&interval={interval}"
    return f"{base_url}?{chart_params}"

def run_script():
    symbols = client.get_symbols()
    usdt_pairs = [s['symbol'] for s in symbols if s['quoteCurrency'] == 'USDT' and 'UP-USDT' not in s['symbol']
                  and 'DOWN-USDT' not in s['symbol'] and 'BEAR-USDT' not in s['symbol'] and 'BULL-USDT' not in s['symbol']
                  and '3S-USDT' not in s['symbol'] and '2S-USDT' not in s['symbol']
                  and '3L-USDT' not in s['symbol'] and '2L-USDT' not in s['symbol']]

    for symbol in usdt_pairs:
        interval = '1hour' # Retrieve data for previous 25 hours with 1 hour interval
        url = f'https://api.kucoin.com/api/v1/market/candles?type={interval}&symbol={symbol}&limit=26'

        try:
            response = requests.get(url)
            response.raise_for_status()  # raise an exception if status code is not 200

            #data = response.json()
            data = response.json()["data"]

            df = pd.DataFrame(data, columns=["timestamp", "open", "close", "high", "low", "volume", "turnover"])

            # convert timestamp to datetime
            df["timestamp"] = pd.to_datetime(df["timestamp"].astype(int), unit="s")
            df = df.sort_values(by='timestamp', ascending=True)

            # convert volume to numeric
            df["volume"] = pd.to_numeric(df["volume"])

            # calculate volume change
            if len(df) > 2:
                curr_volume = df['volume'].iloc[-2]
                past_24_hours = df.iloc[:-2]['volume'].astype(float)
                prev_volume_mean = past_24_hours.mean()

                alert_details_list = get_volume_alert_details(curr_volume, prev_volume_mean, symbol, '1h', 'KUCOIN')

                
            for alert_detail in alert_details_list:
                alert_message = {
                    'exchange': 'KUCOIN',
                    'symbol': alert_detail['symbol'],
                    'curr_volume': alert_detail['curr_volume'],
                    'prev_volume_mean': alert_detail['prev_volume_mean'],
                    'level': alert_detail['level'],
                    'chart_url': alert_detail['chart_url']
                }
                send_telegram_message(alert_message)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {symbol}: {e}")
        except ValueError as e:
            print(f"Error processing data for {symbol}: {e}")

# Schedule and run the script
for hour in range(24):
    schedule.every().day.at("{:02d}:06".format(hour)).do(run_script)

# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
