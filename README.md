# CEX_volume_checker_K

Pulling data from Kucoin CEX.

Install the required dependencies and libraries

You will need API credentials from Kucoin  for accessing the Kucoin API. 

Additionally, you will need a Telegram bot token and chat ID for sending alerts via Telegram. 

Create a credentials_k.json file in the project directory and add your Kucoin API key and secret.

Can be used with `telegram_alerts` and `formatting_btk`.

Run the script!

The script will start monitoring trading pairs on Kucoin. It will retrieve historical volume data and calculate the mean volume over the past 24 hours.
