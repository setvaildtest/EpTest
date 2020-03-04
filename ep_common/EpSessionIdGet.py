# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/21 0021
@File : EpSessionIdGet.py
@describe : 获取用户会话id方法

"""

import json
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.DoauthCheck import doauth_check


def get_sessionId():
    api_url = 'coding/auth/doauth'
    url = conf_url() + api_url
    data = {
        "appId": "epass_app",
        "authPara": {
            "deviceBindType": "",
            "loginName": "wj03",
            "password": "123456"
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
    print(dict)
    # print(dict['code'])
    if 'u' not in dict:
        epsessionId = dict['body']['epsessionId']
        print(epsessionId)
        return epsessionId
    elif 'u' in dict:
        u = dict['u']
        print(type(u))
        print('u：',dict['u'])
        u_dict = json.loads(u)
        epsessionId = u_dict['body']['epsessionId']
        print('jwt：',epsessionId)
        return epsessionId

if __name__ == '__main__':
    get_sessionId()
