import os

import django
from telegram import Update
from telegram.ext import Application, PicklePersistence

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.conf import settings

from apps.tgbot.bot_application import setup_application


def run_polling():
    """Run bot in polling mode"""

    if not os.path.exists(os.path.join(settings.BASE_DIR, "media")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media"))

    if not os.path.exists(os.path.join(settings.BASE_DIR, "media", "state_record")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media", "state_record"))

    persistence = PicklePersistence(
        filepath=os.path.join(settings.BASE_DIR, "media", "state_record", "conversationbot")
    )

    application = Application.builder().token(settings.BOT_TOKEN).persistence(persistence).build()

    setup_application(application)

    # write successful start message in Green to the console
    print("\033[92m👋 Bot started successfully....\033[0m")

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    run_polling()
