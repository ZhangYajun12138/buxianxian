#coding=utf-8
#弹出框操作

from selenium import webdriver
import time

dr=webdriver.Chrome()
dr.get("https://www.baidu.com")

#隐藏的元素需显示出来才能操作
setmenu = dr.find_element_by_link_text("设置")
webdriver.ActionChains(dr).move_to_element(setmenu).perform()
dr.find_element_by_link_text('搜索设置').click()
time.sleep(3)

# 未隐藏的元素可以直接选取；注释掉的是通过父级元素找后代也可以
nrset = dr.find_element_by_id("nr")
nrset.find_element_by_css_selector("option[value='50']").click()
#dr.find_element_by_css_selector("option[value='50']").click()
time.sleep(3)
#弹出框确认 三种弹出框alert（一个按钮），confirm（两个按钮），prompt（两个按钮+输入框）
dr.find_element_by_link_text("保存设置").click()
print(dr.switch_to.alert.text)
# dr.switch_to.alert.accept() #确认
#dr.switch_to_alert().dismiss() #取消
#dr.switch_to_alert().send_keys("只对prompt有效") #在弹出框输入内容

time.sleep(2)
# dr.quit()