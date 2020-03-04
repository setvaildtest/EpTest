# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/27
@File : test_authUserApp.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil
from ep_common.ConfigPerson import ConfigPerson
from ep_common.ConfigServer import conf_appid
import unittest
import time


class AuthUserApp(unittest.TestCase):

    def setUp(self):
        api_url = 'coding/outUserAndApp/authUserApp'
        self.url = conf_url() + api_url
        self.appId = conf_appid()
        person = ConfigPerson()
        self.loginName = person.conf_loginName()
        self.mysql = MySqlUtil()
        self.mysql.cursor.execute("select id from ep_users where login_name='%s'" % self.loginName)
        self.user_id = self.mysql.cursor.fetchone()[0]
        self.mysql.cursor.execute("select id from ep_company_app where app_id='%s'" % self.appId)
        self.app_id = self.mysql.cursor.fetchone()[0]

    def test_auth_user_app_01(self):
        u"authSign参数为true，给用户授予某个应用的权限，请求成功"
        url = self.url
        data = {
            "appIdList": [self.appId],
            "authSign": "true",
            "userList": [
                {
                    "companyId": 1,
                    "loginName": self.loginName
                }
            ]
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response', re)
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_auth_user_app_02(self):
        u"authSign参数为false，取消用户对某个应用的权限，请求成功"
        url = self.url
        data = {
            "appIdList": [self.appId],
            "authSign": "false",
            "userList": [
                {
                    "companyId": 1,
                    "loginName": self.loginName
                }
            ]
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response', re)
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_auth_user_app_03(self):
        u"不传appIdList，请求失败"
        url = self.url
        data = {
            "authSign": "true",
            "userList": [
                {
                    "companyId": 1,
                    "loginName": self.loginName
                }
            ]
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response', re)
        expect_message = "应用ID集合不能空;"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_auth_user_app_04(self):
        u"不传userList，请求失败"
        url = self.url
        data = {
            "appIdList": [self.appId],
            "authSign": "true"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response', re)
        expect_message = "被授权人员集合不能为空;"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_auth_user_app_05(self):
        u"appId为空，请求失败"
        url = self.url
        data = {
            "appIdList": [],
            "authSign": "false",
            "userList": [
                {
                    "companyId": 1,
                    "loginName": self.loginName
                }
            ]
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response', re)
        expect_message = "应用ID集合不能空;"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_auth_user_app_06(self):
        u"appId不存在，请求失败"
        url = self.url
        data = {
            "appIdList": ["rwqyriu"],
            "authSign": "true",
            "userList": [
                {
                    "companyId": 1,
                    "loginName": self.loginName
                }
            ]
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response', re)
        expect_message = "企业应用ID不存在"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_auth_user_app_07(self):
        u"批量授权：将多个应用授权给多个用户，请求成功"
        # 通过sql批量创建测试用户和测试应用
        user_id_list, login_name_list = ChildUserSqlUtil.insert_users(2, '0')
        company_app_id_list, appId_list = ChildUserSqlUtil.insert_app(2)
        url = self.url
        data = {
            "appIdList": appId_list,
            "authSign": "true",
            "userList": [
                {
                    "companyId": 1,
                    "loginName": login_name_list[0]
                },
                {
                    "companyId": 1,
                    "loginName": login_name_list[1]
                }
            ]
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response', re)
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_auth_user_app_08(self):
        u"批量取消授权：取消多个应用对多个用户的权限，请求成功"
        # 批量创建测试用户和测试应用
        user_id_list, login_name_list = ChildUserSqlUtil.insert_users(2, '0')
        company_app_id_list, appId_list = ChildUserSqlUtil.insert_app(2)
        # 给批量用户批量授权
        for u in user_id_list:
            for a in company_app_id_list:
                ChildUserSqlUtil.insert_auth(u, a)
        # 请求取消授权接口
        url = self.url
        data = {
            "appIdList": appId_list,
            "authSign": "false",
            "userList": [
                {
                    "companyId": 1,
                    "loginName": login_name_list[0]
                },
                {
                    "companyId": 1,
                    "loginName": login_name_list[1]
                }
            ]
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response', re)
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_auth_user_app_09(self):
        u"authSign参数为非true和false之外的值，给用户授予某个应用的权限，请求成功"
        url = self.url
        data = {
            "appIdList": [self.appId],
            "authSign": "aaa",
            "userList": [
                {
                    "companyId": 1,
                    "loginName": self.loginName
                }
            ]
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response', re)
        expect_message = "参数类型转换失败"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def tearDown(self):
        # 清除授权数据
        self.mysql.sql_delete(
                      "delete  from ep_user_company_app where user_id='%s' and company_app_id='%s'" % (self.user_id, self.app_id))
        # 删除sql创建的用户和应用
        self.mysql.sql_delete("delete  from ep_users where login_name like '%apiTestUser_sql%'")
        self.mysql.sql_delete("delete  from ep_company_app where app_id like '%apiTestApp_sql%'")
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
