# coding:utf-8
# from selenium import webdriver
# import re
#
# dr = webdriver.Chrome()
# dr.get('https://www.baidu.com')
#
# source = dr.page_source
# # print(source)
#
# linklist = re.findall(r'<a.*?</a>',source)
# print(len(linklist))
#
# for link in linklist:
#     print(link)
#
# dr.quit()

import requests

print(dir(requests))