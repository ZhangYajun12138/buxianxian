# coding:utf-8
# 函数返回传入的列表中最大和第二大的元素

import random

def max_yajun(list_input):
    list = list_input[:]
    m1 = max(list)
    list.pop(list.index(m1))
    m2 = max(list)
    print(m1,m2)

l = [1,5,3,7,34,799,361]
max_yajun(l)
print(l)

print(random.randrange(start=1,stop=11,step= 1))
print(random.random())