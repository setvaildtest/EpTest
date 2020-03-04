# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/27
@File : test_companyAppadd.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil
from ep_common.GenerateRandomStr import generate_random_str
from ep_common.ConfigServer import conf_appid
import unittest


class CompanyAppAdd(unittest.TestCase):

    def setUp(self):

        self.api_url = 'coding/v3/companyApp/add'
        self.url = conf_url() + self.api_url
        self.mysql = MySqlUtil()

    def test_companyapp_add_01(self):
        u"应用id、安全级别id和应用类型正确且不重复，添加应用，请求成功"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp1",
            "description": "应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App1",
            "securityLevelId": "1",
            "sortName": "接口新增App1",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:",re)
        expect_message="操作成功"
        actual_message = re['message']
        self.assertIn(expect_message,actual_message)

    def test_companyapp_add_02(self):
        u"应用名称为空，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp2",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "",
            "securityLevelId": "1",
            "sortName": "接口新增App2",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:",re)
        expect_message="企业应用名称不能为空或空串"
        actual_message = re['message']
        self.assertIn(expect_message,actual_message)

    def test_companyapp_add_03(self):
        u"应用名称为空串，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp3",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "     ",
            "securityLevelId": "1",
            "sortName": "接口新增App3",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "企业应用名称不能为空或空串"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_companyapp_add_04(self):
        u"企业简称为空，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp4",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App4",
            "securityLevelId": "1",
            "sortName": "",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:",re)
        expect_message="企业应用简称不能为空"
        actual_message = re['message']
        self.assertIn(expect_message,actual_message)

    def test_companyapp_add_05(self):
        u"企业简称为空串，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp5",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App5",
            "securityLevelId": "1",
            "sortName": "    ",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:",re)
        expect_message="企业应用简称不能为空"
        actual_message = re['message']
        self.assertIn(expect_message,actual_message)

    def test_companyapp_add_06(self):
        u"appId为空，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App6",
            "securityLevelId": "1",
            "sortName": "接口新增App6",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:",re)
        expect_message="应用id不能为空"
        actual_message = re['message']
        self.assertIn(expect_message,actual_message)

    def test_companyapp_add_07(self):
        u"appId为空串，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "  ",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App7",
            "securityLevelId": "1",
            "sortName": "接口新增App7",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:",re)
        expect_message="参数错误:应用id不能为空;"
        actual_message = re['message']
        self.assertIn(expect_message,actual_message)

    def test_companyapp_add_08(self):
        u"应用安全级别不存在，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp8",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App8",
            "securityLevelId": "99",
            "sortName": "接口新增App8",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:",re)
        expect_message="应用安全级别不存在"
        actual_message = re['message']
        self.assertIn(expect_message,actual_message)

    def test_companyapp_add_09(self):
        u"应用类型不存在，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp9",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App9",
            "securityLevelId": "1",
            "sortName": "接口新增App9",
            "ssoAddress": "com.apiTestApp.android",
            "type": "9"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:",re)
        expect_message="参数错误:0:app应用,1:web应用,2:H5应用,3:PC应用;"
        actual_message = re['message']
        self.assertIn(expect_message,actual_message)

    def test_companyapp_add_10(self):
        u"企业应用名称已存在，请求失败"
        #查询已存在的应用名称
        self.mysql.cursor.execute("select name from ep_company_app where type='0' ORDER BY id DESC LIMIT 1")
        try:
            exist_name=self.mysql.cursor.fetchone()[0]
        except(Exception)as e:
            print(e)
            # 通过sql创建一个应用用于重复校验
            app_id_list, appId_list = ChildUserSqlUtil.insert_app(1)
            exist_name=appId_list[0]
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp10",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": exist_name,
            "securityLevelId": "1",
            "sortName": "接口新增App10",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "企业应用名称重复"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_companyapp_add_11(self):
        u"企业应用简称已存在，请求失败"
        # 查询已存在的应用简称
        self.mysql.cursor.execute("select sort_name from ep_company_app where type='0' ORDER BY id DESC LIMIT 1")
        try:
            exist_sort_name = self.mysql.cursor.fetchone()[0]
        except(Exception)as e:
            print(e)
            # 通过sql创建一个应用用于重复校验
            app_id_list, appId_list = ChildUserSqlUtil.insert_app(1)
            exist_sort_name = appId_list[0]
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp11",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App11",
            "securityLevelId": "1",
            "sortName": exist_sort_name,
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "企业应用简称重复"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_companyapp_add_12(self):
        u"企业应用appId已存在，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": conf_appid(),
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App12",
            "securityLevelId": "1",
            "sortName":"接口新增App12" ,
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "应用id不能重复"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_companyapp_add_13(self):
        u"企业应用名称长度超过30，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp13",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": generate_random_str(31),
            "securityLevelId": "1",
            "sortName": "接口新增App13",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "企业应用名称长度不能超过30"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_companyapp_add_14(self):
        u"企业应用简称长度超过30，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "apiTestApp14",
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App14",
            "securityLevelId": "1",
            "sortName": generate_random_str(31),
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "企业应用简称长度不能超过30"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def test_companyapp_add_15(self):
        u"企业应用appId长度超过45，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": generate_random_str(46),
            "description": "企业应用新增接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口新增App15",
            "securityLevelId": "1",
            "sortName": "接口新增App15",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print("response:", re)
        expect_message = "企业应用ID字符长度不能超过45"
        actual_message = re['message']
        self.assertIn(expect_message, actual_message)

    def tearDown(self):
        #清除接口和sql创建的测试数据
        self.mysql.sql_delete("delete from ep_company_app where app_id like'%apiTestApp%' or description='企业应用新增接口测试'")
        self.mysql.db_sql.close()

if __name__ == "__main__":
    unittest.main()

