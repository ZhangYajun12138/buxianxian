# coding:utf-8
# tuple定义和使用

def main():
    # 定义元组
    t = ("yajun",28,True,"湖北武汉")
    print(t)

    # 获取元组中的元素
    print(t[0])
    print(t[1])

    # 遍历
    for member in t:
        print(member)

    # 重新给元组赋值
    # t[0] = "luzong" 语法错误TypeError
    # 变量t重新引用了新的元组，原来的元组会被垃圾回收
    t = ("luzong",25,False,"江苏宿迁")
    print(t)

    # 将元组转换成列表，列表是可以修改元素的值的
    list1 = list(t)
    list1[1] = 26
    print(list1)

    # 将列表转换成元组
    tuple1 = tuple(list1)
    print(tuple1)

if __name__ == '__main__':
    main()