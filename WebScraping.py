# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:05:29 2022

@author: Dayanand
"""

# targeted web content from web page

#import library

import requests
import urllib.request
import time 
from bs4 import BeautifulSoup

# pointing to url

url="https://insights.blackcoffer.com/how-is-login-logout-time-tracking-for-employees-in-office-done-by-ai/"
url="https://www.indiatoday.in/business/story/india-unemployment-rate-drops-lowest-january-cmie-1908082-2022-02-03"

# sending the request to the url

response=requests.get(url)

# checking the response

response

# intitializing parser
soup=BeautifulSoup(response.text,"html.parser")

# check the soup variable
soup

# Fetching Div="description.tbl-forkorts-article.tbl-forkorts-article-active"
content=soup.find("div",{"class":"story-section"})
content

# creating the text data
article=""
for i in content.findAll("div"):
    article=article+ " " + i.text
print(article)

