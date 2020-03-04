# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/7
@File : EncrypyUtil.py
@describe : 接口请求参数加密工具

"""

import base64
import json
from gmssl.sm4 import CryptSM4,SM4_ENCRYPT,SM4_DECRYPT
from ep_common import ConfigServer
from ep_common import JsonToStrUtil

def encrypt(data):
    print('测试用例接口请求的data：',data)
    key = ConfigServer.conf_encrypt_key()
    print('加密的key：',key)
    b_key = str.encode(key)
    print('key的类型：',type(b_key))
    s_data1 = json.JSONEncoder().encode(data)
    # print('s_data1：',s_data1)
    s_data2 = eval(repr(s_data1).replace('\\', ''))
    s_data3 = s_data2[1:]
    # print('s_data3：',s_data3)
    s_data4 = s_data3[:-1]
    # print('s_data4：',s_data4)
    # print('加密的参数：',s_data4)
    # print('加密参数的类型：',type(s_data4))
    b_data = bytes(s_data4,encoding='utf-8')
    encrypt_sm4 = CryptSM4()
    encrypt_sm4.set_key(b_key,SM4_ENCRYPT)
    encrypt_value = encrypt_sm4.crypt_ecb(b_data)
    b64 = base64.b64encode(encrypt_value)
    print('加密后：', b64)
    str_b64 = str(b64,encoding='utf-8')
    return str_b64


def decrypt(data):

    b64_data = base64.b64decode(data)
    decrypt_sm4 = CryptSM4()
    key = ConfigServer.conf_encrypt_key()
    b_key = str.encode(key)
    decrypt_sm4.set_key(b_key, SM4_DECRYPT)
    decrypt_value = decrypt_sm4.crypt_ecb(b64_data)
    print('解密后的字符串==============>',decrypt_value.decode('utf-8'))
    return decrypt_value.decode('utf-8')


if __name__ == '__main__':
    dec_str = 'XhYmIALSXTbM4LhTZONfHJxUcPHwmrzK1b38velV6TB5H6GXMA9ZC30hQK2cmpuEdsJ1mV50F0tjk5REwQg16SoArXSF2OycdU7xNS3rFdU7FleFchxfd7rY7Qynw6NrhDZLkDbWAX7Rpf5J7SIcAxwVSAbifGS/eHpbwObr1os='
    decrypt(dec_str)
