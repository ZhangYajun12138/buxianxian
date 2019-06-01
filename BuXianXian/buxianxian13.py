# coding:utf-8
# 列表排序

def main():
    list1 = ['orange','apple','zoo','internationalization','blueberry']
    list2 = sorted(list1)
    # sort函数返回列表排序后的拷贝，不会修改传入的列表。函数的设计就应该像sorted函数一样尽可能不要产生副作用
    list3 = sorted(list1,reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序二不是默认的字母表顺序
    list4 = sorted(list1,key=len,reverse=True)

    print(list1)
    print(list2)
    print(list3)
    print(list4)

    # 给列表对象发出排序消息，直接在列表对象上进行排序
    list1.sort(reverse=True,key=len)
    print(list1)

if __name__ =="__main__":
    main()