#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/27
@File : test_userRemove.py
@describe : 该模块用于测试鉴权2.0 bim融合-企业用户管理-用户删除接口

"""
import time
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil


class UserRemove(unittest.TestCase):
    def setUp(self):
        api_url = "coding/service/admin/user/remove"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        # 插入多个用户用于测试删除
        self.test_user_id_list, self.test_login_name_list = ChildUserSqlUtil.insert_users(4, '0')

    def test_user_remove_01(self):
        u'批量删除存在的用户，请求成功'
        data = {
            "list": self.test_login_name_list
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户删除接口入参：=================>\n', data)
        print('用户删除接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 断言响应数据
        expect_data = '1'
        for user_id in self.test_user_id_list:
            self.mysql.cursor.execute("select is_deleted from ep_users where id=%s" % user_id)
            actual_data = self.mysql.cursor.fetchall()[0][0]
            self.assertEqual(expect_data, actual_data)

    def test_user_remove_02(self):
        u'无法根据登录名找到用户，请求失败'
        print('用户删除api_url：=================>', self.url)
        data = {
            "list": ["notFoundUser"]
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户删除接口入参：=================>\n', data)
        print('用户删除接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "无法根据登陆名找到用户"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_remove_03(self):
        u'部分用户不存在，存在的用户删除成功，返回部分用户操作失败'
        print('用户删除api_url：=================>', self.url)
        data = {
            "list": [self.test_login_name_list[0], "notFoundUser"]
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户删除接口入参：=================>\n', data)
        print('用户删除接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "部分用户操作失败"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 断言响应数据
        expect_data = '1'
        self.mysql.cursor.execute("select is_deleted from ep_users where id=%s" % self.test_user_id_list[0])
        actual_data = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_data, actual_data)

    def test_user_remove_04(self):
        u'用户名数组为空，请求失败'
        #Todo 验证bugID1000701
        print('用户删除api_url：=================>', self.url)
        data = {
            "list": []
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户删除接口入参：=================>\n', data)
        print('用户删除接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "数组不能为空"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def tearDown(self):
        u'清除测试数据'
        ChildUserSqlUtil.delete_datas_by_id('ep_users', self.test_user_id_list)
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
