import json
import logging

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views import View
from telegram import Update

from apps.tgbot.bot_application import application
from core.celery import app

logger = logging.getLogger(__name__)


@app.task(ignore_result=True)
async def process_telegram_event(update_json):

    async with application:
        update = Update.de_json(update_json, application.bot)
        await application.process_update(update)


# WARNING: if fail - Telegram webhook will be delivered again.
# Can be fixed with async celery task execution
class TelegramBotWebhookView(View):
    async def post(self, request, *args, **kwargs):
        bot_secret_key = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
        if bot_secret_key != settings.BOT_SECRET_KEY:
            return HttpResponse(status=400)

        if settings.RUN_BOT_CELERY:
            # Process Telegram event in Celery worker (async)
            # Don't forget to run it and & Redis (message broker for Celery)!
            # Locally, You can run all of these services via docker-compose.yml
            process_telegram_event.delay(json.loads(request.body))
        else:
            await process_telegram_event(json.loads(request.body))

        return JsonResponse({"ok": "POST request processed"})

    async def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})
