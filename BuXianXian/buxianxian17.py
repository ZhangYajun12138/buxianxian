# coding:utf-8
# 集合：交集，并集。差集

def main():
    set1 = {1,2,3,3,4,3,4,25}
    print(type(set1))
    print(set1)
    print("length:",len(set1))

    set2 = set(range(10))
    print(type(set2))
    print(set2)

    set1.add(5)
    print(set1)

    set1.update((10,21))# 增加元素，增加类型为list,tuple,set
    print(set1)

    set1.discard(20) # 删除元素，不存在则不删除
    print(set1)

    set1.remove(21) # 删除元素，不存在会引发异常
    print(set1)

    # 遍历
    for elem in set1:
        print(elem)

    print()

    # 将元组转换成集合
    set3 = set((2,1,2,3,6))
    print(set3)
    print(set3.pop())
    print(set3)

    # 集合的交集、并集、差集、对称差运算
    print("set1 = ",set1)
    print("set2 = ",set2)
    # 交集
    print("set1 & set2 = ",set1 & set2)
    print("set1.intersection(set2) = ",set1.intersection(set2))
    # 并集
    print("set1 | set2 = ",set1 | set2)
    print("set1.union(set2) = ",set1.union(set2))
    #差集
    print("set1 - set2 = ",set1 - set2)
    print("set1.difference(set2) = ",set1.difference(set2))
    # 在set1和set2中，但不在set1 & set2中
    print("set1 ^ set2 = ",set1 ^ set2)
    print("set1.symmetric_difference(set2) = ",set1.symmetric_difference(set2))

    # 判断子集和超集
    print("set2 <= set1 = ",set2 <= set1)
    print("set2.issubset(set1) = ",set2.issubset(set1))

    print("set2 >= set1 = ", set2 >= set1)
    print("set2.issuperset(set1) = ", set2.issuperset(set1))

if __name__ == '__main__':
    main()