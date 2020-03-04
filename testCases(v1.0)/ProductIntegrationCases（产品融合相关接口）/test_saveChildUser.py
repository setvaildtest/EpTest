#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/27
@File : test_saveChildUser.py
@describe : 该模块用于测试鉴权1.0 bim融合-企业用户管理-新建应用子账号接口（新增用户在一个应用下的子账号）

"""
import time
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.ConfigServer import conf_appid
from ep_common.ConfigPerson import ConfigPerson
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil
from ep_common.GenerateRandomStr import generate_random_str


class SaveChildUser(unittest.TestCase):
    def setUp(self):
        api_url = "coding/outUserAndApp/saveChildUser"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        self.appId = conf_appid()
        self.login_name = ConfigPerson().conf_loginName()
        # 获取测试用户id：使用配置文件配置的数据
        self.mysql.cursor.execute("select id from ep_users where login_name='%s'" % self.login_name)
        self.user_id = self.mysql.cursor.fetchall()[0][0]
        # 获取测试应用id(使用配置文件配置的数据), 添加应用授权
        self.mysql.cursor.execute("select id from ep_company_app where app_id='%s'" % self.appId)
        self.company_app_id = self.mysql.cursor.fetchall()[0][0]
        self.auth_id = ChildUserSqlUtil.insert_auth(self.user_id, self.company_app_id)


    def test_save_child_user_01(self):
        u'新增子账号（appId和loginName存在且用户已有该应用的权限）,请求成功'
        data = {
            "appId": self.appId,
            "description": "新建子账号接口测试用例1",
            "loginName": self.login_name,
            "name": "child1_apiTest"
        }
        new_child_user=data['name']
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('新建应用子账号接口入参：=================>\n', data)
        print('新建应用子账号接口响应：=================>\n', re)
        # 断言响应消息
        expect_message="操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 断言响应数据
        expect_data = new_child_user
        actual_data = ChildUserSqlUtil.find_child_user(self.user_id, self.company_app_id)
        print(actual_data)
        self.assertIn(expect_data, actual_data)

    def test_save_child_user_02(self):
        u'子账号名称长度超过45，请求失败'
        data = {
            "appId": self.appId,
            "description": "新建子账号测试用例2",
            "loginName": self.login_name,
            "name": generate_random_str(46)
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('新建应用子账号接口入参：=================>\n', data)
        print('新建应用子账号接口响应：=================>\n', re)
        # 断言响应消息
        expect_message="子账号名称长度不超过45;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_child_user_03(self):
        u'子账号描述长度超过300，请求失败'
        data = {
            "appId": self.appId,
            "description": generate_random_str(301),
            "loginName": self.login_name,
            "name": "child3_apiTest"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('新建应用子账号接口入参：=================>\n', data)
        print('新建应用子账号接口响应：=================>\n', re)
        # 断言响应消息
        expect_message="子账号描述长度不超过300;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_child_user_04(self):
        u'应用appId为空，请求失败'
        data = {
            "appId": "",
            "description": "",
            "loginName": self.login_name,
            "name": "child4_apiTest"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('新建应用子账号接口入参：=================>\n', data)
        print('新建应用子账号接口响应：=================>\n', re)
        # 断言响应消息
        expect_message="应用id不能为空;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_child_user_05(self):
        u'主账号loginName为空，请求失败'
        data = {
            "appId": self.appId,
            "description": "",
            "loginName": "",
            "name": "child5_apiTest"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('新建应用子账号接口入参：=================>\n', data)
        print('新建应用子账号接口响应：=================>\n', re)
        # 断言响应消息
        expect_message="参数错误;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_child_user_06(self):
        u'子账号name为空，请求失败'
        data = {
            "appId": self.appId,
            "description": "",
            "loginName": self.login_name,
            "name": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('新建应用子账号接口入参：=================>\n', data)
        print('新建应用子账号接口响应：=================>\n', re)
        # 断言响应消息
        expect_message="参数错误;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_child_user_07(self):
        u'主账号不存在，请求失败'
        data = {
            "appId": self.appId,
            "description": "",
            "loginName": "notfounduser",
            "name": "child7_apiTest"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('新建应用子账号接口入参：=================>\n', data)
        print('新建应用子账号接口响应：=================>\n', re)
        # 断言响应消息
        expect_message="主账号不存在"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_child_user_08(self):
        u'用户不具有此应用的权限，请求失败'
        data = {
            "appId": "elogin",
            "description": "",
            "loginName": self.login_name,
            "name": "child8_apiTest"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('新建应用子账号接口入参：=================>\n', data)
        print('新建应用子账号接口响应：=================>\n', re)
        # 断言响应消息
        expect_message="用户不具有此应用的权限"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_child_user_09(self):
        u'子账号已存在，请求失败'
        # 添加子账号
        child_id_list, child_name_list = ChildUserSqlUtil.insert_child_users(1, self.user_id,
                                                                                       self.company_app_id)
        data = {
            "appId": self.appId,
            "description": "",
            "loginName": self.login_name,
            "name": child_name_list[0]
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('新建应用子账号接口入参：=================>\n', data)
        print('新建应用子账号接口响应：=================>\n', re)
        # 断言响应消息
        expect_message="子账号已存在"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def tearDown(self):
        # 删除应用授权
        self.mysql.sql_delete("delete from ep_user_company_app where id='%s'" % self.auth_id)
        # 删除子账号
        self.mysql.sql_delete(
            "delete from ep_child_user where user_id='%s' and company_app_id=%s" % (
                self.user_id, self.company_app_id))
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
