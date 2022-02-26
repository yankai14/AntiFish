from pickle import TRUE
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from utils.constants import CONSTANTS
from utils.constants import STATE
from utils.telegram_service import TelegramService


def about_callback(update: Update, context: CallbackContext) -> int:

    msg = "*AntiFish*\n\n"
    msg += "Empowering Users Of The Web\n"
    msg += "-----------------------------------------\n"
    msg += "We are a team of developers 🧑🏽‍🤝‍🧑🏽 who aim to spread awareness of Phishing.\n"
    msg += "Our AntiFish extension checks for telltale signs of phishing links and cautions users about possible harmful links.\n"
    msg += "Phishing is an attack often used to steal user data. It baits users into clicking a malicious link that pretends to be a trusted entity. A successful attack could result in stolen personal information, unauthorized purchases, and other devastating outcomes.\n"
    msg += "-----------------------------------------\n"
    msg += "Please contact @yankai14 for any queries.\n"

    keyboard = [
        [
            InlineKeyboardButton(text="Back", callback_data=str(STATE.BACK.value)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    TelegramService.edit_reply_text(msg, update, reply_markup)

    context.user_data[CONSTANTS.START_OVER] = TRUE

    return STATE.FEATURE_SELECTION.value