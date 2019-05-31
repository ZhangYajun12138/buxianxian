# coding:utf-8

'''

判断素数
Version：0.1
Author：不羡仙
Date：2019-5-30

'''

from math import sqrt
lists = range(2,100)
result_list = []
result_list2 = []

for i in lists:
    for j in range(2,(int(sqrt(i)))+1):
        if i%j == 0:
            result_list.append(i)
    if i not in result_list:
        result_list2.append(i)

print("非素数是：",result_list)
print("素数是：",result_list2)