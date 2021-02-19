#!/usr/bin/env python
# -* - coding: utf-8 -* -
# @Time : 2021/2/1710:17
# @Author: Suyongbiao
# @File: liuxinghudiejian

import requests
import re
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

f = open('流星蝴蝶剑.txt', 'w+')

def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>', res.content.decode('GBK'), re.S)
        contents[0] = contents[0].replace('&quot;', '"')
        contents = contents[0].split('<br /><br />')
        for content in contents:
            f.write(content+'\n')
    else:
        f.write('\n\n<章节缺失>\n\n')
        print('缺失')

if __name__ == '__main__':
    urls = ['https://www.gulongwang.com/liu/{}.html'.format(number) for number in range(256, 258)]
    for url in urls:
        get_info(url)
        time.sleep(1)
f.close()