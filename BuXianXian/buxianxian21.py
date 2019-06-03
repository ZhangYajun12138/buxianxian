# coding:utf-8
# 函数返回给定文件的后缀名

def get_suffix(filename,has_dot=False):
    pos = filename.rfind('.') # rfind是从字符串右边开始查询子字符串，匹配到的第一个索引，索引是从前往后的
    print(pos)
    if 0 < pos < len(filename)-1:# 如果“.”不是开头，不是结尾
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

print(get_suffix(filename="ac3v.exe",has_dot=True))
# print('-----')
# print(get_suffix(filename="acv.y02236"))