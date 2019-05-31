# coding:utf-8

'''

九九乘法表
Version：0.1
Author：不羡仙
Date：2019-5-30

'''

for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" %(j,i,i*j),end='\t')
    print("\n")