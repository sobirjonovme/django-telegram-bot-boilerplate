from django.utils.translation import gettext as _
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from apps.tgbot.handlers.utils.decorators import (get_user, send_typing_action,
                                                  subscription_required)
from apps.tgbot.handlers.utils.states import state
from apps.tgbot.models import TelegramProfile


@get_user
@send_typing_action
@subscription_required
async def command_start(update: Update, context: ContextTypes.DEFAULT_TYPE, user: TelegramProfile):

    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text=str(_("Assalomu alaykum\nIltimos, ismingizni kiriting")),
        parse_mode=ParseMode.HTML,
    )

    return state.FULL_NAME


@get_user
@subscription_required
async def set_full_name(update: Update, context: ContextTypes.DEFAULT_TYPE, user: TelegramProfile):
    """
    Receives full name from user
    """
    context.user_data["full_name"] = update.message.text

    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text=str(_("Iltimos, telefon raqamingizni kiriting")),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
    return state.PHONE_NUMBER


@get_user
async def set_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE, user: TelegramProfile):
    """
    Receives phone number from user
    """
    context.user_data["phone_number"] = update.message.text

    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text=str(_("Rahmat! Siz muvaffaqiyatli ro'yxatdan o'tdingiz")),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )

    return state.END
