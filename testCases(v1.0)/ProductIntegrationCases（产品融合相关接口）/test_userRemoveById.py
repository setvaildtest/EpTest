#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/9/23
@File : test_userRemoveById.py
@describe : 鉴权1.0 BIM融合 - 企业用户管理 - 根据物理ID删除用户

"""
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil


class UserRemoveById(unittest.TestCase):
    def setUp(self):
        api_url = "coding/userInfo/removeById"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        # 通过sql创建用户用于测试用户删除
        self.test_user_id_list, self.test_login_name_list = ChildUserSqlUtil.insert_users(4, '0')

    def test_user_remove_by_id_01(self):
        u'批量删除用户，请求成功'
        data = self.test_user_id_list
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

    def test_user_remove_by_id_02(self):
        u'无法根据ID找到用户，请求成功'
        data = [12138]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户删除接口入参：=================>\n', data)
        print('用户删除接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "无法根据ID找到用户"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_user_remove_by_id_03(self):
        u'idList为空，请求成功'
        #todo 验证bug ID1000688
        data = []
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户删除接口入参：=================>\n', data)
        print('用户删除接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "idList不能为空"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_user_remove_by_id_04(self):
        u'部分用户不存在，请求成功'
        #TODO 验证bug ID1000687
        data = [self.test_user_id_list[0], 12138]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户删除接口入参：=================>\n', data)
        print('用户删除接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "部分用户操作失败"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)
        # 断言数据
        expect_data = '1'
        self.mysql.cursor.execute("select is_deleted from ep_users where id=%s" % self.test_user_id_list[0])
        actual_data = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_data, actual_data)

    def tearDown(self):
        u'清除测试数据'
        ChildUserSqlUtil.delete_datas_by_id('ep_users', self.test_user_id_list)
        self.mysql.db_sql.close()
