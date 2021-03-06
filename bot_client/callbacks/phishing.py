from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import re
from http import HTTPStatus

from utils.constants import CONSTANTS
from utils.constants import STATE
from utils.telegram_service import TelegramService
from utils.api_service import ApiService

def phishing_callback(update: Update, context: CallbackContext) -> int:

    msg = "*Phishing Check 🎣*\n\n"
    msg += "Please paste a link to check for the possibility of phishing 💸.\n Or else click on /back to return to main menu 📖.\n"

    if not context.user_data.get(CONSTANTS.START_OVER):
        TelegramService.remove_prev_keyboard(update)

    if not context.user_data.get(CONSTANTS.START_OVER):
        TelegramService.edit_reply_text(msg, update)
    else:
        TelegramService.reply_text(msg, update)
    context.user_data[CONSTANTS.START_OVER] = True

    return STATE.PHISHING_CHECK.value

def phishing_result_callback(update: Update, context: CallbackContext) -> int:

    raw_text = update.message.text

    regex = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?"
    isLink = re.search(regex, raw_text)

    if isLink:
        filtered_link = raw_text.strip('http://')
        filtered_link = filtered_link.strip('https://')
        try:
            ind = filtered_link.index("/")
            filtered_link = filtered_link[:ind]
        except:
            pass
        isPhish, status_code =  ApiService.validate_url(filtered_link)

        if status_code == HTTPStatus.OK:
            if isPhish:
                TelegramService.reply_text("The link is highly likely to be phishing 🐟", update)
            else:
                TelegramService.reply_text("The link is not likely to be phishing 🐟", update)
        else:
            TelegramService.reply_text("Error occurred while checking the link. ❌", update)

        return phishing_callback(update, context)
    else:
        TelegramService.edit_reply_text("Please paste a valid link 🎐", update)
        return phishing_callback(update, context)
