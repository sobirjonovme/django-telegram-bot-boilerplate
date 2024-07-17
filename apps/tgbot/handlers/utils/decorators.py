from functools import wraps
from typing import Callable

from django.conf import settings
from django.utils.translation import activate
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import CallbackContext

from apps.tgbot.models import TelegramProfile
from apps.tgbot.services.subscription import (
    check_if_user_subscribed, send_subscription_required_message)


def admin_only(func: Callable):
    """
    Admin only decorator
    Used for handlers that only admins have access to

    This decorator requires `get_user` decorator to be used first
    """

    @wraps(func)
    async def wrapper(update: Update, context: CallbackContext, user, *args, **kwargs):
        # TODO: should add a check for admin, currently it doesn't work
        # if not user.is_admin:
        #     return

        return await func(update, context, user, *args, **kwargs)

    return wrapper


def send_typing_action(func: Callable):
    """Sends typing action while processing func command."""

    @wraps(func)
    async def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
        await update.effective_chat.send_chat_action(ChatAction.TYPING)
        return await func(update, context, *args, **kwargs)

    return wrapper


def get_user(func: Callable):
    @wraps(func)
    async def wrap(update, context, *args, **kwargs):
        effective_user = update.effective_user
        if not effective_user or effective_user.is_bot:
            # activate(settings.LANGUAGE_CODE)
            return None

        user, _ = await TelegramProfile.objects.aget_or_create(
            telegram_id=effective_user.id,
            defaults={
                "first_name": effective_user.first_name,
                "last_name": effective_user.last_name,
                "username": effective_user.username,
                "language": effective_user.language_code,
            },
        )

        if user.language not in dict(settings.LANGUAGES):
            activate(settings.LANGUAGE_CODE)
        else:
            activate(user.language)

        return await func(update, context, user, *args, **kwargs)

    return wrap


def subscription_required(func: Callable):
    """
    Decorator to check if user is subscribed

    This decorator requires `get_user` decorator to be used first
    """

    @wraps(func)
    async def wrap(update, context, user, *args, **kwargs):
        if not await check_if_user_subscribed(context.bot, user):
            await send_subscription_required_message(context.bot, user.telegram_id)
            return

        return await func(update, context, user, *args, **kwargs)

    return wrap
