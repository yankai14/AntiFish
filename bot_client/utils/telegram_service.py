from telegram import Update, InlineKeyboardMarkup
from telegram.ext import CallbackContext


class TelegramService:

    @staticmethod
    def get_query(update: Update):
        query = update if update.message else update.callback_query
        return query

    @staticmethod
    def replace_invalid_char(msg: str):
        msg = msg.replace('_', ' ')
        msg = msg.replace('.', '\.')
        msg = msg.replace('-', '\-')
        return msg

    @staticmethod
    def replace_invalid_char_stripe_url(msg: str):
        msg = msg.replace('_', '\_')
        msg = msg.replace('.', '\.')
        msg = msg.replace('-', '\-')
        msg = msg.replace('#', '\#')
        msg = msg.replace('!', '\!')
        msg = msg.replace('=', '\=')
        return msg

    @staticmethod
    def reply_text(msg: str, update: Update, keyboard: InlineKeyboardMarkup=None):
        msg = TelegramService.replace_invalid_char(msg)
        query = TelegramService.get_query(update)
        query.message.reply_text(msg, parse_mode='MarkdownV2', reply_markup=keyboard)


    @staticmethod
    def edit_reply_text(msg: str, update: Update, keyboard: InlineKeyboardMarkup=None):
        msg = TelegramService.replace_invalid_char(msg)
        query = TelegramService.get_query(update)
        query.message.edit_text(msg, parse_mode='MarkdownV2', reply_markup=keyboard)

    @staticmethod
    def remove_prev_keyboard(update: Update):
        query = TelegramService.get_query(update)
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup([]))

    @staticmethod
    def get_user_id(update: Update):
        id = update.message.from_user['id'] if update.message else update.callback_query.from_user['id']
        return id

    @staticmethod
    def get_callback_query_data(update: Update):
        query = TelegramService.get_query(update)
        return query.data