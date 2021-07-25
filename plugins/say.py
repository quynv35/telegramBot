#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from gtts import gTTS 

from plugins import config
from telegram import Update
from telegram.ext import CallbackContext

ID = config.ID
TOKEN = config.TOKEN
host = "https://api.telegram.org/bot"+TOKEN

def say(update: Update, context: CallbackContext) -> None:
	message = update.message.text
	
	language = message.split(" ")[1]
	mytext = message[7:]
	
	myobj = gTTS(text=mytext, lang=language, slow=False) 
	myobj.save("voice.mp3") 
  
	# gui den telegram
	files = {"audio": open("voice.mp3","rb")}
	link = "{0}/sendAudio?chat_id={1}&caption={2}".format(host,ID,mytext)
	data = requests.get(link,files=files)
