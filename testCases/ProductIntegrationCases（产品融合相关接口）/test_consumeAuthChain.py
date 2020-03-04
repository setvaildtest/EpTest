#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/9/11
@File : test_consumeAuthChain.py
@describe :  该模块包括鉴权2.0BAM融合 - 消费认证链接口的测试用例

"""
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.ConfigPerson import ConfigPerson
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide


class ConsumeAuthChain(unittest.TestCase):
    def setUp(self):
        api_url = "coding/bam/consumeAuthChain"
        self.url = conf_url() + api_url
        self.login_name = ConfigPerson().conf_loginName()  # 获取测试用户login_name

    def  custom_auth_chain(self,authListChain,loginName):
        # 请求创建认证链接口获取epSessionid
        customAuthChain_url = conf_url() + "coding/bam/customAuthChain"
        customAuthChain_data = {
            "amSessionId": "",
            "authListChain": authListChain,
            "businessId": "",
            "loginName": loginName
        }
        customAuthChain_data = jsonTostr(customAuthChain_data)
        customAuthChain_re = sceneDecide(customAuthChain_url, customAuthChain_data)
        print("创建认证链：", customAuthChain_re)
        epSessionId = customAuthChain_re['body']['epSessionId']
        return epSessionId

    def test_consumeAuthChain_01(self):
        u'必填参数正确，请求成功'
        # 创建认证链
        epSessionId = self.custom_auth_chain("pwd,voice|face", self.login_name)
        # 消费认证链
        data = {
            "appName": "OA",
            "authResult": True,
            "authType": "pwd",
            "device": "web",
            "epSessionid": epSessionId,
            "hostName": "ie",
            "userId": self.login_name,
            "userIp": "192.168.0.31"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_consumeAuthChain_02(self):
        u'epsessionid为空，请求失败'
        data = {
            "appName": "OA",
            "authResult": True,
            "authType": "pwd",
            "device": "web",
            "epSessionid": "",
            "hostName": "ie",
            "userId": self.login_name,
            "userIp": "192.168.0.31"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print("data:", data)
        print("re:", re)
        # 断言
        expect_message = "系统错误，请联系管理员"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_consumeAuthChain_03(self):
        u'当前待消费的认证方式为空，请求失败'
        # 创建认证链
        epSessionId = self.custom_auth_chain("pwd,voice|face", self.login_name)
        data = {
            "appName": "OA",
            "authResult": True,
            "authType": "",
            "device": "web",
            "epSessionid": epSessionId,
            "hostName": "ie",
            "userId": self.login_name,
            "userIp": "192.168.0.31"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print("data:", data)
        print("re:", re)
        # 断言
        expect_message = "当前待消费的认证方式不能为空;"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_consumeAuthChain_04(self):
        u'userId为空，请求失败'
        # 创建认证链
        epSessionId = self.custom_auth_chain("pwd,voice|face", self.login_name)
        data = {
            "appName": "OA",
            "authResult": True,
            "authType": "pwd",
            "device": "web",
            "epSessionid": epSessionId,
            "hostName": "ie",
            "userId": "",
            "userIp": "192.168.0.31"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print("data:", data)
        print("re:", re)
        # 断言
        expect_message = "用户id不能为空;"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_consumeAuthChain_05(self):
        u'userIp为空，请求失败'
        # 创建认证链
        epSessionId = self.custom_auth_chain("pwd,voice|face", self.login_name)
        data = {
            "appName": "OA",
            "authResult":True,
            "authType": "pwd",
            "device": "web",
            "epSessionid": epSessionId,
            "hostName": "ie",
            "userId": self.login_name,
            "userIp": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "用户ip不能为空;"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_consumeAuthChain_06(self):
        u'用户设备为空，请求失败'
        # 创建认证链
        epSessionId = self.custom_auth_chain("pwd,voice|face", self.login_name)
        # 消费认证链
        data = {
            "appName": "OA",
            "authResult": True,
            "authType": "pwd",
            "device": "",
            "epSessionid": epSessionId,
            "hostName": "ie",
            "userId": self.login_name,
            "userIp": "192.168.0.31"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)

        # 断言
        expect_message = "用户设备不能为空;"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_consumeAuthChain_07(self):
        u'epsessionid格式错误，请求失败'
        # 创建认证链
        epSessionId = self.custom_auth_chain("pwd,voice|face", "")
        # 消费认证链
        data = {
            "appName": "OA",
            "authResult": True,
            "authType": "pwd",
            "device": "web",
            "epSessionid": epSessionId,
            "hostName": "ie",
            "userId": self.login_name,
            "userIp": "192.168.0.31"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "epSessionid格式错误"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_consumeAuthChain_08(self):
        u'认证链中未包含该认证方式，请求失败'
        # 创建认证链
        epSessionId = self.custom_auth_chain("pwd,voice|face", self.login_name)
        # 消费认证链
        data = {
            "appName": "OA",
            "authResult": True,
            "authType": "aaa",
            "device": "web",
            "epSessionid": epSessionId,
            "hostName": "ie",
            "userId": self.login_name,
            "userIp": "192.168.0.31"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "不能消费该认证方式：认证链中未包含该认证方式"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_consumeAuthChain_09(self):
        u'认证链已消费完成，请求失败'
        # 创建认证链
        epSessionId = self.custom_auth_chain("pwd,voice|face", self.login_name)
        # 消费认证链
        data = {
            "appName": "OA",
            "authResult": True,
            "authType": "pwd",
            "device": "web",
            "epSessionid": epSessionId,
            "hostName": "ie",
            "userId": self.login_name,
            "userIp": "192.168.0.31"
        }
        data = jsonTostr(data)
        sceneDecide(self.url, data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "不能消费该认证方式：认证链已消费完成"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_consumeAuthChain_10(self):
        u'当前待消费认证方式已经消费当前认证方式前还有未消费的认证方式，请求失败'
        # 创建认证链
        epSessionId = self.custom_auth_chain("pwd,voice|face", self.login_name)
        # 消费认证链
        data = {
            "appName": "OA",
            "authResult": True,
            "authType": "face",
            "device": "web",
            "epSessionid": epSessionId,
            "hostName": "ie",
            "userId": self.login_name,
            "userIp": "192.168.0.31"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "不能消费该认证方式：当前待消费认证方式已经消费当前认证方式前还有未消费的认证方式"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)


if __name__ == "__main__":
    unittest.main()
