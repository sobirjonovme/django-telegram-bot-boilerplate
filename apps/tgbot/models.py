from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


# Create your models here.
class TelegramProfile(BaseModel):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, null=True, blank=True)
    username = models.CharField(_("username"), max_length=150, null=True, blank=True)
    telegram_id = models.CharField(max_length=255, null=True, blank=True, unique=True)

    phone = models.CharField(_("phone"), max_length=20, null=True, blank=True)
    language = models.CharField(max_length=15, choices=settings.LANGUAGES, default='uz')

    class Meta:
        verbose_name = _("Telegram Profile")
        verbose_name_plural = _("Telegram Profiles")

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''}"


class MandatorySubscription(BaseModel):
    chat_title = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255, unique=True)
    invite_link = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Mandatory Subscription")
        verbose_name_plural = _("Mandatory Subscriptions")

    def __str__(self):
        return self.chat_title

