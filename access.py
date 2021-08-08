# coding=utf-8
"""
date: 2021/7/9 13:43
author: lee sure
"""
import urllib

import requests
from bs4 import BeautifulSoup

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query1 = "What's the biggest animal in the world?"
query = "Where are the important centers of the brain stem??"

for j in search(query, tld="co.in", num=10, stop=10, pause=2,verify_ssl=False):
    if ('wikipedia' in j):
        dic={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.post(j, dic,verify=False)
        result = response.text
        soup = BeautifulSoup(result, "html.parser")
        print(soup.prettify())
        break


