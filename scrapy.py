#!/usr/bin/env python
# -* - coding: utf-8 -* -
# @Time : 2021/2/1619:59
# @Author: Suyongbiao
# @File: scrapy

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
res = requests.get('https://bj.xiaozhu.com/', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.prettify())
# print(soup.find_all('div', 's_tab_inner'))
# print(soup.find_all('div', attrs={'class': 's_tab_inner'}))
prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > span > i')
for price in prices:
    print(price.get_text())

# try:
#     print(res.text)
# except ConnectionError:
#     print('拒绝连接')
# except TimeoutError:
#     print('连接超时')
# except:
#     print('其他错误或异常')
'''
Requests库的错误和异常
ConnectionError
HTTPError
URLRequired
ConnectTimeout
Timeout
TooManyRedirects
raise_for_status()  状态非200，抛出HTTPError
'''

