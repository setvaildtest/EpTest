#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/26
@File : test_userList.py
@describe : 该模块用于测试鉴权2.0 bim融合-企业用户管理-用户查询接口

"""
import time
import unittest

from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil


class UserList(unittest.TestCase):
    def setUp(self):
        api_url = "coding/service/admin/user/list"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        self.test_user_id_list, self.test_login_name_list = ChildUserSqlUtil.insert_users(11, '0')

    def test_user_list_01(self):
        u'按关键字查询第1个分页启用状态的10个用户，请求成功'
        condition = "a"
        isDisabled = "0"
        limit = 10
        page = 1
        data = {
            "condition": condition,
            "isDisabled": isDisabled,
            "limit": limit,
            "page": page
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data=data)
        print('用户查询接口入参：=================>\n', data)
        print('用户查询接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 响应数据断言
        startRow = (page - 1) * limit
        self.mysql.cursor.execute(
            "select login_name from ep_users where is_disabled='" + isDisabled + "' and is_deleted='0' and CONCAT(login_name,name,phone,email,department) like '%" + condition + "%'order by id desc limit " + str(
                startRow) + "," + str(
                limit))
        print("select login_name from ep_users where is_disabled='" + isDisabled + "' and is_deleted='0' and CONCAT(login_name,name,phone,email,department) like '%" + condition + "%' order by id desc limit " + str(
                startRow) + "," + str(
                limit))
        expect_data = []
        for e in self.mysql.cursor.fetchall():
            expect_data.append(e[0])
        print(expect_data)

        actual_data = []
        for a in re['body']['data']:
            actual_data.append(a['loginName'])
        print(actual_data)
        self.assertEqual(expect_data, actual_data)  # 对比接口响应结果和数据库查询结果

    def test_user_list_02(self):
        u'查询第1个分页的20个用户,请求成功'
        condition = ""
        isDisabled = None
        limit = 20
        page = 1
        data = {
            "condition": condition,
            "isDisabled": isDisabled,
            "limit": limit,
            "page": page
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data=data)
        print('用户查询接口入参：=================>\n', data)
        print('用户查询接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 响应数据断言
        startRow = (page - 1) * limit
        self.mysql.cursor.execute(
            "select login_name from ep_users where is_deleted='0' order by id desc limit %s,%s" % (startRow, limit))
        expect_data = []
        for e in self.mysql.cursor.fetchall():
            expect_data.append(e[0])
        print(expect_data)
        actual_data = []
        for a in re['body']['data']:
            actual_data.append(a['loginName'])
        print(actual_data)
        self.assertEqual(expect_data, actual_data)  # 对比接口响应结果和数据库查询结果

    def test_user_list_03(self):
        u'查询第2个分页的10个用户,请求成功'
        condition = ""
        isDisabled = None
        limit = 10
        page = 2
        data = {
            "condition": condition,
            "isDisabled": isDisabled,
            "limit": limit,
            "page": page
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data=data)
        print('用户查询接口入参：=================>\n', data)
        print('用户查询接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 响应数据断言
        startRow = (page - 1) * limit
        self.mysql.cursor.execute(
            "select login_name from ep_users where is_deleted='0' order by id desc limit %s,%s" % (startRow, limit))
        expect_data = []
        for e in self.mysql.cursor.fetchall():
            expect_data.append(e[0])
        print(expect_data)
        actual_data = []
        for a in re['body']['data']:
            actual_data.append(a['loginName'])
        print(actual_data)
        self.assertEqual(expect_data, actual_data)  # 对比接口响应结果和数据库查询结果

    def test_user_list_04(self):
        u'查询条件为空，请求成功'
        condition = ""
        isDisabled = "0"
        limit = 10
        page = 1
        data = {
            "condition": condition,
            "isDisabled": isDisabled,
            "limit": limit,
            "page": page
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data=data)
        print('用户查询接口入参：=================>\n', data)
        print('用户查询接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 响应数据断言
        startRow = (page - 1) * limit
        self.mysql.cursor.execute(
            "select login_name from ep_users where is_disabled='%s' and is_deleted='0' order by id desc limit %s,%s" % (
                isDisabled, startRow, limit))
        expect_data = []
        for e in self.mysql.cursor.fetchall():
            expect_data.append(e[0])
        print(expect_data)
        actual_data = []
        for a in re['body']['data']:
            actual_data.append(a['loginName'])
        print(actual_data)
        self.assertEqual(expect_data, actual_data)  # 对比接口响应结果和数据库查询结果

    def test_user_list_05(self):
        u'查询启用状态的用户,请求成功'
        condition = ""
        isDisabled = "0"
        limit = 10
        page = 1
        data = {
            "condition": condition,
            "isDisabled": isDisabled,
            "limit": limit,
            "page": page
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data=data)
        print('用户查询接口入参：=================>\n', data)
        print('用户查询接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 响应数据断言
        startRow = (page - 1) * limit
        self.mysql.cursor.execute(
            "select login_name from ep_users where is_disabled='%s' and is_deleted='0' order by id desc limit %s,%s" % (
                isDisabled, startRow, limit))
        expect_data = []
        for e in self.mysql.cursor.fetchall():
            expect_data.append(e[0])
        print(expect_data)
        actual_data = []
        for a in re['body']['data']:
            actual_data.append(a['loginName'])
        print(actual_data)
        self.assertEqual(expect_data, actual_data)  # 对比接口响应结果和数据库查询结果

    def test_user_list_06(self):
        u'查询禁用状态的用户,请求成功'
        condition = ""
        isDisabled = "1"
        limit = 10
        page = 1
        data = {
            "condition": condition,
            "isDisabled": isDisabled,
            "limit": limit,
            "page": page
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data=data)
        print('用户查询接口入参：=================>\n', data)
        print('用户查询接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 响应数据断言
        startRow = (page - 1) * limit
        self.mysql.cursor.execute(
            "select login_name from ep_users where is_disabled='%s' and is_deleted='0' order by id desc limit %s,%s" % (
                isDisabled, startRow, limit))
        expect_data = []
        for e in self.mysql.cursor.fetchall():
            expect_data.append(e[0])
        print(expect_data)
        actual_data = []
        for a in re['body']['data']:
            actual_data.append(a['loginName'])
        print(actual_data)
        self.assertEqual(expect_data, actual_data)  # 对比接口响应结果和数据库查询结果

    def test_user_list_07(self):
        u'用户状态不存在,请求失败'
        condition = ""
        isDisabled = "3"
        limit = 10
        page = 1
        data = {
            "condition": condition,
            "isDisabled": isDisabled,
            "limit": limit,
            "page": page
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data=data)
        print('用户查询接口入参：=================>\n', data)
        print('用户查询接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "参数错误;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_list_08(self):
        u'用户状态为空,请求失败'
        condition = ""
        isDisabled = ""
        limit = 10
        page = 1
        data = {
            "condition": condition,
            "isDisabled": isDisabled,
            "limit": limit,
            "page": page
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data=data)
        print('用户查询接口入参：=================>\n', data)
        print('用户查询接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "参数错误;参数错误;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def tearDown(self):
        ''''清除测试数据'''
        ChildUserSqlUtil.delete_datas_by_id('ep_users', self.test_user_id_list)
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
