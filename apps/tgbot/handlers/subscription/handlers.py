from django.utils.translation import gettext as _
from telegram import Update
from telegram.ext import CallbackContext

from apps.tgbot.handlers.utils.decorators import get_user
from apps.tgbot.models import TelegramProfile
from apps.tgbot.services.subscription import check_if_user_subscribed


@get_user
async def check_user_subscription(update: Update, context: CallbackContext, user: TelegramProfile):
    status = await check_if_user_subscribed(context.bot, user)
    if status:
        await update.callback_query.answer()
        await context.bot.send_message(
            chat_id=user.telegram_id,
            text=str(_("You subscribed to all the required channels. You can use all the features of the bot.")),
        )
        return

    await update.callback_query.answer(
        text=str(
            _(
                "You did not subscribe to all the channels required to use the bot. "
                "Please subscribe to all the channels and try again."
            )
        ),
        show_alert=True,
    )
