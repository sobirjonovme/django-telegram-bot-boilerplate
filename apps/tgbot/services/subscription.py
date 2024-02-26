from django.utils.translation import gettext as _

from apps.tgbot.handlers.subscription.keyboards import get_subscription_buttons
from apps.tgbot.models import MandatorySubscription, TelegramProfile


def check_if_user_subscribed(bot, user: TelegramProfile) -> bool:
    """
    Checks if user is subscribed to mandatory channels
    """

    for chat in MandatorySubscription.objects.filter(is_active=True):
        chat_member = bot.get_chat_member(chat.chat_id, user.telegram_id)
        if chat_member.status not in ["member", "administrator", "creator"]:
            return False

    return True


def send_subscription_required_message(bot, chat_id):
    """
    Sends message to user that subscription is required to use the bot
    """
    exists, buttons = get_subscription_buttons(bot)
    if exists:
        text = str(_("Iltimos, botdan foydalanish uchun quyidagi kanallarga obuna bo'ling"))
        bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=buttons,
        )

    return False
