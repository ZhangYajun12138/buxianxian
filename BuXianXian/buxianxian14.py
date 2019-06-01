# coding:utf-8
#  列表的生成式语法来创建列表

import sys

def main():
    f = [x for x in range(10)]
    print(f)

    f = [x + y for x in "ABC" for y in "123"]
    print(f)
    print(len(f))

    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后，元素已经准备就绪所以需要耗费较多的内存空间
    f = [x**2 for x in range(1000)]
    print(sys.getsizeof(f))

    # 生成器对象：不占用额外的空间，每次迭代计算，需要花费时间
    f = (x**2 for x in range(1000))
    print(sys.getsizeof(f))
    print(f)
    for i in f:
        print(i)

if __name__ == '__main__':
    main()