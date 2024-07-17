from typing import Dict, Tuple

from django.conf import settings
from django.urls import reverse
from telegram import Bot, BotCommand, Update

from apps.tgbot.main import bot


async def set_webhook(bot_instance: Bot = bot) -> Tuple[bool, str]:
    webhook_url = settings.HOST + reverse("tgbot:webhook", args=[settings.BOT_TOKEN])

    webhook_info = await bot_instance.get_webhook_info()
    if webhook_info.url != webhook_url:
        await bot_instance.set_webhook(
            url=webhook_url,
            secret_token=settings.BOT_SECRET_KEY,
            allowed_updates=Update.ALL_TYPES,
        )
        return True, webhook_url

    return False, webhook_url


async def delete_webhook(bot_instance: Bot = bot) -> None:
    await bot_instance.delete_webhook()


async def set_up_commands(bot_instance: Bot = bot) -> None:

    langs_with_commands: Dict[str, Dict[str, str]] = {
        "en": {
            "start": "Start bot 🚀",
        },
        "uz": {
            "start": "Botni boshlash 🚀",
        },
    }

    await bot_instance.delete_my_commands()
    for language_code in langs_with_commands:
        await bot_instance.set_my_commands(
            language_code=language_code,
            commands=[
                BotCommand(command, description) for command, description in langs_with_commands[language_code].items()
            ],
        )
