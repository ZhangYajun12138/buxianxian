#coding=utf-8
from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.get('https://www.baidu.com')

js = "document.getElementById('su').style.color='red'"
dr.execute_script(js)
sleep(1)

dr.execute_script('document.getElementById("su").style.display="none"')
sleep(1)

dr.execute_script('$("#su").show()')
sleep(1)

dr.quit()