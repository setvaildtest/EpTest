# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_verify.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import *
from ep_common.ConfigServer import conf_appid
import unittest


class Verify(unittest.TestCase):

    def setUp(self):

        self.api_url = 'coding/jwt/verify'
        self.url = conf_url() + self.api_url

    def test_verify_01(self):
        u"应用id、jwt正确，令牌校验请求成功"
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
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_verify_02(self):
        u"应用id为空，令牌校验请求失败"
        url = self.url
        data = {
            "appId": "",
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
        expect_status = '企业应用ID不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_verify_03(self):
        u"应用id为空串，令牌校验请求失败"
        url = self.url
        data = {
            "appId": "   ",
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
        expect_status = '企业应用ID不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_verify_04(self):
        u"应用id不存在，令牌校验请求失败"
        url = self.url
        data = {
            "appId": "xxx",
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
        expect_status = '企业应用ID不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_verify_05(self):
        u"jwt为空，令牌校验请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwtVerify": "true",
            "jwt": "",
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

    def test_verify_06(self):
        u"jwt为空串，令牌校验请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": "    ",
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

    def test_verify_07(self):
        u"jwt错误，令牌校验请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": "111111",
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
        expect_status = 'JWT解析失败'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_verify_08(self):
        u"jwt已过期，令牌校验请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": "eyJhbGciOiJIUzI1NiJ9.eyJlcHRva2VuIjoidG9rZW46MTU2ODEwNjgyMzQwNSIsImFwcGlkIjoiY3hoX2FwcCIsInN1YnRva2VuIjoiIiwidXNlcmlkIjoiY3hoIiwiaWF0IjoiMjAxOS0wOS0xMCAwMi4xMy40MyIsInVwZHQiOiIyMDE5LTA5LTEwIDAyLjEzLjQzIn0.hPLuvJP_wPtcXE63FjR4YfQyvqYvoN0ne5Jh8BcPlsA",
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
        expect_status = 'JWT解析失败'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_verify_09(self):
        u"token参数有值，令牌校验请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "jwt": get_jwt_v1('jwt'),
            "jwtVerify": "true",
            "token": "111"
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