# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/13
@File : DoauthCheck.py
@describe : 对请求doauth接口具体鉴权方式的路径判断

"""

import json
from ep_common import ConfigServer
from ep_common import Headers
from ep_common import PermissionUtil
from ep_common import SignUtil
from ep_common import EncrypyUtil
from ep_common.LogUtil import Logger
from ep_common.RequestsUtil import post
from ep_common.JwtGetSignEncryptPermission import jwt_per_enc_sign


def doauth_check(url=None, data=None):
    permission = int(ConfigServer.conf_type_Permission())
    encrypt = int(ConfigServer.conf_type_Encrypt())
    sign = int(ConfigServer.conf_type_Sign())
    value = jwt_per_enc_sign(permission, encrypt, sign)
    # l = Logger()
    # l.logger.info('获取到configServer鉴权加密签名的值为：%s' % value)
    # print('获取到configServer鉴权加密签名的值为：%s' % value)

    # 全部关闭
    if value == 0:
        headers = Headers.headers()
        dict = post(url, data, headers)
        return dict

    # 开启鉴权
    elif value == 1:
        headers = PermissionUtil.permission()
        print(headers)
        print(url)
        print(data)
        dict = post(url, data, headers)
        return dict

    # 开启加密
    elif value == 2:
        headers = Headers.headers()
        print('请求头；', headers)
        u = EncrypyUtil.encrypt(data)
        u_data = {
            "u": u
        }
        print('u_data：', u_data)
        print('u_data数据类型：', type(u_data))
        str_u_data = json.dumps(u_data)
        print('str_u_data数据：', str_u_data)
        print('str_u_data数据类型：', type(str_u_data))
        dict = post(url, str_u_data, headers)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>',new_str_u,type(new_dict))
        return new_dict

    # 开启【签名】
    elif value == 3:
        headers = SignUtil.sign(data)
        dict = post(url, data, headers)
        return dict

    # 开启【鉴权，加密】
    elif value == 4:
        headers = PermissionUtil.permission()
        print('请求头；', headers)
        u = EncrypyUtil.encrypt(data)
        u_data = {
            "u": u
        }
        print('u_data：', u_data)
        print('u_data数据类型：', type(u_data))
        str_u_data = json.dumps(u_data)
        print('str_u_data数据：', str_u_data)
        print('str_u_data数据类型：', type(str_u_data))
        dict = post(url, str_u_data, headers)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict

    # 开启【鉴权，签名】
    elif value == 5:
        headers = SignUtil.sign(data)
        headers.update(PermissionUtil.permission())
        print(headers)
        dict = post(url, data, headers)
        print('=======>' * 20, dict)
        return dict

    # 开启【加密，签名】
    elif value == 6:
        u = EncrypyUtil.encrypt(data)
        u_data = {
            "u": u
        }
        str_u_data = json.dumps(u_data)
        headers = SignUtil.sign(str_u_data)
        print('【加密后请求的参数】：', str_u_data)
        print('【加密后请求的参数类型】：', type(str_u_data))
        print('-' * 130)
        dict = post(url, str_u_data, headers)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict

    # 开启【鉴权，加密，签名】
    elif value == 7:
        headers = PermissionUtil.permission()
        u = EncrypyUtil.encrypt(data)
        u_data = {
            "u": u
        }
        print('u_data：', u_data)
        print('u_data数据类型：', type(u_data))
        str_u_data = json.dumps(u_data)
        headers.update(SignUtil.sign(str_u_data))
        print('str_u_data：', str_u_data)
        print('str_u_data：', type(str_u_data))
        dict = post(url, str_u_data, headers)
        print('-' * 130)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        print(decrypt_value)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict
