# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_getEncryptedStringByApp.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

from ep_common.JwtGet import get_jwt
import unittest
import time
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson
from ep_common.ConfigServer import conf_url
from ep_common.ConfigServer import conf_appid
from ep_common.child_user_sql import ChildUserSqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP


class GetEncryptedStringByApp(unittest.TestCase):

    def setUp(self) -> None:
        self.mysql = MySqlUtil()
        self.person = ConfigPerson()

        self.mysql = MySqlUtil()
        # 根据当前登录用户的login_name获取对应的user id
        self.login_name = self.person.conf_loginName()
        self.mysql.cursor.execute("select id from ep_users where login_name='%s'" % self.login_name)
        self.user_id = self.mysql.cursor.fetchone()[0]
        # 获取当前登录应用的appId和id
        self.appId = conf_appid()  # 获取测试应用appId
        self.mysql.cursor.execute("select id from ep_company_app where app_id='%s'" % self.appId)
        self.company_app_id = self.mysql.cursor.fetchone()[0]
        # 通过sql授权应用
        self.auth_id = ChildUserSqlUtil.insert_auth(self.user_id, self.company_app_id)
        # 通过sql新建子账号
        self.child_id_list, self.child_name_list = ChildUserSqlUtil.insert_child_users(5, self.user_id,self.company_app_id)

        self.api_url = 'coding/v3/getEncryptedStringByApp'
        self.url = conf_url() + self.api_url

    def test_get_encrypted_string_by_app_01(self):
        u'应用id和jwt参数正确，获取加密串请求成功'
        url = self.url
        data = {
            "appId": self.appId,
            "jwt": get_jwt('jwt'),
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_encrypted_string_by_app_02(self):
        u'应用id为空，获取加密串请求失败'
        url = self.url
        data = {
            "appId": "",
            "jwt": get_jwt('jwt'),
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = '应用ID不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_encrypted_string_by_app_03(self):
        u'应用id为空串，获取加密串请求失败'
        url = self.url
        data = {
            "appId": "     ",
            "jwt": get_jwt('jwt'),
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = '应用ID不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_encrypted_string_by_app_04(self):
        u'应用id不存在，获取加密串请求失败'
        url = self.url
        data = {
            "appId": "xxx",
            "jwt": get_jwt('jwt'),
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = '企业应用ID不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_encrypted_string_by_app_05(self):
        u'jwt为空，获取加密串请求失败'
        url = self.url
        data = {
            "appId": self.appId,
            "jwt": "",
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = '用户名jwt不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_encrypted_string_by_app_06(self):
        u'jwt为空串，获取加密串请求失败'
        url = self.url
        data = {
            "appId": self.appId,
            "jwt": "    ",
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = '用户名jwt不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_encrypted_string_by_app_07(self):
        u'jwt已过期，获取加密串请求失败'
        url = self.url
        data = {
            "appId": self.appId,
            "jwt": "eyJhbGciOiJIUzI1NiJ9.eyJlcHRva2VuIjoidG9rZW46MTU2ODEwMzE0MDU4OCIsImFwcGlkIjoiZXBhc3MiLCJzdWJ0b2tlbiI6IiIsInVzZXJpZCI6ImFkbWluIiwiaWF0IjoiMjAxOS0wOS0xMCAwMS4xMi4yMCIsInVwZHQiOiIyMDE5LTA5LTEwIDAxLjEyLjIwIn0.GNuiw0pPfZHGUeLN8J0JJRm_N-KoY0x-X5zD2ddM8-U",
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = 'JWT解析失败'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_encrypted_string_by_app_08(self):
        u'jwt参数错误，获取加密串请求失败'
        url = self.url
        data = {
            "appId": self.appId,
            "jwt": "323231zdcz",
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = 'JWT解析失败'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_encrypted_string_by_app_09(self):
        u'传入的子账号不属于当前用户，获取加密串请求失败'
        url = self.url
        data = {
            "appId": self.appId,
            "jwt": get_jwt('jwt'),
            "subAccount": "sss"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = '传入的子账号不属于登陆用户'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def test_get_encrypted_string_by_app_10(self):
        u'应用id不是认证登录时的应用id，获取加密串请求失败'
        url = self.url
        data = {
            "appId": "wangjing_app",
            "jwt": get_jwt('jwt'),
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = '应用安全级别改变,认证类型有效期过期,请进行补充认证或重新开始认证'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_encrypted_string_by_app_11(self):
        u'用户没有使用当前应用的权限，获取加密串请求失败'
        self.mysql.sql_delete("delete from ep_user_company_app where id=%s" % self.auth_id)
        ChildUserSqlUtil.delete_datas_by_id('ep_child_user', self.child_id_list)

        url = self.url
        data = {
            "appId": self.appId,
            "jwt": get_jwt('jwt'),
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print('='*10,re)
        expect_status = '用户'+CP().conf_loginName()+'没有应用epass_app的使用权限'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def tearDown(self):
        '''根据id清除测试所创数据'''
        self.mysql.sql_delete("delete from ep_user_company_app where id=%s" % self.auth_id)
        ChildUserSqlUtil.delete_datas_by_id('ep_child_user', self.child_id_list)
        self.mysql.db_sql.close()

if __name__ == "__main__":
    unittest.main()