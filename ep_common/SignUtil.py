# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/7
@File : SignUtil.py
@describe : 接口参数签名工具

"""

import json
from hashlib import md5
from ep_common.Headers import headers
from ep_common.ConfigServer import conf_sign_key


def sign(data):
    sign_key = conf_sign_key()
    # print(sign_key)
    data1 = json.JSONEncoder().encode(data)
    data2 = eval(repr(data1).replace('\\', ''))
    data3 = data2[1:]
    # print('s_data3：', data3)
    data4 = data3[:-1]
    print('【准备签名的参数】：', data4)
    print('【参数类型：】',type(data4))
    print('-' * 130)
    sign = sign_key + data4
    print('【签名密钥和参数拼接后的结果sign】：', sign)
    print('-' * 130)
    md = md5()
    md.update(sign.encode('utf-8'))
    md_hex = md.hexdigest().upper()
    print('【签名后的结果】：', md_hex)
    print('-' * 130)
    new_headers = headers()
    new_headers.update({"sign": md_hex})
    print('【生成签名后生成新的headers】：',new_headers)
    print('-' * 130)
    return new_headers

if __name__ == '__main__':
    sign_str = '123'
    sign(sign_str)
