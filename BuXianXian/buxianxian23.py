# coding:utf-8
# 计算指定的年月日时这一年的第几天

def is_leap_year(year):
    return year % 4 == 0 and year % 100 == 0 or year % 400 == 0

def which_day(year,month,day):
    day_return = 1
    each_month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

    for i in range(month-1):
        day_return += each_month_days[i]

    if is_leap_year(year) and month > 2:
        day_return += 1
    else:
        pass

    return day_return

print(which_day(2019,3,1))