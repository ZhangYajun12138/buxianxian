# coding:utf-8

'''

将华氏温度转换成摄氏温度
F = 1.8C + 32
Version：0.1
Author：不羡仙
Date：2019-5-30

'''

f = float(input("请输入华氏温度："))
c = (f-32)/1.8
print("%.1f华氏度 = %.1f摄氏度" %(f,c))