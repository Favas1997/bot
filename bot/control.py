from . import actions
from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


print("Bot working")
API_KEY='1945777770:AAEPi9txTtGtfOuG2JXksmFsM1X_ZXhZAMw'

def start_command(update, context):
    buttons = [
        [InlineKeyboardButton("Stupid", callback_data='stupid')],
        [InlineKeyboardButton("fat", callback_data='fat')],
        [InlineKeyboardButton("dumb", callback_data='dumb')],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    message_reply = 'Click a button'
    update.message.reply_text(message_reply, reply_markup=reply_markup)


def press_button_callback(update, context):
    text = str(update.callback_query.data).lower()
    username = str(update.callback_query.message.chat.first_name).lower()
    response_data = actions.bot_responses(text, username)
    response = response_data[0]

    update.callback_query.message.reply_text(text=response)


def help_command(update, context):
    update.message.reply_text("If you need help ask it in stockOverflow")


def handle_message(update, context):
    text = str(update.message.text).lower()
    print(text)
    username = str(update.message.chat.first_name).lower()
    print(username)
    response_data = actions.bot_responses(text, username)
    response = response_data[0]
    print(response)

    update.message.reply_text(response)


def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    dispatch = updater.dispatcher

    dispatch.add_handler(CommandHandler("start", start_command))
    dispatch.add_handler(CallbackQueryHandler(press_button_callback))
    dispatch.add_handler(CommandHandler("help", help_command))

    dispatch.add_handler(MessageHandler(Filters.text, handle_message))

    dispatch.add_error_handler(error)

    updater.start_polling()

    updater.idle()


main()