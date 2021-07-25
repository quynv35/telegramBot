#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def config(file):
	f = open(file,"r")
	data = f.read()
	f.close()
	return(data)

ID = config("./Config/id.txt")
TOKEN = config("./Config/token.txt")

