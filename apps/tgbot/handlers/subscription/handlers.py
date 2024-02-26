from telegram import ParseMode, Update
from telegram.ext import CallbackContext
from django.utils.translation import gettext as _

from apps.tgbot.handlers.utils.decorators import get_user
from apps.tgbot.models import TelegramProfile
from apps.tgbot.services.subscription import check_if_user_subscribed


@get_user
def check_user_subscription(update: Update, context: CallbackContext, user: TelegramProfile):
    status = check_if_user_subscribed(context.bot, user)
    if status:
        update.message.reply_text(
            str(_("You are subscribed to the bot. You can use all the features of the bot."))
        )
        return

    update.callback_query.answer(
        text=str(_(
            "You are not subscribed to all the channels required to use the bot. "
            "Please subscribe to all the channels and try again."
        )),
        show_alert=True
    )

