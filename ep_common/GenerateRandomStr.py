# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/9/11
@File : GenerateRandomStr.py
@describe : 生成一个指定长度的随机字符串

"""

import random

def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

if __name__ == '__main__':
    f = generate_random_str(256)
    print(f)