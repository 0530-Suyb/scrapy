#!/usr/bin/env python
# -* - coding: utf-8 -* -
# @Time : 2021/2/1623:56
# @Author: Suyongbiao
# @File: kugou

import requests
from bs4 import BeautifulSoup
import time

# 请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# 爬取函数
def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')  # 网站数据解析为soup文档
    ranks = soup.select('span.pc_temp_num')     # selector
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().split('-')[0],
            'song': title.get_text().split('-')[1],
            'time': time.get_text().strip()
        }
        print(data)

if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(number) for number in range(1, 5)]
    for url in urls:
        get_info(url)
    time.sleep(1)