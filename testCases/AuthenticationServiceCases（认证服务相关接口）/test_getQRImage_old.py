# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_getQRImage.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.ConfigServer import conf_appid
import unittest


class GetQrImage(unittest.TestCase):

    def setUp(self):

        self.api_url = 'xxx/auth/getQRImage'
        self.url = conf_url() + self.api_url

    def test_get_qrimage_01(self):
        u"二维码作为一级认证时，应用id正确，获取二维码认证图片请求成功"
        url = self.url
        data = {
            "appId": conf_appid(),
	        "epsessionId": ""
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

    def test_get_qrimage_02(self):
        u"应用id为空，获取二维码认证图片请求失败"
        url = self.url
        data = {
            "appId": "",
            "epsessionId": ""
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
        self.assertIn(expect_status, actual_status, msg=re['status'])

    def test_get_qrimage_03(self):
        u"应用id为空格，获取二维码认证图片请求失败"
        url = self.url
        data = {
            "appId": " ",
            "epsessionId": ""
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

    def test_get_qrimage_04(self):
        u"应用id长度为25位，获取二维码认证图片请求失败"
        url = self.url
        data = {
            "appId": "1111111111111111111111111",
            "epsessionId": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '企业应用ID长度不能超过24位;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_qrimage_05(self):
        u"应用id不存在，获取二维码认证图片请求失败"
        url = self.url
        data = {
            "appId": "xxxx",
            "epsessionId": ""
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

    def test_get_qrimage_06(self):
        u"二维码作为二级认证时，应用id正确epsessionId过期，获取二维码认证图片请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "epsessionId": "epsession:cxh:20190910235915348:3972"
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

    def test_get_qrimage_07(self):
        u"应用id正确epsessionId为空格，获取二维码认证图片请求失败"
        url = self.url
        data = {
            "appId": conf_appid(),
            "epsessionId": " "
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
