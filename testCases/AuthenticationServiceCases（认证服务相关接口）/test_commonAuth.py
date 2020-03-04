# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/20
@File : commonAuth(认证方式验证接口).py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.ConfigPerson import ConfigPerson as CP


class CommonAuth(unittest.TestCase):

    def setUp(self) -> None:
        self.api_url = 'xxx/auth/commonAuth'
        self.url = conf_url() + self.api_url

    def test_commonauth_01(self):
        u'用户名作为登录名，正确的用户名密码，请求成功'
        data = {
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_commonauth_02(self):
        u'用户名为空，输入密码，认证失败，缺少参数'
        data = {
            "authPara": {
                "deviceBindType": "",
                "loginName": '',
                "password": CP().conf_password()
            },
            "authType": "pwd"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '认证失败，缺少参数'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_commonauth_03(self):
        u'输入正确的用户名，密码为空，认证失败，缺少参数'
        data = {
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": ''
            },
            "authType": "pwd"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '认证失败，缺少参数'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_commonauth_04(self):
        u'输入正确的用户名，错误的密码，提示账号或密码错误'
        data = {
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": '123123'
            },
            "authType": "pwd"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '账号或密码错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def test_commonauth_05(self):
        u'输入不存在的用户名，错误的密码，提示用户不存在或已被禁用'
        data = {
            "authPara": {
                "deviceBindType": "",
                "loginName": 'test007',
                "password": '123123'
            },
            "authType": "pwd"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '用户不存在或已被禁用'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_commonauth_06(self):
        u'手机号码作为登录名，正确的号码密码，请求成功'
        data = {
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_phone(),
                "password": CP().conf_password()
            },
            "authType": "pwd"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_commonauth_07(self):
        u'邮箱作为登录名，正确的邮箱密码，请求成功'
        data = {
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_email(),
                "password": CP().conf_password()
            },
            "authType": "pwd"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

if __name__ == '__main__':
    unittest.main()