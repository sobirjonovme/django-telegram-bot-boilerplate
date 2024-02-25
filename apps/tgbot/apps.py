from django.apps import AppConfig


class TgbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tgbot'

    def ready(self):
        from apps.tgbot.services.on_startup import set_webhook, set_up_commands
        from apps.tgbot.main import bot

        set_up_commands(bot)
        is_webhook_set, url = set_webhook(bot)

        if is_webhook_set:
            print(f"Webhook set to {url}")
        else:
            print(f"Webhook is already set to {url}")
