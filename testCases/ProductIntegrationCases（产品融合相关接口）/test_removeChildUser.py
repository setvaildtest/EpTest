#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/27
@File : test_removeChildUser.py
@describe : 该模块用于测试鉴权2.0 bim融合-企业用户管理-删除子账号接口（根据登录用户、授权应用id、子账号id删除子账号，可批量）


"""
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.ConfigServer import conf_appid
from ep_common.ConfigPerson import ConfigPerson
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil


class RemoveChildUser(unittest.TestCase):
    def setUp(self):
        api_url = "coding/outUserAndApp/removeChildUser"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        self.appId = conf_appid()  # 获取测试应用appId
        self.login_name = ConfigPerson().conf_loginName()  # 获取测试用户login_name
        # 获取测试用户id：使用配置文件配置的数据
        self.mysql.cursor.execute("select id from ep_users where login_name='%s'" % self.login_name)
        self.user_id = self.mysql.cursor.fetchall()[0][0]
        # 获取测试应用id：使用配置文件配置的数据
        self.mysql.cursor.execute("select id from ep_company_app where app_id='%s'" % self.appId)
        self.company_app_id = self.mysql.cursor.fetchall()[0][0]
        # 添加应用授权
        self.auth_id = ChildUserSqlUtil.insert_auth(self.user_id, self.company_app_id)
        # 添加子账号
        self.child_id_list, self.child_name_list = ChildUserSqlUtil.insert_child_users(4, self.user_id,
                                                                                       self.company_app_id)

    def test_remove_child_user_01(self):
        u'批量删除已授权应用的子账号，请求成功'
        data = {
            "appId": self.appId,
            "childNameList": self.child_name_list,
            "loginName": self.login_name
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('删除子账号接口入参：=================>\n', data)
        print('删除子账号接口响应：=================>\n', re)
        # 断言响应状态
        expect_message = '操作成功'
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 断言响应数据
        expect_data = ()
        for child_id in self.child_id_list:
            self.mysql.cursor.execute("select * from ep_child_user where id=%s" % child_id)
            actual_data = self.mysql.cursor.fetchall()
            self.assertEqual(expect_data, actual_data)

    def test_remove_child_user_02(self):
        u'用户账户登录名为空，请求失败'
        data = {
            "appId": self.appId,
            "childNameList": self.child_name_list,
            "loginName": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('删除子账号接口入参：=================>\n', data)
        print('删除子账号接口响应：=================>\n', re)
        # 断言响应状态
        expect_message = '用户账户登录名不能为空;'
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_remove_child_user_03(self):
        u'应用appId为空，请求失败'
        data = {
            "appId": "",
            "childNameList": self.child_name_list,
            "loginName": self.login_name
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('删除子账号接口入参：=================>\n', data)
        print('删除子账号接口响应：=================>\n', re)
        # 断言响应状态
        expect_message = '应用id不能为空;'
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_remove_child_user_04(self):
        u'子账号为空，请求失败'
        data = {
            "appId": self.appId,
            "childNameList": [],
            "loginName": self.login_name
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('删除子账号接口入参：=================>\n', data)
        print('删除子账号接口响应：=================>\n', re)
        # 断言响应状态
        expect_message = '子账号集合不能为空;'
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_remove_child_user_05(self):
        u'appId不存在，请求失败'
        data = {
            "appId": "notfoundapp",
            "childNameList": self.child_name_list,
            "loginName": self.login_name
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('删除子账号接口入参：=================>\n', data)
        print('删除子账号接口响应：=================>\n', re)
        # 断言响应message
        expect_message = '企业应用ID不存在'
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_remove_child_user_06(self):
        u'用户不存在，请求失败'
        data = {
            "appId": self.appId,
            "childNameList": self.child_name_list,
            "loginName": "notfounduser"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('删除子账号接口入参：=================>\n', data)
        print('删除子账号接口响应：=================>\n', re)
        # 断言响应
        expect_status = 'fail'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status)

    def test_remove_child_user_07(self):
        u'子账号不存在，请求失败'
        data = {
            "appId": self.appId,
            "childNameList": ["notfoundchilduser"],
            "loginName": self.login_name
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('删除子账号接口入参：=================>\n', data)
        print('删除子账号接口响应：=================>\n', re)
        # 断言响应
        expect_status = 'fail'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status)

    def test_remove_child_user_08(self):
        u'用户没有应用的权限，请求失败'

        data = {
            "appId": "elogin",
            "childNameList": self.child_name_list,
            "loginName": self.login_name
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('删除子账号接口入参：=================>\n', data)
        print('删除子账号接口响应：=================>\n', re)
        # 断言响应
        expect_status = 'fail'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status)

    def test_remove_child_user_09(self):
        u'子账号和应用不匹配，请求失败'

        data = {
            "appId": "elogin",
            "childNameList": self.child_name_list,
            "loginName": self.login_name
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('删除子账号接口入参：=================>\n', data)
        print('删除子账号接口响应：=================>\n', re)
        # 断言响应
        expect_status = 'fail'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status)

    def tearDown(self):
        '''清除测试数据'''
        # 删除应用授权
        self.mysql.sql_delete("delete from ep_user_company_app where id='%s'" % self.auth_id)
        # 删除子账号：避免接口删除子账号失败的情况
        ChildUserSqlUtil.delete_datas_by_id('ep_child_user', self.child_id_list)
        self.mysql.db_sql.close()

if __name__ == "__main__":
    unittest.main()
