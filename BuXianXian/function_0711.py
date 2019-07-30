# coding:utf-8
# 函数
'''
类型属于对象，变量是没有类型的
可更改对象：string,tuple,number,参数传递时，值，函数内修改不会影响原值
不可更改对象:list,dict，参数传递时，引用，函数内修改会影响原值
参数：
    必备参数，必须与函数声明时一致的顺序来传递参数
    关键字参数，传递参数时可与函数声明的顺序不一样，应为可以用参数名来匹配参数值
    缺省参数，保持默认值
    不定长参数，定义时，参数名前加*号，按顺序输入时进行对应
    匿名函数，lambda
变量作用域：
    全局变量，global
    局部变量
'''


def change_int(a):
    a = 10
    print('a =', a)


b = 2
change_int(b)
print('b =', b)


def change_me(mylist):
    mylist.append(1)
    print('内部', mylist)


mylist = [12, 34, 56]
change_me(mylist)
print('函数外', mylist)


# 定义不定长参数
def printinfo(arg1, *vartuple):
    print("输出:", arg1)
    for var in vartuple:
        print("不定长", var)


# 调用不定长参数
printinfo(10)
printinfo(10, 23, 45, 321)
# 定义匿名函数
sum = lambda arg1, arg2: arg1 + arg2
# 调用匿名函数
print("相加后：", sum(10, 30))

