#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import config
from telegram import Update
from telegram.ext import CallbackContext

ID = config.ID
TOKEN = config.TOKEN
host = "https://api.telegram.org/bot"+TOKEN

def grab(message): #84943687522
	phone = message.split(" ")[1]
	link = "https://api.grab.com/grabid/v1/oauth2/otp"
	data = {
		"client_id":"4da4649307cc4bfaa16b08d03432535e",
		"transaction_ctx":"null",
		"country_code":"VN",
		"method":"CALL",
		"num_digits":"6",
		"phone_number":""
		}
	data["phone_number"] = "84"+phone[1:]
	res = requests.post(link,json=data)
	result = "{0}\nStatus_Code: {1}\n{2}".format(phone,res,res.text)
	return(result)


def airbnb(message): #phone = 84943687522
	phone = message.split(" ")[1]
	link = "https://www.airbnb.co.in/api/v2/phone_one_time_passwords?currency=VND&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=vi"
	data = {
		"phoneNumber":"",
		"workFlow":"GLOBAL_SIGNUP_LOGIN",
		"otpMethod":"CALL"
		}
	data["phoneNumber"] = "84" + phone[1:]
	res = requests.post(link, json = data)
	result = "{0}\nStatus_Code: {1}\n{2}".format(phone,res,res.text)
	return(result)
