#!/usr/bin/env python
# -* - coding: utf-8 -* -
# @Time : 2021/2/1718:46
# @Author: Suyongbiao
# @File: csv

import csv

fp = open('book.csv', 'w+')
writer = csv.writer(fp)
writer.writerow(('id', 'name'))
writer.writerow(('1', '小米'))
writer.writerow(('2', '小张'))