# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/7
@File : PermissionUtil.py
@describe : 接口鉴权工具，生成随机数，时间戳，encode

"""
import string
import random
import datetime
import time
from ep_common.ConfigServer import conf_operator_v1, conf_operator_v2, conf_permission_key, conf_version
from hashlib import md5
from ep_common.Headers import headers


def permission():
    if conf_version() == '2':
        bas_str = string.ascii_letters + string.digits
        print('选择生成的字符串========>>', bas_str)
        keylist = [random.choice(bas_str) for i in range(8)]
        random_str = ''.join(keylist)
        # print(random_str)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        operator = conf_operator_v2()
        permission_key = conf_permission_key()
        encode_str = operator + random_str + timestamp + permission_key
        md = md5()
        md.update(encode_str.encode('utf-8'))
        md_str = md.hexdigest()
        encode = md_str.upper()
        new_headers = headers()
        new_headers.update({"timestamp": timestamp})
        new_headers.update({"randomstr": random_str})
        new_headers.update({"encode": encode})
        # print(timestamp,random_str,encode)
        print(new_headers)
        return new_headers
    elif conf_version() == '1':
        bas_str = string.ascii_letters + string.digits
        print('选择生成的字符串========>>', bas_str)
        keylist = [random.choice(bas_str) for i in range(8)]
        random_str = ''.join(keylist)
        # print(random_str)
        timestamp = int(round(time.time() * 1000))
        print(timestamp)
        # print(type(timestamp))
        appuser = conf_operator_v1()
        permission_key = conf_permission_key()
        encode_str = appuser + random_str + str(timestamp) + '{' + permission_key + '}'
        print(encode_str)
        md = md5()
        md.update(encode_str.encode('utf-8'))
        md_str = md.hexdigest()
        encode = md_str.upper()
        new_headers = headers()
        new_headers.update({"timestamp": str(timestamp)})
        new_headers.update({"randomcode": random_str})
        new_headers.update({"encode": encode})
        # print(timestamp,random_str,encode)
        print('鉴权v1.0new_header============>',new_headers)
        return new_headers


if __name__ == '__main__':
    permission()
