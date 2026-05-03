import os
bot_token = os.getenv('BOT_TOKEN')

raw_ids = os.getenv('CHAT_IDS', '')
# 2. Split, strip whitespace, and only convert if the result is actually a digit
chat_ids = [int(x.strip()) for x in os.getenv('CHAT_IDS', '').split(',') if x.strip().isdigit()]

bot_id = os.getenv('BOT_ID')
