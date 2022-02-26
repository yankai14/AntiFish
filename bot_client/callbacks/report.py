from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import re
from http import HTTPStatus

from utils.constants import CONSTANTS
from utils.constants import STATE
from utils.telegram_service import TelegramService
from utils.api_service import ApiService

def report_callback(update: Update, context: CallbackContext) -> int:

    msg = "*Report Suspicious Links 👮*\n\n"
    msg += "Please paste a link to report a link. We will investigate on our end. Otherwise, click on the back button to return to main menu\n"

    if not context.user_data.get(CONSTANTS.START_OVER):
        TelegramService.remove_prev_keyboard(update)

    keyboard = [
        [
            InlineKeyboardButton(text="Back", callback_data=STATE.BACK.value),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    if not context.user_data.get(CONSTANTS.START_OVER):
        TelegramService.edit_reply_text(msg, update, reply_markup)
    else:
        TelegramService.reply_text(msg, update, reply_markup)
    context.user_data[CONSTANTS.START_OVER] = True

    return STATE.REPORT.value



def report_result_callback(update: Update, context: CallbackContext) -> int:
    raw_text = update.message.text

    regex = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?"
    isLink = re.search(regex, raw_text)

    if isLink:
        # TODO Check if the link is phishing
        status_code =  ApiService.report_url(raw_text)

        if status_code == HTTPStatus.OK:
            TelegramService.reply_text("The link has successfully been reported", update)
        else:
            TelegramService.reply_text("Error occurred while reporting the link", update)

        return report_callback(update, context)
    else:
        TelegramService.reply_text("Please paste a valid link", update)
        return report_callback(update, context)