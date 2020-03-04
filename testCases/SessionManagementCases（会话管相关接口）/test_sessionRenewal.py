#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/21
@File : test_sessionRenewal.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import get_jwt
from ep_common.DoauthCheck import doauth_check
import time
import unittest
import os

class SessionRenewal(unittest.TestCase):
    def setUp(self):
        self.api_url = 'coding/sessionManager/sessionRenewal'
        self.url = conf_url() + self.api_url

    def test_session_renewal_01(self):
        u'登录之后请求会话续期接口，请求成功'
        #登录写入jwt_data,避免jwt失效
        get_jwt('jwt')
        print('会话续期api_url：=================>', self.url)
        data = {}
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('会话续期接口入参：=================>\n', data)
        print('会话续期接口响应：=================>\n', re)
        # 断言
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_session_renewal_02(self):
        u'不传jwt，请求失败'
        print('会话续期api_url：=================>', self.url)
        data = {}
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print('会话续期接口入参：=================>\n', data)
        print('会话续期接口响应：=================>\n', re)
        # 断言
        expect_status = "fail"
        actual_staus = re['status']
        self.assertIn(expect_status, actual_staus)

if __name__ == "__main__":
    unittest.main()
