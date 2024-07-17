"""
    Telegram event handlers
"""
import os

from django.conf import settings
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ConversationHandler, MessageHandler,
                          PicklePersistence, filters)

from apps.tgbot.handlers.registration.handlers import (command_start,
                                                       set_full_name,
                                                       set_phone_number)
from apps.tgbot.handlers.subscription.handlers import check_user_subscription
# from apps.tgbot.handlers.utils import files, error
from apps.tgbot.handlers.utils.states import state


def setup_application():
    """
    Adding handlers for events from Telegram
    """
    if not os.path.exists(os.path.join(settings.BASE_DIR, "media")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media"))

    if not os.path.exists(os.path.join(settings.BASE_DIR, "media", "state_record")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media", "state_record"))

    persistence = PicklePersistence(
        filepath=os.path.join(settings.BASE_DIR, "media", "state_record", "conversationbot")
    )

    app = Application.builder().token(settings.BOT_TOKEN).updater(None).persistence(persistence).build()

    states = {
        state.FULL_NAME: [MessageHandler(filters.TEXT, set_full_name)],
        state.PHONE_NUMBER: [MessageHandler(filters.TEXT, set_phone_number)],
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
        allow_reentry=True,
    )

    # registration
    app.add_handler(
        CallbackQueryHandler(
            check_user_subscription,
            pattern="check_subscription",
        )
    )
    app.add_handler(conversation_handler)

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

    return app


application = setup_application()
