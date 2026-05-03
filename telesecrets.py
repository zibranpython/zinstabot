import os
bot_token = os.getenv('BOT_TOKEN')
chat_ids = [int(x) for x in os.getenv('CHAT_IDS', '').split(',')]
bot_id = os.getenv('BOT_ID')
