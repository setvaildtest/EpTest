# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_sendSMS.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.ConfigPerson import ConfigPerson as CP
from ep_common.MysqldbUtil import MySqlUtil
import unittest


class SendSMS(unittest.TestCase):

    def setUp(self):

        self.api_url = 'xxx/login/sendSMS'
        self.url = conf_url() + self.api_url

    def test_send_sms_01(self):
        u"手机号码正确，发送短信验证码请求成功"
        url = self.url
        data = {
            "mobile": CP().conf_phone(),
	        "templateType": "sms.send.resetpwd.template"
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

    def test_send_sms_02(self):
        u"手机号码不合法，发送短信验证码请求失败"
        url = self.url
        data = {
            "mobile": "111112333333333",
            "templateType": "sms.send.resetpwd.template"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '该手机号不合法'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_send_sms_03(self):
        u"手机号码为空，发送短信验证码请求失败"
        url = self.url
        data = {
            "mobile": "",
            "templateType": "sms.send.resetpwd.template"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'fail'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_send_sms_04(self):
        u"手机号码为空串，发送短信验证码请求失败"
        url = self.url
        data = {
            "mobile": "     ",
            "templateType": "sms.send.resetpwd.template"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'fail'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_send_sms_05(self):
        u"手机号用户不存在，发送短信验证码请求失败"
        url = self.url
        data = {
            "mobile": "13458530488",
            "templateType": "sms.send.resetpwd.template"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '用户不存在或已被禁用'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()