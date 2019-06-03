# coding:utf-8
# 产生指定长度的验证码，雁阵吗由大小写字母和数字构成

import random

def generate_code(code_len = 4):
    all_chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    code = ''
    for _ in range(code_len):
        code += all_chars[random.randint(0,len(all_chars)-1)]
    return code

print(generate_code(6))