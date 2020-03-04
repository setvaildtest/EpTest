# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/7
@File : SceneDecide.py
@describe : 鉴权用户所有业务的判断

"""

import requests
import json
from ep_common import ConfigServer
from ep_common.SignEncryptPermission import SignEncryptPermission
from ep_common import PermissionUtil
from ep_common import SignUtil
from ep_common import EncrypyUtil
from ep_common import SessionGet
from ep_common.RequestsUtil import post, get


def sceneDecide(url=None, data=None, type_data=None):
    # permission, encrypt, sign, session = Config.conf_type()
    # # SignEncryptPermission(permission, encrypt, sign, session)
    permission = int(ConfigServer.conf_type_Permission())
    encrypt = int(ConfigServer.conf_type_Encrypt())
    sign = int(ConfigServer.conf_type_Sign())
    session = int(ConfigServer.conf_type_session())
    value = SignEncryptPermission(permission, encrypt, sign, session)
    print(value)

    # 全部关闭
    if value == 0:
        if type_data == 'get':
            # headers = Headers.headers()
            headers = SessionGet.session()
            dict = get(url, data, headers)
            return dict
        else:
            headers = SessionGet.session()
            dict = post(url, data, headers)
            return dict

    # 开启【鉴权】
    elif value == 1:
        if type_data == 'get':
            headers = PermissionUtil.permission()
            print(headers)
            print(url)
            print(data)
            headers.update(SessionGet.session())
            print(headers)
            dict = get(url, data, headers)
            return dict
        else:
            headers = PermissionUtil.permission()
            print(headers)
            print(url)
            print(data)
            headers.update(SessionGet.session())
            print(headers)
            dict = post(url, data, headers)
            return dict

    # 开启【加密】
    elif value == 2:
        headers = SessionGet.session()
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
        # print(decrypt_value)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict

    # 开启【签名】
    elif value == 3:
        headers = SignUtil.sign(data)
        headers.update(SessionGet.session())
        dict = post(url, data, headers)
        return dict

    # 开启【会话】
    elif value == 4:
        headers = SessionGet.session()
        print('session准备转递的headers为：', headers)
        dict = post(url, data, headers)
        return dict

    # 开启【鉴权加密】
    elif value == 5:
        headers = PermissionUtil.permission()
        headers.update(SessionGet.session())
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
        r_text = requests.post(url=url, data=str_u_data, headers=headers).text
        dict = json.loads(r_text)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        # print(decrypt_value)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict

    # 开启【鉴权加密签名】
    elif value == 6:
        headers = PermissionUtil.permission()
        u = EncrypyUtil.encrypt(data)
        u_data = {
            "u": u
        }
        print('u_data：', u_data)
        print('u_data数据类型：', type(u_data))
        str_u_data = json.dumps(u_data)
        headers.update(SignUtil.sign(str_u_data))
        headers.update(SessionGet.session())
        print('str_u_data：', str_u_data)
        print('str_u_data：', type(str_u_data))
        r_text = requests.post(url=url, data=str_u_data, headers=headers).text
        print('-' * 130)
        dict = json.loads(r_text)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        print(decrypt_value)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict

    # 开启【鉴权加密签名会话】
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
        headers.update(SessionGet.session())
        print('str_u_data：', str_u_data)
        print('str_u_data：', type(str_u_data))
        dict = post(url, str_u_data, headers)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        print(decrypt_value)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict

    # 开启【鉴权签名】
    elif value == 8:
        headers = SignUtil.sign(data)
        headers.update(PermissionUtil.permission())
        headers.update(SessionGet.session())
        print(headers)
        dict = post(url, data, headers)
        return dict

    # 开启【鉴权会话】
    elif value == 9:
        headers = PermissionUtil.permission()
        headers.update(SessionGet.session())
        print('======================>>>>>', headers)
        dict = post(url, data, headers)
        return dict

    # 开启【加密签名】
    elif value == 10:
        u = EncrypyUtil.encrypt(data)
        u_data = {
            "u": u
        }
        str_u_data = json.dumps(u_data)
        headers = SignUtil.sign(str_u_data)
        headers.update(SessionGet.session())
        print('【加密后请求的参数】：', str_u_data)
        print('【加密后请求的参数类型】：', type(str_u_data))
        print('-' * 130)
        print('请求的Headers头：', headers)
        dict = post(url, str_u_data, headers)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict

    # 开启【加密会话】
    elif value == 11:
        headers = SessionGet.session()
        u = EncrypyUtil.encrypt(data)
        u_data = {
            "u": u
        }
        str_u_data = json.dumps(u_data)
        dict = post(url, str_u_data, headers)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict

    # 开启【签名会话】
    elif value == 12:
        headers = SignUtil.sign(data)
        headers.update(SessionGet.session())
        dict = post(url, data, headers)
        return dict

    # 开启【鉴权加密会话】
    elif value == 13:
        headers = PermissionUtil.permission()
        headers.update(SessionGet.session())
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
        r_text = requests.post(url=url, data=str_u_data, headers=headers).text
        dict = json.loads(r_text)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        # print(decrypt_value)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict

    # 开启【鉴权签名会话】
    elif value == 14:
        headers = SignUtil.sign(data)
        headers.update(PermissionUtil.permission())
        headers.update(SessionGet.session())
        print(headers)
        dict = post(url, data, headers)
        return dict

    # 开启【加密签名会话】
    elif value == 15:
        u = EncrypyUtil.encrypt(data)
        u_data = {
            "u": u
        }
        str_u_data = json.dumps(u_data)
        headers = SignUtil.sign(str_u_data)
        headers.update(SessionGet.session())
        print('【加密后请求的参数】：', str_u_data)
        print('【加密后请求的参数类型】：', type(str_u_data))
        print('-' * 130)
        print('请求的Headers头：', headers)
        dict = post(url, str_u_data, headers)
        u_dict = dict['u']
        decrypt_value = EncrypyUtil.decrypt(u_dict)
        new_str_u = decrypt_value
        new_dict = json.loads(new_str_u)
        print('============================>>>', new_str_u, type(new_dict))
        return new_dict
