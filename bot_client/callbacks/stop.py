from telegram import Update
from telegram.ext import CallbackContext
from utils.constants import STATE, CONSTANTS

def stop_callback(update: Update, context: CallbackContext) -> None:
    """End Conversation by command."""
    if context.user_data.get(CONSTANTS.START_OVER):
        del context.user_data[CONSTANTS.START_OVER]
    update.message.reply_text('Okay, bye.')
    return STATE.END.value