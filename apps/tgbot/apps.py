from django.apps import AppConfig


class TgbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tgbot'

    def ready(self):
        from apps.tgbot.services.on_startup import set_webhook, set_up_commands
        from apps.tgbot.main import bot
        set_webhook(bot)
        set_up_commands(bot)
