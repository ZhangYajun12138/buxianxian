# coding:utf-8

'''

猜数字游戏
计算机随机一个1-100的整数
用户输入，提示大了/小了/猜对
Version：0.1
Author：不羡仙
Date：2019-5-30

'''

from random import randint
answer = randint(1,100)
count = 0
while True:
    number = int(input("> "))
    count += 1

    if number == answer:
        print("猜对了")
        break # 跳出这一层循环
    elif number > answer:
        print("大了")
    else:
        print("小了")

print("the count:",count)
print("the number is:",answer)