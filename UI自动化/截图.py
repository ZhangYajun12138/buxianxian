#coding:utf-8
# for a in range(1,8):
# 	for b in range(1,5):
# 		for c in range(1,4):
# 			print(a*100+b*10+c,end='--')

from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")

dr.find_element_by_id('kw').send_keys('selenium')
re = dr.get_screenshot_as_file(r"D:\张亚军\WEB测试\Python File\学习了\UI自动化\baidu.png")
print(re)

dr.find_element_by_id('su').click()
sleep(1)
re = dr.save_screenshot(r"D:\张亚军\WEB测试\Python File\学习了\UI自动化\baidu1.png")
print(re)

print("base64:",dr.get_screenshot_as_base64())
print("binary:",dr.get_screenshot_as_png())

dr.quit()