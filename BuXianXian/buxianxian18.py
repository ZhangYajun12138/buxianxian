# coding:utf-8
# dictionary字典

def main():
    scores = {
        "yajun":100,
        "luozng":95,
        "lige":88
    }

    # 通过key可以获取字典中对应的值
    print(scores["yajun"])
    print(scores["luozng"])

    #遍历
    for item in scores:
        print("key:",item,"---value:",scores[item])

    # 更新
    scores["yajun"] = 99
    print(scores["yajun"])
    scores.update(yajun = 88)
    print(scores["yajun"])
    print(scores.get("yajun",60))

    # 删除
    # print(scores.popitem())
    # print(scores)
    print(scores.pop('luzong',95))
    print(scores)

    # 清空
    scores.clear()
    print(scores)

if __name__ == '__main__':
    main()