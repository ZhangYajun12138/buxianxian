# coding:utf-8
# 列表切片

def main():
    fruits = ['grape','apple','starwberry','waxberry']
    fruits += ['pitaya','pear','mango']
    # 循环遍历列表
    for fruit in fruits:
        print(fruit.title(),end=' ')

    print('\n----------')

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)

    # fruits3 = fruits 没有复制列表只是创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)

    fruits4 = fruits[-3:-1]
    print(fruits4)

    # 可以通过反向切片操作才获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)

if __name__ == "__main__":
    main()