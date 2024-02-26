from django.contrib import admin

from .models import TelegramProfile, MandatorySubscription


# Register your models here.
@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "username", "telegram_id", "phone", "language")
    list_display_links = ("id", "first_name", "last_name", "username", "telegram_id")
    search_fields = ("first_name", "last_name", "username", "phone")
    list_filter = ("language",)


@admin.register(MandatorySubscription)
class MandatorySubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "chat_title", "chat_id", "is_active")
    list_display_links = ("id", "chat_title", "chat_id")
    search_fields = ("chat_title", "chat_id")
    list_filter = ("is_active",)
