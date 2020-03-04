# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_sendSmsMsg.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.ConfigPerson import ConfigPerson as CP
from ep_common.MysqldbUtil import MySqlUtil
import unittest


class SendSmsMsg(unittest.TestCase):

    def setUp(self):

        self.api_url = 'xxx/login/sendSmsMsg'
        self.url = conf_url() + self.api_url

    def test_send_smsmsg_01(self):
        u"输入合法手机号和短信内容，发送指定短信请求成功"
        url = self.url
        data = {
            "message": "短信内容",
	        "mobile": CP().conf_phone(),
	        "signature": ""
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

    def test_send_smsmsg_02(self):
        u"输入合法手机号，短信内容为空，发送指定短信请求失败"
        url = self.url
        data = {
            "message": "",
            "mobile": CP().conf_phone(),
            "signature": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '手机号和信息不能为空'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_send_smsmsg_03(self):
        u"手机号不合法，发送指定短信请求失败"
        url = self.url
        data = {
            "message": "短信内容",
            "mobile": "1232222222222222",
            "signature": ""
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

    def test_send_smsmsg_04(self):
        u"手机号为空，发送指定短信请求失败"
        url = self.url
        data = {
            "message": "短信内容",
            "mobile": "",
            "signature": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '手机号和信息不能为空'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_send_smsmsg_05(self):
        u"手机号为空串，发送指定短信请求失败"
        url = self.url
        data = {
            "message": "短信内容",
            "mobile": "      ",
            "signature": ""
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


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()