#coding:utf-8
#异常

from selenium import webdriver
dr = webdriver.Firefox()
dr.get("http://www.baidu.com")


try:
    dr.find_element_by_id('kw').send_keys("异常处理finally") #故意写错id，定位不到元素
    dr.find_element_by_id('su').click()
except Exception as e:
    print(e)
else :
    print("else")
finally:
    print("finally")   #不论有无异常都会执行

dr.quit()