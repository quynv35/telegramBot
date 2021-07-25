#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import json
import os
import config
from telegram import Update
from telegram.ext import CallbackContext





# youtube-dl can't be use :((





ID = config.ID
TOKEN = config.TOKEN
host = "https://api.telegram.org/bot"+TOKEN

# https://rapidapi.com/convertisseur.mp3.video/api/youtube-search1/endpoints
def yt1(message):
	keyword = message[9:]
	url = "https://youtube-search1.p.rapidapi.com/{0}".format(keyword)
	headers = {
	    'x-rapidapi-host': "youtube-search1.p.rapidapi.com",
	    'x-rapidapi-key': "0cc733e278mshc6dfccfbf2203f6p16914djsnc108e3d901f5"
	    }
	data = requests.request("GET", url, headers=headers).json()["items"][0]
	url = data["url"]
	title = data["title"]
	thumbHigh = data["thumbHigh"]
	viewCount = data["viewCount"].replace("Aufrufe","views")
	result = "<URL> : {0}\n\n<TITLE> : {1}\n\n<VIEWS> : {2}".format(url,title,viewCount)
	return(result,url,thumbHigh)


# https://rapidapi.com/marindelija/api/youtube-search-results/endpoints
def yt2(keyword):
	url = "https://youtube-search-results.p.rapidapi.com/youtube-search/"
	querystring = {"q":""}
	querystring["q"] = keyword
	headers = {
	    'x-rapidapi-host': "youtube-search-results.p.rapidapi.com",
	    'x-rapidapi-key': "0cc733e278mshc6dfccfbf2203f6p16914djsnc108e3d901f5"
	    }
	data = requests.request("GET", url, headers=headers, params=querystring).json()["items"]

	list_view = [] #tim video co view max
	for i in data:
		try:
			list_view.append(i["views"])
		except:
			continue
	index = list_view.index(max(list_view))

	data = data[index]

	url = data["url"]
	title = data["title"]
	thumbnail = data["bestThumbnail"]["url"]
	views = data["views"]
	uploaded_at = data["uploadedAt"]
	thumb = getThumb(thumbnail)
	result = "🔗 : {0}\n\n🎵 : {1}\n\n👀 : {2}\n\n🕒 : {3}\n".format(url,title,views,uploaded_at)
	return(result,url)

def getThumb(link) -> None:
	data = requests.get(link).content
	f = open("thumb.jpg","wb")
	f.write(data)
	f.close()


def mp4(update: Update, context: CallbackContext) -> None:
	message = update.message.text
	keyword = message[5:]

	if "https://" in message:
		idvideo = message.split("/")[-1].replace("watch?v=","")
		link = "https://www.youtube.com/watch?v="+idvideo
		result = ""
	else:
		data = yt2(keyword)
		result = data[0]
		link = data[1]
	os.system("youtube-dl -f mp4 {0} --audio-quality 0 -f best".format(link))
	os.system("mv *.mp4 youtube.mp4")
	
	# gui den telegram
	files = {"video": open("./youtube.mp4","rb")}
	link = "{0}/sendVideo?chat_id={1}&caption={2}".format(host,ID,result+link)
	data = requests.get(link,files=files)



def mp3(update: Update, context: CallbackContext) -> None:
	message = update.message.text
	keyword = message[5:]

	if "https://" in message:
		idvideo = message.split("/")[-1].replace("watch?v=","")
		link = "https://www.youtube.com/watch?v="+idvideo
		result = ""
	else:
		data = yt2(keyword)
		result = data[0]
		link = data[1]
	os.system("youtube-dl -f m4a {0} --audio-quality 0".format(link))
	os.system("mv *.m4a youtube.m4a")

	# gui den telegram
	files = {"audio": open("./youtube.m4a","rb")}
	link = "{0}/sendAudio?chat_id={1}&caption={2}".format(host,ID,result+link)
	data = requests.get(link,files=files)

