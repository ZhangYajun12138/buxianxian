# coiding:utf-8
'''

输入年份，如果是闰年输出True，否则输出False
Version：0.1
Author：不羡仙
Date：2019-5-30

'''
while True:
    year = input("请输入年份：\n")
    if year == "q":
        exit(0)
    else:
        year = int(year)
        is_leap = (year%4 == 0 and year%100 != 0 or year%400 == 0)
        print(is_leap)

