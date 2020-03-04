# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/9/25
@File : test_getAppWakeUspType.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import *
from ep_common.ConfigPerson import ConfigPerson
import unittest
from ep_common.ConfigPerson import ConfigPerson as CP


class GetAppWakeUspType(unittest.TestCase):

    def setUp(self):

        self.api_url = 'coding/authinfo/getAppWakeUspType'
        self.url = conf_url() + self.api_url
        conf_person = ConfigPerson()
        self.login_name = conf_person.conf_loginName()

    def test_get_AppWake_UspType_01(self):
        u"用户名参数正确，获取APP唤醒方式请求成功"
        url = self.url
        data = {
            "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])

    def test_get_AppWake_UspType_02(self):
        u"用户名参数为空，获取APP唤醒方式请求失败"
        url = self.url
        data = {
            "loginName": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "用户名不能为空"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])

    def test_get_AppWake_UspType_03(self):
        u"用户名参数为空串，获取APP唤醒方式请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "loginName": "    "
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "用户名不能为空"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])

    def test_get_AppWake_UspType_04(self):
        u"用户名参数不存在，获取APP唤醒方式请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "loginName": "cxh12121"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "用户名不存在"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()