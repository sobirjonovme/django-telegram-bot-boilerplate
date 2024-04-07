from telegram import Bot
from django.conf import settings
from django.core.management import BaseCommand

from apps.tgbot.services.on_startup import set_webhook, set_up_commands


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = Bot(settings.BOT_TOKEN)
        is_webhook_set, url = set_webhook(bot)
        set_up_commands(bot)

        if is_webhook_set:
            self.stdout.write(self.style.SUCCESS(f"Webhook was successfully set to {url}"))
        else:
            self.stdout.write(self.style.WARNING(f"Webhook already set to {url}"))
