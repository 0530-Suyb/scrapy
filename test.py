# a = 'www.baidu.com'
# print(a.split('.'))
# b = '  sss  '
# print(b.strip())
#
# def change_number(number):
#     print(number.replace(number[3:7], '*'*4))
# change_number('15814358779')


'''
正则表达式
一般字符：.   \    [...]
预定义字符集：\d  \D  \s  \S  \w  \W
数量词：*  +  ？  {m}  {m,n}
边界匹配：^  &  \A  \Z
(.*?) 非贪心算法
re模块修饰符：re.I  re.L  re.M  re.S  re.U  re.X
'''
import re
# a = 'xxIxxhflxxlovexxsdflhxxpythonxx'
# print(re.findall('xx(.*?)xx', a))
#
# # search()
# a = 'one1two2three3'
# infos = re.search('\d+', a)
# print(infos.group())
#
# # sub()
# phone = '123-4567-8912'
# new_phone = re.sub('\D', '', phone)
# print(new_phone)
#
# # findall()
# a = 'one1two2three3'
# infos = re.findall('\d+', a)
# print(infos)
#
# import requests
# url = 'https://list.tmall.com/search_product.htm?spm=875.7931836/B.category2016012.2.4c474265iPXOyt&q=%C4%D0%D0%AC&vmarket=&from=nanxie..pc_1_searchbutton&acm=lb-zebra-148799-667863.1003.4.708026&type=p&scm=1003.4.lb-zebra-148799-667863.OTHER_14561689118972_708026'
# res = requests.get(url)
# prices = re.findall('<em title="(.*?)"><b>&yen;</b>(.*?)</em>', res.text)
# for price in prices:
#     print(price)
#
# # re.S 匹配包括换行符在内的所有字符,实现多行匹配
# a = '''<div>hello
# </div>'''
# word = re.findall('<div>(.*?)</div>', a, re.S)
# print(word[0].strip())

str1 = '我是&quot;仙人&quot;'
str1 = str1.replace('&quot;', '"')
print(str1)