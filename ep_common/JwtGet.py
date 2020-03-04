# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/13 0013
@File : JwtGet.py
@describe : 封装jwt生成

"""

import json
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.DoauthCheck import doauth_check
from ep_common.ConfigPerson import *
from ep_common.LogUtil import Logger

file_path = os.path.realpath(__file__)
jwt_data = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\jwt_data'

def get_jwt(type_data):
    api_url = 'xxx/auth/doauth'
    url = conf_url() + api_url
    ln = ConfigPerson().conf_loginName()
    pd = ConfigPerson().conf_password()
    data = {
        "appId": "epass_app",
        "authPara": {
            "deviceBindType": "",
            "loginName": ln,
            "password": pd
        },
        "authType": "pwd",
        "device": "app",
        "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
        "epsessionId": "",
        "hostname": "vivo X9L",
        "requestType": "1"
    }
    data = jsonTostr(data)
    dict = doauth_check(url, data)
    # l = Logger()
    # l.logger.info('JwtGet返回的参数为======>%s' % dict)
    print('JwtGet返回的参数为======>%s' % dict)
    if type_data == 'session':
        jwt = dict['body']['jwt']
        epsessionId = dict['body']['epsessionId']
        with open(jwt_data, 'w', encoding='utf-8') as f:
            f.write(jwt)
        # l.logger.info('JwtGet不加密返回的epsession参数为======>%s' % (epsessionId))
        print('JwtGet不加密返回的epsession参数为======>%s' % (epsessionId))
        return epsessionId

    elif type_data == 'jwt':
        jwt = dict['body']['jwt']
        with open(jwt_data, 'w', encoding='utf-8') as f:
            f.write(jwt)
        # l.logger.info('JwtGet不加密返回的jwt参数为:%s' % (jwt))
        print('JwtGet不加密返回的jwt参数为:%s' % (jwt))
        return jwt
    else:
        print("-------------参数错误----------------")


def get_jwt_v1(type_data):
    api_url = 'coding/auth/doauth'
    url = conf_url() + api_url
    ln = ConfigPerson().conf_loginName()
    pd = ConfigPerson().conf_password()
    data = {
        "appId": "epass_app",
        "authPara": {
            "deviceBindType": "",
            "loginName": ln,
            "password": pd
        },
        "authType": "pwd",
        "device": "app",
        "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
        "epsessionId": "",
        "hostname": "vivo X9L",
        "requestType": "1"
    }
    data = jsonTostr(data)
    dict = doauth_check(url, data)
    # l = Logger()
    # l.logger.info('JwtGet返回的参数为======>%s' % dict)
    print('JwtGet返回的参数为======>%s' % dict)
    if type_data == 'session':
        jwt = dict['body']['jwt']
        epsessionId = dict['body']['epsessionId']
        with open(jwt_data, 'w', encoding='utf-8') as f:
            f.write(jwt)
        # l.logger.info('JwtGet不加密返回的epsession参数为======>%s' % (epsessionId))
        print('JwtGet不加密返回的epsession参数为======>%s' % (epsessionId))
        return epsessionId

    elif type_data == 'jwt':
        jwt = dict['body']['jwt']
        with open(jwt_data, 'w', encoding='utf-8') as f:
            f.write(jwt)
        # l.logger.info('JwtGet不加密返回的jwt参数为:%s' % (jwt))
        print('JwtGet不加密返回的jwt参数为:%s' % (jwt))
        return jwt
    else:
        print("-------------参数错误----------------")


if __name__ == '__main__':
    # get_jwt('session')
    get_jwt_v1('jwt')