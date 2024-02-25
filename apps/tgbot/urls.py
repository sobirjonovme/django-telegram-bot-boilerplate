from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import TelegramBotWebhookView

app_name = "tgbot"

urlpatterns = [
    path("webhook/<str:token>/", csrf_exempt(TelegramBotWebhookView.as_view()), name="webhook"),
]

