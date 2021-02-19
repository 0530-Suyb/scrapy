#!/usr/bin/env python
# -* - coding: utf-8 -* -
# @Time : 2021/2/1622:06
# @Author: Suyongbiao
# @File: example1

'''
https://bj.xiaozhu.com
https://bj.xiaozhu.com/search-duanzufang-p2-0/
'''

from bs4 import BeautifulSoup
import requests
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# def judge_sex(class_name):
#     if class_name == ['member_girl_ico']:
#         return '女'
#     else:
#         return '男'

def get_links(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('#sjina_C20_02 > a')
    for link in links:
        href = 'http:' + link.get('href')
        print(href)
        get_info(href)

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.information > div.inf_left1 > div > h1 > strong')
    addresses = soup.select('#xfptxq_B04_12 > span')
    prices = soup.select('div.information > div.information_li.mb5 > div.inf_left.fl.mr30 > span')
    imgs = soup.select('#imageShowBig > li.bannerbg.hover > div > a > img')
    ping = soup.select('#xfptxq_B04_42')
    # names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    # sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')
    for title, address, price, img, ping in zip(titles, addresses, prices, imgs, ping):
        data = {
            'title': title.get_text().strip(),
            'address': address.get_text().strip(),
            'price': price.get_text(),
            'img': img.get('src'),
            'ping': ping.get_text()
            # 'name': name.get_text(),
            # 'sex': judge_sex(sex.get('class'))
        }
        print(data)

if __name__ == '__main__':
    urls = ['https://newhouse.fang.com/house/s/b9{}/'.format(number) for number in range(1, 4)]
    for url in urls:
        get_links(url)
        time.sleep(2)
