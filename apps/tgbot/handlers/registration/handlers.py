from django.utils.translation import gettext as _
from telegram import Update
from telegram.ext import CallbackContext

from apps.tgbot.handlers.utils.decorators import (get_user,
                                                  subscription_required)
from apps.tgbot.handlers.utils.states import state
from apps.tgbot.models import TelegramProfile


@get_user
def command_start(update: Update, context: CallbackContext, user: TelegramProfile):

    update.message.reply_text(
        text=str(_("Assalomu alaykum\nIltimos, ismingizni kiriting")),
    )
    return state.FULL_NAME


@get_user
@subscription_required
def set_full_name(update: Update, context: CallbackContext, user: TelegramProfile):
    """
    Receives full name from user
    """

    context.user_data["full_name"] = update.message.text

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=str(_("Iltimos, telefon raqamingizni kiriting")),
        parse_mode="html",
        disable_web_page_preview=True,
    )
    return state.PHONE_NUMBER


@get_user
def set_phone_number(update: Update, context: CallbackContext, user: TelegramProfile):
    """
    Receives phone number from user
    """

    # user.full_name = context.user_data["full_name"]
    # user.phone_number = update.message.text
    # user.save()

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=str(_("Rahmat! Siz muvaffaqiyatli ro'yxatdan o'tdingiz")),
        parse_mode="html",
        disable_web_page_preview=True,
    )

    return state.END
