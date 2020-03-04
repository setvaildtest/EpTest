# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_getQREpsesson.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.ConfigServer import conf_appid
from ep_common.JwtGet import *
import unittest


class GetQrEpsesson(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/auth/getQREpsesson'
        self.url = conf_url() + self.api_url

    def test_get_qrepsesson_01(self):
        u"应用id和epsessionTag正确，生成认证会话请求成功"
        url = self.url
        data = {
            "appId": conf_appid(),
            "epsessionId": "",
            "epsessionTag": get_jwt_v1('session')
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

    def test_get_qrepsesson_02(self):
        u"应用id为空，生成认证会话请求失败"
        url = self.url
        data = {
            "appId": "",
            "epsessionId": "",
            "epsessionTag": get_jwt_v1('session')
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '企业应用ID不能为NULL;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_qrepsesson_03(self):
        u"应用id为空串，生成认证会话请求失败"
        url = self.url
        data = {
            "appId": "   ",
            "epsessionId": "",
            "epsessionTag": get_jwt_v1('session')
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '企业应用ID不能为NULL;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_qrepsesson_04(self):
        u"应用id不存在，生成认证会话请求失败"
        url = self.url
        data = {
            "appId": "xxx",
            "epsessionId": "",
            "epsessionTag": get_jwt_v1('session')
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

    def test_get_qrepsesson_05(self):
        u"epsessionTag为空，生成认证会话请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "epsessionId": "",
            "epsessionTag": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '认证会话标识符不能为NULL;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_qrepsesson_06(self):
        u"epsessionTag为空串，生成认证会话请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "epsessionId": "",
            "epsessionTag": "    "
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '认证会话标识符不能为NULL;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_qrepsesson_07(self):
        u"epsessionTag只要不为空，生成认证会话请求成功"
        url = self.url
        data = {
            "appId": conf_appid(),
            "epsessionId": "",
            "epsessionTag": "  12121%%**"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_qrepsesson_08(self):
        u"epsessionId已过期，生成认证会话请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "epsessionId": "epsession:cxh:20190915191802549:1744",
            "epsessionTag": "1"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '认证超时, 请在15分钟内完成所有认证挑战, 3秒后将跳转到登录页'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def test_get_qrepsesson_09(self):
        u"epsessionId参数错误，生成认证会话请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "epsessionId": "3222",
            "epsessionTag": "1"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '认证超时, 请在15分钟内完成所有认证挑战, 3秒后将跳转到登录页'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
