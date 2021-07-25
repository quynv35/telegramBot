#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import json
import os 
from Config import config

global TOKEN, ID, host
ID = config.ID
TOKEN = config.TOKEN
host = "https://api.telegram.org/bot"+TOKEN

# print(ID)
# print(TOKEN)

def infor():
	link = "{0}/getMe".format(host)
	data = requests.get(link).json()["result"]
	Id = data["id"]
	first_name = data["first_name"]
	username = data["username"]
	return(Id,first_name,username)

def sendMessage(text):
	link = "{0}/sendMessage?chat_id={1}&text={2}".format(host,ID,text)
	data = requests.get(link)
	return(data,data.text)

def sendPhoto(f,cap):
	files = {"photo": open(f,"rb")}
	link = "{0}/sendPhoto?chat_id={1}&caption={2}".format(host,ID,cap)
	data = requests.get(link,files=files)
	return(data,data.text)

def sendAudio(f,cap):
	files = {"audio": open(f,"rb")}
	link = "{0}/sendAudio?chat_id={1}&caption={2}".format(host,ID,cap)
	data = requests.get(link,files=files)
	return(data,data.text)

def sendVideo(f,cap):
	files = {"video": open(f,"rb")}
	link = "{0}/sendVideo?chat_id={1}&caption={2}".format(host,ID,cap)
	data = requests.get(link,files=files)
	return(data,data.text)

def exportChatInviteLink():
	link = "{0}/exportChatInviteLink?chat_id={1}".format(host,ID)
	data = requests.get(link).json()["result"]
	mess = "Invite Link: {0}".format(data)
	return(sendMessage(mess))

# -----------------------------------------



from telegram import Update, ForceReply,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

from plugins.lookup import lookup
from plugins.say import say
from plugins.youtube import mp3,mp4

def sms(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
            InlineKeyboardButton("Option 4", callback_data='4'),


        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text("Selected option: {0}".format(query.data))

def help_cmd(update: Update, context: CallbackContext) -> None:
	menu = """/help - show this help menu
/hi - say hi
/"""
	update.message.reply_text(menu)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    # dispatcher.add_handler(CommandHandler("sms", sms))
    # dispatcher.add_handler(CommandHandler("help", help_cmd))
    dispatcher.add_handler(CommandHandler("lookup", lookup))
    # dispatcher.add_handler(CommandHandler("call", call))
    dispatcher.add_handler(CommandHandler("say", say))
    dispatcher.add_handler(CommandHandler("mp3", mp3))
    dispatcher.add_handler(CommandHandler("mp4", mp4))

    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, simsimi))

    # Start the Bot
    updater.start_polling()
    updater.idle()

main()