# CEX_volume_checker_K
Pulling data from Kucoin CEX and notifying the user of any sudden changes in volume.

Install the required dependencies and libraries

You will need API credentials from Kucoin  for accessing the Kucoin API. 
Additionally, you will need a Telegram bot token and chat ID for sending alerts via Telegram. 
Create a credentials_k.json file in the project directory and add your Kucoin API key and secret.

Update the bot_token and chat_id variables in the script with your Telegram bot token and chat ID.

Run the script!

The script will start monitoring trading pairs on Kucoin. It will retrieve historical volume data, calculate the mean volume over the past 24 hours, and send Telegram alerts if the current volume exceeds certain thresholds.

The alerts will include information about the trading pair, current volume, and mean volume over the past 24 hours.
