# coding:utf-8

'''

输入月薪和五险一金计算个人所得税
version：0.1
author：buxianxian
date:2019-5-30
rate：税率
1.起征5000
2.8000以内，0.1 105
3.12000以内，0.2，555
4.30000以内，0.3.1005
5.50000以内，0.4，2755
6.以上，0.5，5055

'''

salary = float(input("月薪："))
insurance = float(input("五险一金："))
diff = salary - insurance -5000

if salary <= 5000:
    rate = 0
elif salary <=8000:
    rate = 0.1
elif salary <=12000:
    rate = 0.2
elif salary <=30000:
    rate = 0.3
elif salary <=50000:
    rate = 0.4
else:
    rate = 0.5

result = diff*rate
print(salary-result)
