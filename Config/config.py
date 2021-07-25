#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def cf(file):
	f = open(file,"r")
	data = f.read()
	f.close()
	return(data)

ID = cf("./Config/id.txt")
TOKEN = cf("./Config/token.txt")
