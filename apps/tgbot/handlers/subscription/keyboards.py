from django.utils.translation import gettext as _
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from apps.tgbot.models import MandatorySubscription


async def get_subscription_buttons(bot):

    buttons = []

    mandatory_subscriptions = MandatorySubscription.objects.filter(is_active=True)
    if not await mandatory_subscriptions.aexists():
        return False, None

    async for mandatory_chat in mandatory_subscriptions:
        invite_link = mandatory_chat.invite_link
        if invite_link is None:
            invite_link = (await bot.create_chat_invite_link(chat_id=mandatory_chat.chat_id)).invite_link
            mandatory_chat.invite_link = invite_link
            await mandatory_chat.asave()

        buttons.append([InlineKeyboardButton(mandatory_chat.chat_title, url=invite_link)])

    buttons.append([InlineKeyboardButton(text=str(_("Check subscription")), callback_data="check_subscription")])

    return True, InlineKeyboardMarkup(buttons)
