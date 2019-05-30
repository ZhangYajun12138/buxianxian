#coding=utf-8
#cookie的增删改查

from selenium import webdriver

dr=webdriver.Chrome()
dr.get("http://www.baidu.com")

#所有cookies查询
cookies = dr.get_cookies()
print('cookies的类型： ',type(cookies)) #打印出来是list类型
print('cookie的类型： ',type(cookies[0])) #元素是dict类型
print('打印出所有的cookie: ')
for cookie in cookies:
    #print(cookie)
    print(cookie["name"],'-----',cookie["value"])

#查询单个cookie
print("baiduid:", dr.get_cookie('BAIDUID'))
#删除cookie
dr.delete_cookie("BAIDUID")
print(dr.get_cookie("BAIDUID")) #已删除 none
#增加cookie
dr.add_cookie({"name":"testcookie","value":"testcookievalue"})
print(dr.get_cookie('testcookie'))
dr.add_cookie({"name":"zhang","value":"yajun"})
print(dr.get_cookie(name='zhang'))
#修改cookie
dr.add_cookie({"name":"testcookie","value":"modify-testcookievalue"})
print(dr.get_cookie("testcookie"))

dr.quit()