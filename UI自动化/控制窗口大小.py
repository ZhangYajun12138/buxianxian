#coding=utf-8
#控制窗口大小，前进，后退
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.runoob.com/html/html-tutorial.html')
sleep(2)

driver.set_window_size(480,800)
sleep(2)

driver.set_window_size(900,1000)
sleep(2)

driver.get('http://www.runoob.com')
sleep(2)

driver.back()
print('back to url:',driver.current_url)
sleep(2)

driver.forward()
print("forward to url:",driver.current_url)
sleep(2)

driver.close()