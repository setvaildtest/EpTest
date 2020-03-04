#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/9/23
@File : test_updatePasswordById.py
@describe : 鉴权1.0 BIM融合 - 企业用户管理 - 根据ID更新用户密码

"""
import time
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson
import os


class UpdatePasswordById(unittest.TestCase):
    def setUp(self):
        api_url = "coding/userInfo/updatePasswordById"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        self.conf_user = ConfigPerson()
        self.mysql.cursor.execute("select id from ep_users where login_name='%s'" % self.conf_user.conf_loginName())
        self.conf_user_id = self.mysql.cursor.fetchone()[0]

    def test_update_password_01(self):
        u'所有参数正确，请求成功'
        print('密码更新api_url：=================>', self.url)
        new_password = "111111"
        data = {
            "id": self.conf_user_id,
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
        time.sleep(1)
        expect_password = "28C981CC911D3AC7EAA3CEA49D3E7D94"
        self.mysql.cursor.execute("select password from ep_users where id=%s" % self.conf_user_id)
        actual_password = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_password, actual_password)
        # 同步修改配置文件的用户密码
        self.conf_user.conf_write_passwd(new_password)

    def test_update_password_02(self):
        u'用户不存在，请求失败'
        print('密码更新api_url：=================>', self.url)
        new_password = "111111"
        data = {
            "id": 999,
            "passExpireDate": "20230712235959",
            "password": new_password
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('密码更新接口入参：=================>\n', data)
        print('密码更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "用户不存在"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_update_password_03(self):
        u'用户id为空，请求失败'
        print('密码更新api_url：=================>', self.url)
        new_password = "111111"
        data = {
            "id": "",
            "passExpireDate": "20230712235959",
            "password": new_password
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('密码更新接口入参：=================>\n', data)
        print('密码更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "参数错误"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_update_password_04(self):
        u'新密码为空，请求失败'
        print('密码更新api_url：=================>', self.url)
        new_password = ""
        data = {
            "id": self.conf_user_id,
            "passExpireDate": "20230712235959",
            "password": new_password
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('密码更新接口入参：=================>\n', data)
        print('密码更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "参数错误"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_update_password_05(self):
        u'新密码为空串，请求失败'
        print('密码更新api_url：=================>', self.url)
        new_password = "      "
        data = {
            "id": self.conf_user_id,
            "passExpireDate": "20230712235959",
            "password": new_password
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('密码更新接口入参：=================>\n', data)
        print('密码更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "参数错误"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def tearDown(self):
        # 清空jwt_data中的jwt，避免会话失效的情况
        file_path = os.path.dirname(__file__)  # 获取当前目录
        parent_path = os.path.dirname(file_path)  # 获得当前所在目录的父级目录
        jwt_data_path = os.path.dirname(parent_path) + '\\ep_config\\jwt_data_v1.txt'
        open(jwt_data_path, "w").close()
