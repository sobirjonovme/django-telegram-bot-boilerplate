from typing import Dict, Tuple
from telegram import Bot, BotCommand
from django.urls import reverse
from django.conf import settings

from apps.tgbot.main import bot


def set_webhook(bot_instance: Bot = bot) -> Tuple[bool, str]:
    webhook_url = settings.HOST + reverse('tgbot:webhook', args=[settings.BOT_TOKEN])

    webhook_info = bot_instance.get_webhook_info()
    if webhook_info.url != webhook_url:
        bot_instance.set_webhook(
            url=webhook_url,
            secret_token=settings.BOT_SECRET_KEY
        )
        return True, webhook_url

    return False, webhook_url


def delete_webhook(bot_instance: Bot = bot) -> None:
    bot_instance.delete_webhook()


def set_up_commands(bot_instance: Bot = bot) -> None:

    langs_with_commands: Dict[str, Dict[str, str]] = {
        'en': {
            'start': 'Start bot 🚀',
        },
        'uz': {
            'start': 'Botni boshlash 🚀',
        }
    }

    bot_instance.delete_my_commands()
    for language_code in langs_with_commands:
        bot_instance.set_my_commands(
            language_code=language_code,
            commands=[
                BotCommand(command, description) for command, description in langs_with_commands[language_code].items()
            ]
        )
