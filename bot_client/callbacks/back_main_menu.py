from telegram import Update, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from utils.constants import STATE
from utils.telegram_service import TelegramService
from callbacks.start import start_callback


def back_main_menu_callback(update:Update, context: CallbackContext) -> None:

    TelegramService.remove_prev_keyboard(update)
    context.user_data[STATE.START_OVER.value] = True
    start_callback(update, context)

    return STATE.BACK.value