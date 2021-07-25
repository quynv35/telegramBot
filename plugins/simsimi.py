#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from telegram import Update
from telegram.ext import CallbackContext


global TOKEN, ID, host

TOKEN = "1192446009:AAGYuFawbHfoafNaJvRke0vjy2ViYCspeDY"
ID = "-1001234961377"


host = "https://api.telegram.org/bot"+TOKEN


def simsimi(update: Update, context: CallbackContext) -> None:
	text = update.message.text
	link = "https://simsumi.herokuapp.com/api?text={0}&lang=vi".format(text)
	data = requests.get(link).json()
	text = 'data["success"]'
	# gui len telegram
	link = "{0}/sendMessage?chat_id={1}&text={2}".format(host,ID,text)
	data = requests.get(link)

