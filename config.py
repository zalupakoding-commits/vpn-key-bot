# Configuration settings for the VPN Key Bot

DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

LOGGING = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'filename': 'vpn_key_bot.log'
}

BOT_TOKENS = {
    'telegram': 'your_telegram_bot_token',
    'discord': 'your_discord_bot_token'
}

API_KEYS = {
    'service_one': 'your_api_key_for_service_one',
    'service_two': 'your_api_key_for_service_two'
}