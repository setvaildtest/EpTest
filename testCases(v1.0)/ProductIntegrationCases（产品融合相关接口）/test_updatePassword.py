#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/27
@File : test_updatePassword.py
@describe : 该模块用于测试鉴权1.0 bim融合-企业用户管理-密码更新接口

"""
import time
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson
import os

class UpdatePassword(unittest.TestCase):
    def setUp(self):
        api_url = "coding/userInfo/updatePassword"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        self.conf_person=ConfigPerson()
        self.login_name = self.conf_person.conf_loginName()


    def test_update_password_01(self):
        u'所有参数正确，请求成功'
        print('密码更新api_url：=================>', self.url)
        new_password="111111"
        data = {
            "loginName": self.login_name,
            "passExpireDate": "20230712235959",
            "password": new_password
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('密码更新接口入参：=================>\n', data)
        print('密码更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 断言数据
        expect_password = "28C981CC911D3AC7EAA3CEA49D3E7D94"
        self.mysql.cursor.execute("select password from ep_users where login_name='%s'"%self.login_name)
        actual_password = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_password, actual_password)
        #同步修改配置文件的用户密码
        self.conf_person.conf_write_passwd(new_password)

    def test_update_password_02(self):
        u'用户不存在，请求失败'
        print('密码更新api_url：=================>', self.url)
        data = {
            "loginName": "notfoundUser",
            "passExpireDate": "20230712235959",
            "password": "123456"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('密码更新接口入参：=================>\n', data)
        print('密码更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "用户不存在"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_update_password_03(self):
        u'用户名为空，请求失败'
        print('密码更新api_url：=================>', self.url)
        data = {
            "loginName": "",
            "passExpireDate": "20230712235959",
            "password": "123456"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('密码更新接口入参：=================>\n', data)
        print('密码更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "参数错误;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_update_password_04(self):
        u'新密码为空，请求失败'
        print('密码更新api_url：=================>', self.url)
        data = {
            "loginName": self.login_name,
            "passExpireDate": "20230712235959",
            "password": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('密码更新接口入参：=================>\n', data)
        print('密码更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "参数错误;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_update_password_05(self):
        u'新密码为空串，请求失败'
        print('密码更新api_url：=================>', self.url)
        data = {
            "loginName": self.login_name,
            "passExpireDate": "20230712235959",
            "password": "      "
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('密码更新接口入参：=================>\n', data)
        print('密码更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "参数错误;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def tearDown(self):
        # 清空jwt_data中的jwt，避免会话失效的情况
        file_path = os.path.dirname(__file__)  # 获取当前目录
        parent_path = os.path.dirname(file_path)  # 获得当前所在目录的父级目录
        jwt_data_path = os.path.dirname(parent_path) + '\\ep_config\\jwt_data_v1.txt'
        open(jwt_data_path, "w").close()




if __name__ == "__main__":
    unittest.main()
