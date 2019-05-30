#coding=utf-8
# 鼠标 webdriver.ActionChains
# 键盘 Keys


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.implicitly_wait(10)

moreproduct = dr.find_element_by_name('tj_briicon')
webdriver.ActionChains(dr).move_to_element(moreproduct).perform()
time.sleep(3)

kw = dr.find_element_by_id("kw")
#webdriver.ActionChains(dr).context_click(kw).perform()  #鼠标右击
kw.send_keys('测试') #键盘输入
time.sleep(2)
#kw.send_keys(Keys.CONTROL,'a') #组合键ctrl+a
kw.send_keys(Keys.BACK_SPACE)
time.sleep(2)
kw.send_keys(Keys.RETURN)
time.sleep(2)
dr.quit()