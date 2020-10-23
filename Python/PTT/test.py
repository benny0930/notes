# -*- coding: utf-8 -*-
import requests
import bs4
import os
import time
from threading import Thread
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
URL = 'https://ck101.com/forum-3866-1.html?order_by=dateline'
headers = {'cookie': 'over18=1;',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
response = requests.get(URL, headers=headers)
soup = bs4.BeautifulSoup(response.text, "html.parser")
print soup
