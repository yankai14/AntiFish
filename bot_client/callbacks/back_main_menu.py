from telegram import Update
from telegram.ext import CallbackContext
from utils.constants import CONSTANTS

from utils.constants import STATE
from utils.telegram_service import TelegramService
from callbacks.start import start_callback


def back_main_menu_callback(update:Update, context: CallbackContext) -> None:

    TelegramService.remove_prev_keyboard(update)
    context.user_data[CONSTANTS.START_OVER] = True
    start_callback(update, context)

    return STATE.BACK.value


def back_main_menu_command_callback(update:Update, context: CallbackContext) -> None:

    context.user_data[CONSTANTS.START_OVER] = False
    start_callback(update, context)

    return STATE.BACK.value