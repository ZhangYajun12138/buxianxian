# coding:utf-8

import json

def jsonp_to_json(jsonp_string):
    """get jsonstr from jsonpstr=callback(jsonstr)"""

    left = jsonp_string.find('(') #找到第一个(的索引
    json_string = json.loads(jsonp_string[left+1:-1])  # 取callback()括号里的内容
    return json_string


