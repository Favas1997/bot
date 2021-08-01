from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from . import actions
from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

API_KEY='1945777770:AAEPi9txTtGtfOuG2JXksmFsM1X_ZXhZAMw'

def chat(request):
    print("xjzkjxcjxclkjxcjk")
    user_data = chats.objects.all()
    context = {'data': user_data}
    return render(request, 'bot/table.html', context)


"""start function to start the conversation with bot"""


def start_command(update, context):
    buttons = [
        [InlineKeyboardButton("Stupid", callback_data='stupid')],
        [InlineKeyboardButton("fat", callback_data='fat')],
        [InlineKeyboardButton("dumb", callback_data='dumb')],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    message_reply = 'Click a button'
    update.message.reply_text(message_reply, reply_markup=reply_markup)


""" This function defines what happens when a user clicks a button"""


def press_button_callback(update, context):
    text = str(update.callback_query.data).lower()
    username = str(update.callback_query.message.chat.first_name).lower()
    response_data = actions.bot_responses(text, username)
    response = response_data[0]

    update.callback_query.message.reply_text(text=response)


""" This function is executed when help command is selected"""


def help_command(update, context):
    update.message.reply_text("If you need help ask it in stockOverflow")


""" This function defines what happens when a user types a text instead of using the button"""


def handle_message(update, context):
    text = str(update.message.text).lower()
    username = str(update.message.chat.first_name).lower()
    response_data = actions.bot_responses(text, username)
    response = response_data[0]

    update.message.reply_text(response)


"""This functions logs the error"""


def error(update, context):
    print(f"update {update} caused error {context.error}")


"""This function triggers all functions"""


def trigger(request):
    updater = Updater(API_KEY, use_context=True)
    dispatch = updater.dispatcher
    dispatch.add_handler(CommandHandler("start", start_command))
    dispatch.add_handler(CallbackQueryHandler(press_button_callback))
    dispatch.add_handler(CommandHandler("help", help_command))

    dispatch.add_handler(MessageHandler(Filters.text, handle_message))

    dispatch.add_error_handler(error)

    updater.start_polling()

    updater.idle()

    return JsonResponse("Check your telegram app droid is working", safe=False)
