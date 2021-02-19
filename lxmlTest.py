#!/usr/bin/env python
# -* - coding: utf-8 -* -
# @Time : 2021/2/1717:09
# @Author: Suyongbiao
# @File: lxml

import requests
from lxml import etree

# lxml是XML和HTML的解析器，其主要功能是解析和提取XML和HTML中的数据
# 如果HTML代码不规范或者不完整，lxml解析器会自动修复或补全代码，从而提高效率
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

res = requests.get('http://www.baidu.com', headers=headers)
html = etree.HTML(res.text)
result = etree.tostring(html)
# print(result)

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('test.html', parser=parser)
result = etree.tostring(html, pretty_print=True)
print(result)