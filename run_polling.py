import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from telegram import Bot
from telegram.ext import Updater, PicklePersistence


from django.conf import settings
from apps.tgbot.dispatcher import setup_dispatcher


def run_polling(tg_token: str = settings.BOT_TOKEN):
    """ Run bot in polling mode """
    updater = Updater(tg_token, use_context=True)

    if not os.path.exists(os.path.join(settings.BASE_DIR, "media")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media"))

    if not os.path.exists(os.path.join(settings.BASE_DIR, "media", "state_record")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media", "state_record"))

    persistence = PicklePersistence(
        filename=os.path.join(
            settings.BASE_DIR, "media", "state_record", "conversationbot"
            # settings.BASE_DIR, "media", "conversationbot"
        )
    )

    dp = updater.dispatcher
    dp.persistence = persistence
    dp = setup_dispatcher(dp)

    bot = Bot(tg_token)
    bot_info = bot.get_me()
    bot_link = f"https://t.me/{bot_info['username']}"

    print(f"Polling of '{bot_link}' has started")
    # it is really useful to send '👋' emoji to developer
    # when you run local test
    bot.send_message(text='👋', chat_id=1039835085)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    run_polling()
