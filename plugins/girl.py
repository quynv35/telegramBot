#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import random
import re
import json




def download(url):
	data = requests.get(url).content
	f = open("girl.jpg","wb")
	f.write(data)
	f.close()

def get_link():
	link = "https://gxcl.info/api.php"
	data = requests.get(link).json()["link"]
	return(data)

def girl():
	url = get_link()
	download(url)