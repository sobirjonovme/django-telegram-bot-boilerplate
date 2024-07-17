import asyncio

from django.conf import settings
from django.core.management import BaseCommand
from telegram import Bot

from apps.tgbot.services.on_startup import set_up_commands, set_webhook


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = Bot(settings.BOT_TOKEN)

        # Use a custom event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        is_webhook_set, url = loop.run_until_complete(set_webhook(bot))
        loop.run_until_complete(set_up_commands(bot))

        loop.close()

        if is_webhook_set:
            self.stdout.write(self.style.SUCCESS(f"Webhook was successfully set to {url}"))
        else:
            self.stdout.write(self.style.WARNING(f"Webhook already set to {url}"))
