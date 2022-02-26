from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.conversationhandler import ConversationHandler
from telegram.ext.callbackqueryhandler import CallbackQueryHandler

from config import ENV
from utils.constants import STATE
from callbacks.start import start_callback
from callbacks.stop import stop_callback
from callbacks.back_main_menu import back_main_menu_callback, back_main_menu_command_callback
from callbacks.phishing import phishing_callback, phishing_result_callback
from callbacks.report import report_callback, report_result_callback
from callbacks.about import about_callback


def start():
    updater = Updater(token = ENV.TELEGRAM_BOT_TOKEN, use_context = True)
    dispatcher = updater.dispatcher

    phishing_conv = ConversationHandler(
        entry_points= [CallbackQueryHandler(phishing_callback, pattern=f"^{str(STATE.PHISHING_CHECK.value)}$")],
        states = {
            STATE.PHISHING_CHECK.value: [
                MessageHandler(Filters.text & ~ Filters.command, phishing_result_callback)
            ]
        },
        fallbacks = [
            CommandHandler('stop', stop_callback),
            # CallbackQueryHandler(
            #     back_main_menu_callback,
            #     pattern=f"^{STATE.BACK.value}$"
            # ), 
            CommandHandler("back", back_main_menu_command_callback)
        ],
        map_to_parent={
            STATE.BACK.value: STATE.FEATURE_SELECTION.value,
            STATE.END.value: STATE.END.value
        }
    )

    report_conv = ConversationHandler(
        entry_points= [CallbackQueryHandler(report_callback, pattern=f"^{str(STATE.REPORT.value)}$")],
        states = {
            STATE.REPORT.value: [
                MessageHandler(Filters.text & ~ Filters.command, report_result_callback)

            ]
        },
        fallbacks = [
            CommandHandler('stop', stop_callback),
            # CallbackQueryHandler(
            #     back_main_menu_callback,
            #     pattern=f"^{STATE.BACK.value}$"
            # ), 
            CommandHandler("back", back_main_menu_command_callback)
        ],
        map_to_parent={
            STATE.BACK.value: STATE.FEATURE_SELECTION.value,
            STATE.END.value: STATE.END.value
        }
    )

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start_callback)],
        states = {
            STATE.SHOWING.value: [
                CallbackQueryHandler(start_callback, pattern=f"^{str(STATE.BACK.value)}$")
            ],
            STATE.FEATURE_SELECTION.value: [
                phishing_conv,
                report_conv,
                CallbackQueryHandler(about_callback, pattern=f"^{str(STATE.ABOUT.value)}$")
            ],
        },
        fallbacks=[
            CommandHandler("stop", stop_callback),
            CallbackQueryHandler(
                start_callback,
                pattern=f"^{STATE.BACK.value}$"
            ),
        ]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    start()