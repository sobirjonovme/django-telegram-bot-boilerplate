"""
    Telegram event handlers
"""
import os
from queue import Queue
from telegram.ext import (
    Dispatcher, Filters,
    CommandHandler, MessageHandler,
    CallbackQueryHandler, ConversationHandler, PicklePersistence,
)

from django.conf import settings
from apps.tgbot.handlers.registration.manage_data import SECRET_LEVEL_BUTTON

from apps.tgbot.handlers.utils import files, error
from apps.tgbot.handlers.utils.states import state
from apps.tgbot.handlers.registration.handlers import (
    command_start, set_full_name, set_phone_number
)
from apps.tgbot.handlers.subscription.handlers import check_user_subscription
from apps.tgbot.main import bot


def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """

    states = {
        state.FULL_NAME: [MessageHandler(Filters.text, set_full_name)],
        state.PHONE_NUMBER: [MessageHandler(Filters.text, set_phone_number)],
    }

    entry_points = [
        CommandHandler("start", command_start),
    ]

    fallbacks = [
        CommandHandler("start", command_start),
    ]

    conversation_handler = ConversationHandler(
        entry_points=entry_points,
        states=states,
        fallbacks=fallbacks,
        name="conversation_handler",
        persistent=True,
    )

    # registration
    dp.add_handler(
        CallbackQueryHandler(
            check_user_subscription,
            pattern="check_subscription",
        )
    )
    dp.add_handler(conversation_handler)

    # # files
    # dp.add_handler(MessageHandler(
    #     Filters.animation, files.show_file_id,
    # ))

    # # handling errors
    # dp.add_error_handler(error.send_stacktrace_to_tg_chat)

    # EXAMPLES FOR HANDLERS
    # dp.add_handler(MessageHandler(Filters.text, <function_handler>))
    # dp.add_handler(MessageHandler(
    #     Filters.document, <function_handler>,
    # ))
    # dp.add_handler(CallbackQueryHandler(<function_handler>, pattern="^r\d+_\d+"))
    # dp.add_handler(MessageHandler(
    #     Filters.chat(chat_id=int(TELEGRAM_FILESTORAGE_ID)),
    #     # & Filters.forwarded & (Filters.photo | Filters.video | Filters.animation),
    #     <function_handler>,
    # ))

    return dp


if not os.path.exists(os.path.join(settings.BASE_DIR, "media")):
    os.makedirs(os.path.join(settings.BASE_DIR, "media"))

if not os.path.exists(os.path.join(settings.BASE_DIR, "media", "state_record")):
    os.makedirs(os.path.join(settings.BASE_DIR, "media", "state_record"))

persistence = PicklePersistence(
    filename=os.path.join(
        settings.BASE_DIR, "media", "state_record", "conversationbot"
        # settings.BASE_DIR, "media", "conversationbot"
    )
)
queue = Queue()

n_workers = 1 if settings.DEBUG else 4
dispatcher = setup_dispatcher(
    Dispatcher(
        bot,
        update_queue=queue,
        workers=n_workers,
        use_context=True,
        persistence=persistence
    )
)
