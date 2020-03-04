# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/9/25
@File : test_voiceprintCanceled.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import *
from ep_common.ConfigPerson import ConfigPerson
import unittest
from ep_common.ConfigPerson import ConfigPerson as CP
from ep_common.MysqldbUtil import MySqlUtil


class VoicePrintCanceled(unittest.TestCase):

    def setUp(self):

        self.api_url = 'coding/authinfo/voiceprintCanceled'
        self.url = conf_url() + self.api_url
        conf_person = ConfigPerson()
        self.login_name = conf_person.conf_loginName()
        self.mysql = MySqlUtil()
        self.mysql.sql_update("update ep_user_auth_info set `face_model_id` = '2' where user_id = '2'")
        self.mysql.sql_update("update ep_user_auth_info set `face_model_id` = '1' where user_id = '1'")

    def test_voicePrint_Canceled_01(self):
        u"参数正确，删除登录用户声纹请求成功"
        url = self.url
        data = {
            "loginName": CP().conf_loginName(),
            "voiceModelId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])


    def test_voicePrint_Canceled_02(self):
        u"用户名参数为空，删除声纹请求失败"
        #todo 验证缺陷
        url = self.url
        data = {
            "loginName": "",
            "voiceModelId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作失败"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def test_voicePrint_Canceled_03(self):
        u"用户名参数为空串，删除声纹请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "loginName": "   ",
            "voiceModelId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作失败"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def test_voicePrint_Canceled_04(self):
        u"用户名参数不存在，删除声纹请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "loginName": "cxh12121",
            "voiceModelId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作失败"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def test_voicePrint_Canceled_05(self):
        u"声纹参数为空，删除声纹请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "loginName": CP().conf_loginName(),
            "voiceModelId": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作失败"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def test_voicePrint_Canceled_06(self):
        u"参数正确，删除其他用户声纹请求成功"
        url = self.url
        data = {
            "loginName": "admin",
            "voiceModelId": "1"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])

    def test_voicePrint_Canceled_07(self):
        u"声纹参数为空串，删除声纹请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "loginName": CP().conf_loginName(),
            "voiceModelId": "   "
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作失败"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def test_voicePrint_Canceled_08(self):
        u"声纹参数错误，删除声纹请求失败"
        # todo 验证缺陷
        url = self.url
        data = {
            "loginName": CP().conf_loginName(),
            "voiceModelId": "222"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作失败"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])


    def tearDown(self):
        self.mysql.sql_update("update ep_user_auth_info set `face_model_id` = '' where user_id = '2'")
        self.mysql.sql_update("update ep_user_auth_info set `face_model_id` = '' where user_id = '1'")

if __name__ == "__main__":
    unittest.main()