#coding:utf-8
#等待时间
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from launch_brower import LaunchBrower

# dr = webdriver.Firefox()
dr = Launch_brower("chrome")
dr.get("https://www.baidu.com")

dr.find_element_by_id("kw").send_keys("selenium",Keys.ENTER)
#显示等待
element = WebDriverWait(dr,10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,'Web Browser Automation'))
)
element.click()
dr.quit()