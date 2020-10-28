# -*- coding: utf-8 -*-
import requests
import bs4
import os , json
import time
from threading import Thread
import requests.packages.urllib3
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

requests.packages.urllib3.disable_warnings()
aPTTRead = aHNBangRead = []
aIGRead = {}
aJKFRead = {}
aCKRead = {}
iLoopIndex = 0
iGIFIndex = 0
iIMGIndex = 0

file_path2 = "./shotUrl.txt"
if not os.path.isfile(file_path2):
    f2 = open(file_path2, 'w')
    f2.close()

f2 = open(file_path2, 'r')
file_data = f2.read()
f2.close()

print file_data
aShotUrl = json.loads(file_data)
print aShotUrl
aShotUrl['url_555'] = "5555"
aShotUrl['url_666'] = "6666"

