#!/usr/bin/python
#-*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/9/11
@File : test_customAuthChain.py
@describe : 该模块包括鉴权1.0BAM融合 - 创建自定义认证链路接口的测试用例

"""
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.ConfigPerson import ConfigPerson
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide

class CustomAuthChain(unittest.TestCase):
    def setUp(self):
        api_url = "coding/bam/customAuthChain"
        self.url = conf_url() + api_url
        self.login_name = ConfigPerson().conf_loginName()  # 获取测试用户login_name

    def test_customAuthChain_01(self):
        u'认证链不为空，其余非必填参数不填，请求成功'
        data ={
            "amSessionId": "",
            "authListChain": "pwd",
            "businessId": "",
            "loginName": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_customAuthChain_02(self):
        u'认证链不为空，loginName存在，请求成功'
        data ={
            "amSessionId": "",
            "authListChain": "pwd",
            "businessId": "",
            "loginName": self.login_name
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_customAuthChain_03(self):
        u'认证链为空,请求失败'
        data = {
            "amSessionId": "",
            "authListChain": "",
            "businessId": "",
            "loginName": self.login_name
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "认证链不能为空;"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_customAuthChain_04(self):
        u'loginName不存在,请求失败'
        data = {
            "amSessionId": "",
            "authListChain": "pwd",
            "businessId": "",
            "loginName": "notfound"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "用户不存在，创建失败"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_customAuthChain_05(self):
        u'loginName为NULL,请求失败'
        data = {
            "amSessionId": "",
            "authListChain": "pwd",
            "businessId": "OA"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言
        expect_message = "loginName不能为NULL;"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)


if __name__ == "__main__":
    unittest.main()