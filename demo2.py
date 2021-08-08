# coding=utf-8
"""
date: 2021/7/10 15:45
author: lee sure
"""
# 这里的headers使用的是手机版的
import requests
from bs4 import BeautifulSoup

from retrying import retry


@retry(stop_max_attempt_number = 10)  #让被装饰的函数反复执行10次，10次全部报错才会报错， 中间有一次正常就继续往下走
def parse_url1(url,m_headers,params):
    response = requests.post(url, headers=m_headers, params=params, timeout=5)
    return response.content.decode()

# 真正的url请求函数
def parse_url(url,m_headers,params):
    try:
        html_str = parse_url1(url,m_headers,params)

    except:
        html_str = None
    return html_str

if __name__ == '__main__':
    m_headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    params = {
        'wd': '周冬雨'
    }
    url = "http://www.baidu.com/s"
    soup = BeautifulSoup(parse_url(url,m_headers,params), "html.parser")
    print(soup.prettify())
    # for link in soup.find_all('a'):
    #     if '百度百科' in str(link):
    #     # print(link.get('href'))
    #         print(link)