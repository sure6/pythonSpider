# coding=utf-8
"""
date: 2021/7/10 15:01
author: lee sure
"""
import re
import string
import sys
import urllib.request
from urllib.parse import quote

from bs4 import BeautifulSoup

print(sys.getdefaultencoding())

# m_header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
# }
key = input("请输入关键字: ")
url = "http://www.baidu.com/s?wd=" + key + "&usm=3&rsv_idx=2&rsv_page=1"
url_request = quote(url, safe=string.printable)  # 解决ascii编码报错问题，不报错则可以注释掉
response = urllib.request.urlopen(url_request)
result = response.read().decode('utf-8')
soup = BeautifulSoup(result, "html.parser")
# print(soup.prettify())
for link in soup.find_all('a'):
    if '百度百科' in str(link):
        # print(link.get('href'))
        content = urllib.request.urlopen(link.get('href')).read().decode('utf-8')
        info = BeautifulSoup(content, "html.parser")
        for text in info.find_all('div', {'class':'para'}):
            dr = re.compile(r'<[^>]+>', re.S)  # 获取所有的标签
            dd = dr.sub('', str(text))  # 去除所有标签
            print(dd.strip())
else:
    print("没有找到")
