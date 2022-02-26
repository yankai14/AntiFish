from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from utils.constants import STATE, CONSTANTS
from utils.telegram_service import TelegramService

def start_callback(update: Update, context: CallbackContext) -> int:

    msg = "*Welcome To AntiFish*\n\n"
    msg += "Listed below are the following features you can take advantage of\n"
    msg += "-----------------------------------------\n"
    msg += "Below are the default commands:\n"
    msg += "/stop - To stop the bot✋\n"
    msg += "-----------------------------------------\n"
    msg += "Please contact @yankai14 for any queries\n"

    keyboard = [
        [
            InlineKeyboardButton(text="Phishing Check", callback_data=str(STATE.PHISHING_CHECK.value)),
            InlineKeyboardButton(text="Report Suspicious Links", callback_data=str(STATE.REPORT.value)),
            InlineKeyboardButton(text="Help", callback_data=str(STATE.ABOUT.value)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if context.user_data.get(CONSTANTS.START_OVER):
        TelegramService.edit_reply_text(msg, update, reply_markup)
    else:
        TelegramService.reply_text(msg, update, reply_markup)

    context.user_data[CONSTANTS.START_OVER] = False

    return STATE.FEATURE_SELECTION.value
