# KuCoin Volume Alert

## Overview

This script is designed to monitor trading volume changes on the KuCoin exchange for USDT trading pairs. It alerts users via Telegram when significant volume changes occur, compared to the 24-hour average. It integrates with the KuCoin API to fetch trading data, analyzes volume changes, and utilizes Telegram for notifications. Additionally, it provides a link to a trading view chart for the relevant cryptocurrency pair.

## Features

- Monitors all USDT pairs on KuCoin that don't include leveraged tokens.
- Calculates the average trading volume over the past 24 hours.
- Detects significant volume changes and generates alerts.
- Sends a detailed alert message through Telegram, including the exchange, symbol, current volume, previous average volume, alert level, and a chart URL.
- Schedules the script to run at the beginning of every hour to ensure up-to-date monitoring.

## Prerequisites

Before running this script, ensure you have the following:
- Python 3.x installed on your system.
- `requests`, `pandas`, `schedule`, and `kucoin-python` packages installed.
- A KuCoin account with an API key, secret key, and passphrase.
- A Telegram bot for sending alerts and the corresponding bot token.

## Installation

1. Clone the repository or download the script to your local machine.
2. Install the required Python packages using pip:

```bash
pip install requests pandas schedule kucoin-python
```

Create a credentials_k.json file in the script's directory with your KuCoin API credentials in the following format:
```
{
  "Kucoin_api_key": "your_api_key",
  "Kucoin_secret_key": "your_secret_key",
  "Kucoin_passphrase": "your_passphrase"
}
```

Ensure you have set up a Telegram bot and have its token. Modify the telegram_alerts.py script to include your bot token and the chat ID where alerts should be sent.

## Customization

You can customize the alert criteria by modifying the get_volume_alert_details function in the alert_levels_tg.py file. This allows you to set different thresholds for volume changes that trigger alerts.

## Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Support

For issues, questions, or contributions, please open an issue in the GitHub repository.

Feedback and contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
This project and the direct_address_tg_listener.py module are licensed under the MIT License. For more details, see the LICENSE file.
