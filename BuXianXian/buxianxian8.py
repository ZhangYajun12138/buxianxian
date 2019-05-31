# coding:utf-8

'''

打印三角形
Version：0.1
Author：不羡仙
Date：2019-5-30
   *    3  1
  ***   2  3
 *****  1  5
******* 0   7
            n =4
'''

n = 4
for i in range(1,n+1):
    print(" "*(n-i),end='')
    print("*"*(2*i-1),end='')
    print()
