import logging
import sys

import telegram
from telegram import Bot

from core.settings import BOT_TOKEN

# Global variable - the best way I found to init Telegram bot
try:
    bot = Bot(BOT_TOKEN)
    TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
except telegram.error.Unauthorized:
    logging.error("Invalid TELEGRAM_TOKEN.")
    sys.exit(1)
