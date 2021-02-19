#!/usr/bin/env python
# -* - coding: utf-8 -* -
# @Time : 2021/2/1717:31
# @Author: Suyongbiao
# @File: XpathTest

'''
节点关系：父节点  子节点  同胞节点  先辈节点  后代节点
节点选择：nodename  /  //  .  ..  @  *  []
'''

import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

res = requests.get('https://www.qiushibaike.com/text/', headers=headers)
selector = etree.HTML(res.text)
# result = etree.tostring(selector, encoding='utf-8', pretty_print=True, method='html')
# print(result.decode('utf-8'))

id = selector.xpath('//div[starts-with(@id, "qiushi_tag")]/div[1]/a[2]/h2/text()')
print(id)

url_infos = selector.xpath('//div[@class="article block untagged mb15 typs_hot"]')
for url_info in url_infos:
    id = url_info.xpath('div[1]/a[2]/h2/text()')[0]
    print(id.strip('\n'))


# 标签套标签
html2 = '''
<div class="red">内容一
    <h1>内容二</h1>
</div>
'''
selector = etree.HTML(html2)
content1 = selector.xpath('//div[@class="red"]')[0]
content2 = content1.xpath('string(.)')
print(content2)
