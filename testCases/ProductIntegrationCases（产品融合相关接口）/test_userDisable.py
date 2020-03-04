#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/27
@File : test_userDisable.py
@describe : 该模块用于测试鉴权2.0 bim融合-企业用户管理-用户启用接口

"""
import time
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil

class UserDisable(unittest.TestCase):
    def setUp(self):
        api_url = "coding/service/admin/user/disable"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        #通过sql创建用户用于测试用户禁用
        self.test_user_id_list1, self.test_login_name_list1 = ChildUserSqlUtil.insert_users(4, '0')
        self.test_user_id_list2, self.test_login_name_list2 = ChildUserSqlUtil.insert_users(4, '1')

    def test_user_disable_01(self):
        u'批量禁用用户，请求成功'
        print('用户禁用api_url：=================>', self.url)
        data = {
            "list": self.test_login_name_list1
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户禁用接口入参：=================>\n', data)
        print('用户禁用接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 断言响应数据
        expect_data = '1'
        for user_id in self.test_user_id_list1:
            self.mysql.cursor.execute("select is_disabled from ep_users where id=%s" % user_id)
            actual_data = self.mysql.cursor.fetchall()[0][0]
            self.assertEqual(expect_data, actual_data)

    def test_user_disable_02(self):
        u'禁用禁用状态的用户，请求成功'
        print('用户禁用api_url：=================>', self.url)
        data = {
            "list": self.test_login_name_list2
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户禁用接口入参：=================>\n', data)
        print('用户禁用接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 断言响应数据
        expect_data = '1'
        for user_id in self.test_user_id_list2:
            self.mysql.cursor.execute("select is_disabled from ep_users where id=%s" % user_id)
            actual_data = self.mysql.cursor.fetchall()[0][0]
            self.assertEqual(expect_data, actual_data)

    def test_user_disable_03(self):
        u'数组为空，请求失败'
        print('用户禁用api_url：=================>', self.url)
        data = {
            "list":[]
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户禁用接口入参：=================>\n', data)
        print('用户禁用接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "数组不能为空"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_disable_04(self):
        u'用户不存在，请求失败'
        print('用户禁用api_url：=================>', self.url)
        data = {
            "list":["notfounduser"]
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户禁用接口入参：=================>\n', data)
        print('用户禁用接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "部分用户操作失败"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def tearDown(self):
        u'清除测试数据'
        ChildUserSqlUtil.delete_datas_by_id('ep_users',self.test_user_id_list1)
        ChildUserSqlUtil.delete_datas_by_id('ep_users', self.test_user_id_list2)
        self.mysql.db_sql.close()

if __name__ == "__main__":
    unittest.main()
