#coding:utf-8

'''

最大公约数和最小公倍数
Version：0.1
Author：不羡仙
Date：2019-5-30

'''

x = int(input("x= "))
y = int(input("y= "))

if x < y:
    (x,y) = (y,x)

for i in range(x,0,-1):

    if i == 1:
        print("无公约数")
        print("公倍数:",x*y)
        break

    if x%i == 0 and y%i == 0:
        print("最大公约数：",i)
        print("最小公倍数：",int(x*y/i))
        break