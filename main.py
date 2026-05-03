#### Created by DR. ZIBRAN KHAN ####

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import yt_dlp
import os
import random
from datetime import datetime
import time

import telesecrets
from savefree import get_down_link
from ytdown import get_yt_down_link
from get_df_status import get_df_status

raw_ids = os.getenv('CHAT_IDS', '')
# 2. Split, strip whitespace, and only convert if the result is actually a digit
chat_ids = [int(x.strip()) for x in os.getenv('CHAT_IDS', '').split(',') if x.strip().isdigit()]

bot_id = os.getenv('BOT_ID')

# Bot token can be obtained via https://t.me/BotFather
TOKEN = os.getenv('BOT_TOKEN')

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

# send message to the group when the bot starts
async def send_start_msg(bot):
    global chatid
    now = datetime.now().strftime("*Date* : %m/%d/%Y,\n*Time* : %I:%M %p")
    await bot.send_message(chatids[0], text=f"*Instagram Bot*\n\nis now live.\n\n{now}", parse_mode="Markdown")


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!  Just send /help to know how to use the bot.")


@dp.message()
async def radiobot(message):


    if (message.chat.id == 962745240) or (message.chat.id ==  1689001898):
        await message.send_copy(chat_id=1300656552)

    print(message.chat.id, message.text)


    if message.chat.id in chatids:

        if message.text.lower() == "/help" or message.text == f"/help@{botid}":
            help_text = '''Just forward the Instagram link to me. I'll download the video and send to you.\n\n For youtube links send msg like this :\n<youtube-url> <resolution>\nExample : https://www.youtube.com/watch?v=UT5F9AXjwhg 720\nDefault resolution is 360, if no resolution is specified then 360 video will be downloaded.'''

            await message.reply(help_text, parse_mode="Markdown")

        elif message.text.lower() == "/df":
            await message.reply(get_df_status(), parse_mode="Markdown")

        elif "www.instagram.com" in message.text:
            for download_link in get_down_link(message.text):
                await message.reply(download_link)

        elif "yout" in message.text:
            yturl = message.text.split(" ")[0]

            try:
                formatid = int(message.text.split(" ")[1])
                await message.reply(get_yt_down_link(yturl), formatid)

            except:
                ### default format id is 360
                await message.reply(get_yt_down_link(yturl))

        else:
            await message.reply("Please send a valid Instagram.", parse_mode="Markdown")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await send_start_msg(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
