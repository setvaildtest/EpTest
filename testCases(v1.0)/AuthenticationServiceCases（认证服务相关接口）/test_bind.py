# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_bind.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import*
from ep_common.ConfigServer import conf_appid
import unittest


class Bind(unittest.TestCase):

    def setUp(self):

        self.api_url = 'coding/jwt/bind'
        self.url = conf_url() + self.api_url

    def test_bind_01(self):
        u"所有参数正确，票据互信绑定请求成功"
        url = self.url
        data = {
            "appId": conf_appid(),
	        "jwt": get_jwt_v1('jwt'),
            "jwtVerify": "true",
	        "token": "ASDL234235651616SADFADF1A6"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_bind_02(self):
        u"jwt参数为空，票据互信绑定请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": "",
            "jwtVerify": "true",
            "token": "ASDL234235651616SADFADF1A6"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_bind_03(self):
        u"jwt参数为空串，票据互信绑定请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": "     ",
            "jwtVerify": "true",
            "token": "ASDL234235651616SADFADF1A6"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_bind_04(self):
        u"jwt参数错误，票据互信绑定请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": "2ewewqwqq",
            "jwtVerify": "true",
            "token": "ASDL234235651616SADFADF1A6"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'JWT解析失败'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_bind_05(self):
        u"jwt参数已过期，票据互信绑定请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": "eyJhbGciOiJIUzI1NiJ9.eyJlcHRva2VuIjoidG9rZW46MTU2ODEwNjgyMzQwNSIsImFwcGlkIjoiY3hoX2FwcCIsInN1YnRva2VuIjoiIiwidXNlcmlkIjoiY3hoIiwiaWF0IjoiMjAxOS0wOS0xMCAwMi4xMy40MyIsInVwZHQiOiIyMDE5LTA5LTEwIDAyLjEzLjQzIn0.hPLuvJP_wPtcXE63FjR4YfQyvqYvoN0ne5Jh8BcPlsA",
            "jwtVerify": "true",
            "token": "ASDL234235651616SADFADF1A6"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'JWT解析失败'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_bind_06(self):
        u"token为空，票据互信绑定请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": get_jwt_v1('jwt'),
            "jwtVerify": "true",
            "token": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_bind_07(self):
        u"token为空串，票据互信绑定请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": get_jwt_v1('jwt'),
            "jwtVerify": "true",
            "token": "     "
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_bind_08(self):
        u"token参数错误，票据互信绑定请求成功"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": get_jwt_v1('jwt'),
            "jwtVerify": "true",
            "token": "     "
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

