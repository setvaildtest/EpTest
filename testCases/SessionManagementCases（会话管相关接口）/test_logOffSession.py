#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/21
@File : test_logOffSession.py
@describe : 该模块测试会话注销接口，该接口需要登录，根据tokenKey来注销用户会话

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.ConfigRedis import conf_redis
from ep_common.JwtGet import get_jwt
from ep_common.ConfigPerson import ConfigPerson
import redis
import unittest
import os


class LogOffSession(unittest.TestCase):
    def setUp(self):
        if len(conf_redis()) == 4:
            host, port, db, password = conf_redis()
            self.r = redis.StrictRedis(host=host, port=port, db=db, password=password)
        elif len(conf_redis()) == 3:
            host, port, db = conf_redis()
            self.r = redis.StrictRedis(host=host, port=port, db=db)
        self.api_url = 'coding/v3/session/logOffSession'
        self.url = conf_url() + self.api_url
        self.loginName = ConfigPerson().conf_loginName()
        # 登录,生成tokenkey
        get_jwt('jwt')
    def test_logoff_session_01(self):
        u'登录之后请求会话注销接口，请求成功'
        # 从redis中获取当前登录用户的tokenKey，tokens值为集合，转换成列表后，获取最后一个key值即为最新的tokenkey
        token_set = self.r.smembers('tokens:' + self.loginName)
        token_list = list(token_set)
        tokenKey = token_list[-1].decode()
        print("tokenKey:", tokenKey)
        print('会话注销api_url：=================>', self.url)
        data = {
            "loginName": self.loginName,
            "tokenKey": tokenKey
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('会话注销接口入参：=================>\n', data)
        print('会话注销接口响应：=================>\n', re)
        expect_message = '操作成功'
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_logoff_session_02(self):
        u'tokenKey为空，请求失败'
        print('会话注销api_url：=================>', self.url)
        data = {
            "loginName": self.loginName,
            "tokenKey": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('会话注销接口入参：=================>\n', data)
        print('会话注销接口响应：=================>\n', re)
        expect_message = "tokenKey不能为空或空串;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_logoff_session_03(self):
        u'tokenKey为空串，请求失败'
        print('会话注销api_url：=================>', self.url)
        data = {
            "loginName": self.loginName,
            "tokenKey": "              "
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('会话注销接口入参：=================>\n', data)
        print('会话注销接口响应：=================>\n', re)
        expect_message = "tokenKey不能为空或空串;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_logoff_session_04(self):
        u'登录名为空，请求失败'
        print('会话注销api_url：=================>', self.url)
        data = {
            "loginName": "",
            "tokenKey": "token:1568185485129"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('会话注销接口入参：=================>\n', data)
        print('会话注销接口响应：=================>\n', re)
        expect_message = '登录名不能为空或空串;'
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_logoff_session_05(self):
        u'登录名为空串，请求失败'
        print('会话注销api_url：=================>', self.url)
        data = {
            "loginName": "          ",
            "tokenKey": "token:1568185485129"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('会话注销接口入参：=================>\n', data)
        print('会话注销接口响应：=================>\n', re)
        expect_message = '登录名不能为空或空串;'
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def tearDown(self):
        # 清空jwt_data中的已失效的jwt
        file_path = os.path.dirname(__file__)  # 获取当前目录
        parent_path = os.path.dirname(file_path)  # 获得当前所在目录的父级目录
        jwt_data_path = os.path.dirname(parent_path) + '\\ep_config\\jwt_data'
        open(jwt_data_path, "w").close()


if __name__ == "__main__":
    unittest.main()
