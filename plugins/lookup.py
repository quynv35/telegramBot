#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import json
from plugins import config
from telegram import Update
from telegram.ext import CallbackContext


ID = config.ID
TOKEN = config.TOKEN
host = "https://api.telegram.org/bot"+TOKEN


def lookup(update: Update, context: CallbackContext) -> None:
	message = update.message.text
	phone = "+84" + message[1:]
	url = "https://veriphone.p.rapidapi.com/verify"
	querystring = {"phone":""}
	querystring["phone"] = phone
	headers = {
	    'x-rapidapi-host': "veriphone.p.rapidapi.com",
	    'x-rapidapi-key': "0cc733e278mshc6dfccfbf2203f6p16914djsnc108e3d901f5"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring).json()
	
	phone = message.split(" ")[1]

	if response["phone_valid"] == True:
		valid = phone + " is valid phone number."
	else:
		valid = phone + " is not valid phone number."
	
	network = response["carrier"]

	result = "{0}\n{1}".format(valid,network)

	# gui len telegram
	link = "{0}/sendMessage?chat_id={1}&text={2}".format(host,ID,result)
	data = requests.get(link)


