#coding=utf-8
# 通过js操作滚动条

from selenium import webdriver
import time
#打开网站
browser = webdriver.Chrome()
# browser.get("http://www.magicalign.com/pc/about_us.html")
# time.sleep(2)
#
# #向下滚动1000像素
# js="document.documentElement.scrollTop=1000"
# browser.execute_script(js)
# time.sleep(2)
#
# #回顶部
# js="document.documentElement.scrollTop=0"
# browser.execute_script(js)
# time.sleep(2)

#找到某个元素，scrollIntoView让当前的元素滚动到浏览器窗口的可视区域内
# js="var div1=document.getElementsByLinkText('公司资讯').scrollIntoView();"
# browser.execute_script(js)
# time.sleep(5)

#缩小窗口显示水平滚动条
browser.set_window_size(500,800)
browser.get("http://www.bing.com")
time.sleep(2)
js=" document.documentElement.scrollLeft=1000"
browser.execute_script(js)
time.sleep(2)
js="document.documentElement.scrollLeft=0"
browser.execute_script(js)
time.sleep(2)

browser.quit()