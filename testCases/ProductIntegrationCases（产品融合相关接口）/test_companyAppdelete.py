# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/27
@File : test_companyAppdelete.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil
import unittest


class CompanyAppDelete(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/v3/companyApp/delete'
        self.url = conf_url() + self.api_url
        self.company_app_id_list, self.appId_list = ChildUserSqlUtil.insert_app(1)
        self.mysql = MySqlUtil()

    def test_companyapp_delete_01(self):
        u"企业应用存在，删除企业应用，请求成功"
        #Todo 验证bugID1000702
        url = self.url
        data = {
            "appId": self.company_app_id_list[0]
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        expect_data = ()
        self.mysql.cursor.execute("select * from ep_company_app where id=%s" % self.company_app_id_list[0])
        actual_data = self.mysql.cursor.fetchall()
        self.assertEqual(expect_data, actual_data)

    def test_companyapp_delete_02(self):
        u"应用id为空，请求失败"
        url = self.url
        data = {
            "appId": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "应用id不能为空;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_companyapp_delete_03(self):
        u"应用id不存在，请求失败"
        url = self.url
        data = {
            "appId": "12138"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "企业应用ID不存在"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def tearDown(self):
        #检查测试数据是否已通过接口删除，若接口删除失败则通过sql清除测试数据
        self.mysql.cursor.execute("select * from ep_company_app where id=%s" % self.company_app_id_list[0])
        test_data = self.mysql.cursor.fetchall()
        if test_data !=():
            self.mysql.sql_delete("delete from ep_company_app where id=%s" % self.company_app_id_list[0])
        else:
            print("测试数据已被删除")
        self.mysql.db_sql.close()

if __name__ == "__main__":
    unittest.main()
