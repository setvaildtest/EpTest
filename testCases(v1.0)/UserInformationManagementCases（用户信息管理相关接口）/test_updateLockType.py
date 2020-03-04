# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/9/25
@File : test_updateLockType.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import *
from ep_common.ConfigPerson import ConfigPerson
import unittest
from ep_common.ConfigPerson import ConfigPerson as CP


class UpdateLockType(unittest.TestCase):

    def setUp(self):

        self.api_url = 'coding/authinfo/updateLockType'
        self.url = conf_url() + self.api_url
        conf_person = ConfigPerson()
        self.login_name = conf_person.conf_loginName()

    def test_update_LockType_01(self):
        u"参数正确，认证管理解锁设置请求成功"
        url = self.url
        data = {
            "lockType": "password",
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

    def test_update_LockType_02(self):
        u"用户名参数为空，认证管理解锁设置请求失败"
        url = self.url
        data = {
            "lockType": "password",
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

    def test_update_LockType_03(self):
        u"用户名参数为空串，认证管理解锁设置请求失败"
        #todo 验证缺陷
        url = self.url
        data = {
            "lockType": "password",
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

    def test_update_LockType_04(self):
        u"锁定方式参数为空，认证管理解锁设置请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "lockType": "",
            "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "唤醒方式不能为空"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])

    def test_update_LockType_05(self):
        u"锁定方式为空串，认证管理解锁设置请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "lockType": "   ",
            "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "唤醒方式不能为空"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])

    def test_update_LockType_06(self):
        u"用户名参数不存在，认证管理解锁设置请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "lockType": "password",
            "loginName": "cxh1212"
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