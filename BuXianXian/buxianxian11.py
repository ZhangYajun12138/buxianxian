# coding:utf-8
# 列表

def main():
    list1 = [1,3,5,7,100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    # 计算列表长度，元素个数
    print(len(list1))
    print(len(list2))
    # 下标运算
    print(list1[0])
    print(list2[4])
    # 添加元素
    list1.append(55)
    list2.append("aa")
    list1.insert(1,25)
    list2 += ["bb","cc"]
    print(list1)
    print(list2)
    # 删除元素
    list1.remove(3)
    print(list1)

    for i in range(10):
        if i in list1:
            list1.remove(i)

    print(list1)
    #清空列表元素
    list1.clear()
    print(list1)


if __name__ == "__main__":
    main()