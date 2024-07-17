import asyncio
import sys

import telegram
from django.conf import settings
from telegram import Bot

bot = Bot(settings.BOT_TOKEN)


def is_async_process():
    try:
        asyncio.get_running_loop()
        return True
    except RuntimeError:
        return False


async def check_bot_token():
    try:
        bot_info = await bot.get_me()
        sys.stdout.write(f"\033[92mBot token is valid: {bot_info.username}\033[0m\n")
    except telegram.error.InvalidToken:
        sys.stderr.write("\033[91mERROR:Invalid bot token\033[0m\n")
        sys.exit(1)


if is_async_process():
    # loop = asyncio.get_running_loop()
    # loop.run_until_complete(check_bot_token())
    pass
else:
    asyncio.run(check_bot_token())
