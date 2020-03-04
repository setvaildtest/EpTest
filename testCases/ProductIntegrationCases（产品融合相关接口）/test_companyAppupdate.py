# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/27
@File : test_companyAppupdate.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil
from ep_common.GenerateRandomStr import generate_random_str
import unittest


class CompanyAppUpdate(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/v3/companyApp/update'
        self.url = conf_url() + self.api_url
        self.company_app_id_list, self.appId_list = ChildUserSqlUtil.insert_app(2)
        self.mysql = MySqlUtil()

    def test_companyapp_update_01(self):
        u"应用id、安全级别id和应用类型正确且不重复，修改企业应用请求成功"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口修改App1",
            "securityLevelId": "2",
            "sortName": "接口修改App1",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("操作成功", result)

    def test_companyapp_update_02(self):
        u"appId为空，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "",
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口修改App2",
            "securityLevelId": "2",
            "sortName": "接口修改App2",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("参数错误:应用id不能为空;", result)

    def test_companyapp_update_03(self):
        u"appId不存在，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": "notfoundapp",
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口修改App3",
            "securityLevelId": "2",
            "sortName": "接口修改App3",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertIn("企业应用ID不存在", result)

    def test_companyapp_update_04(self):
        u"应用名称为空，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "",
            "securityLevelId": "2",
            "sortName": "接口修改App4",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("参数错误:企业应用名称不能为空或空串;", result)

    def test_companyapp_update_05(self):
        u"应用名称为空串，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "    ",
            "securityLevelId": "2",
            "sortName": "接口修改App5",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("参数错误:企业应用名称不能为空或空串;", result)

    def test_companyapp_update_06(self):
        u"应用简称为空，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口修改App6",
            "securityLevelId": "2",
            "sortName": "",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("参数错误:企业应用简称不能为空;", result)

    def test_companyapp_update_07(self):
        u"应用简称为空串，请求失败"
        # todo 验证bug ID1000663
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口修改App7",
            "securityLevelId": "2",
            "sortName": "             ",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("参数错误:企业应用简称不能为空;", result)

    def test_companyapp_update_08(self):
        u"企业应用名称长度超过30，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": generate_random_str(31),
            "securityLevelId": "2",
            "sortName": "接口修改App8",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("参数错误:企业应用名称长度不能超过30;", result)

    def test_companyapp_update_09(self):
        u"企业应用简称长度超过30，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口修改App9",
            "securityLevelId": "2",
            "sortName": generate_random_str(31),
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("参数错误:企业应用简称长度不能超过30;", result)

    def test_companyapp_update_10(self):
        u"企业应用名称已存在，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": self.appId_list[1],
            "securityLevelId": "2",
            "sortName": "接口修改App10",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("企业应用名称重复", result)

    def test_companyapp_update_11(self):
        u"企业应用简称已存在，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口修改App11",
            "securityLevelId": "2",
            "sortName": self.appId_list[1],
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("企业应用简称重复", result)

    def test_companyapp_update_12(self):
        u"应用安全级别不存在，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口修改App12",
            "securityLevelId": "999",
            "sortName": "接口修改App12",
            "ssoAddress": "com.apiTestApp.android",
            "type": "0"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertEqual("应用安全级别不存在", result)

    def test_companyapp_update_13(self):
        u"应用类型不存在，请求失败"
        url = self.url
        data = {
            "androidPackageName": "com.apiTestApp.android",
            "appIcon": "",
            "appId": self.appId_list[0],
            "description": "企业应用修改接口测试",
            "downdloadAddr": "",
            "downloadType": "",
            "isRelay": "0",
            "name": "接口修改App13",
            "securityLevelId": "9",
            "sortName": "接口修改App13",
            "ssoAddress": "com.apiTestApp.android",
            "type": "10"
        }

        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('response：', re)
        result = re['message']
        self.assertIn("参数错误:0:app应用,1:web应用,2:H5应用,3:PC应用;", result)

    def tearDown(self):
        ChildUserSqlUtil.delete_datas_by_id("ep_company_app", self.company_app_id_list)
        self.mysql.db_sql.close()

if __name__ == "__main__":
    unittest.main()

