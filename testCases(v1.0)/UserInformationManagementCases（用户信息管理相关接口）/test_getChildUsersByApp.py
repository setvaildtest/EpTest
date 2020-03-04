#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/22
@File : test_getChildUsersByApp.py
@describe : 该模块用户测试子账号查询接口(登录用户查询自己在某个授权应用下的子账号信息)

"""
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.ConfigServer import conf_appid
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson
from ep_common.child_user_sql import ChildUserSqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP


class GetChildUsersByApp(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/outUserAndApp/getChildUserByApp'
        self.url = conf_url() + self.api_url
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

    # 测试获取子账号外部接口
    def test_get_child_users_01(self):
        '''应用id和用户名入参正确，返回对应的子账号信息'''
        print('查询子账号接口api_url：=================>', self.url)
        data = {
            "appId": self.appId,
	        "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询子账号接口入参：=================>\n', data)
        print('查询子账号接口响应：=================>\n', re)
        # 断言响应status
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status)

    def test_get_child_users_02(self):
        '''应用id为空，获取子账号信息失败'''
        print('查询子账号接口api_url：=================>', self.url)
        data = {
            "appId": "",
            "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询子账号接口入参：=================>\n', data)
        print('查询子账号接口响应：=================>\n', re)

        # 断言响应数据
        expect_status = '应用id不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_child_users_03(self):
        '''应用id为空串，获取子账号信息失败'''
        print('查询子账号接口api_url：=================>', self.url)
        data = {
            "appId": "    ",
            "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询子账号接口入参：=================>\n', data)
        print('查询子账号接口响应：=================>\n', re)

        # 断言响应数据
        expect_status = '应用id不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_child_users_04(self):
        '''应用id不存在，获取子账号信息失败'''
        #todo 验证缺陷
        print('查询子账号接口api_url：=================>', self.url)
        data = {
            "appId": "epass121",
            "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询子账号接口入参：=================>\n', data)
        print('查询子账号接口响应：=================>\n', re)

        # 断言响应数据
        expect_status = 'appId不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status)

    def test_get_child_users_05(self):
        '''用户没有使用当前应用的权限，获取子账号信息失败'''
        # todo 验证缺陷
        ChildUserSqlUtil.delete_datas_by_id('ep_child_user', self.child_id_list)
        self.mysql.sql_delete("delete from ep_user_company_app where id=%s" % self.auth_id)

        print('查询子账号接口api_url：=================>', self.url)
        data = {
            "appId": self.appId,
            "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询子账号接口入参：=================>\n', data)
        print('查询子账号接口响应：=================>\n', re)

        # 断言响应数据
        expect_status = '用户' + CP().conf_loginName() + '没有应用epass_app的使用权限'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_child_users_06(self):
        '''用户名为空，获取子账号信息失败'''
        ChildUserSqlUtil.delete_datas_by_id('ep_child_user', self.child_id_list)
        self.mysql.sql_delete("delete from ep_user_company_app where id=%s" % self.auth_id)

        print('查询子账号接口api_url：=================>', self.url)
        data = {
            "appId": self.appId,
            "loginName": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询子账号接口入参：=================>\n', data)
        print('查询子账号接口响应：=================>\n', re)

        # 断言响应数据
        # 断言响应数据
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status)

    def test_get_child_users_07(self):
        '''用户名为空串，获取子账号信息失败'''
        # todo 验证缺陷
        ChildUserSqlUtil.delete_datas_by_id('ep_child_user', self.child_id_list)
        self.mysql.sql_delete("delete from ep_user_company_app where id=%s" % self.auth_id)

        print('查询子账号接口api_url：=================>', self.url)
        data = {
            "appId": self.appId,
            "loginName": "   "
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询子账号接口入参：=================>\n', data)
        print('查询子账号接口响应：=================>\n', re)

        # 断言响应数据
        # 断言响应数据
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status)

    def test_get_child_users_08(self):
        '''用户名参数超过45个字符，获取子账号信息失败'''
        ChildUserSqlUtil.delete_datas_by_id('ep_child_user', self.child_id_list)
        self.mysql.sql_delete("delete from ep_user_company_app where id=%s" % self.auth_id)

        print('查询子账号接口api_url：=================>', self.url)
        data = {
            "appId": self.appId,
            "loginName": "XtXe4AuxH1cFgO48POglQtqnfk7itxC69GZHeH2dW5Gehc"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询子账号接口入参：=================>\n', data)
        print('查询子账号接口响应：=================>\n', re)

        # 断言响应数据
        # 断言响应数据
        expect_status = '主账号的名称长度不超过45;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status)

    def test_get_child_users_09(self):
        '''用户名不存在，获取子账号信息失败'''
        # todo 验证缺陷
        ChildUserSqlUtil.delete_datas_by_id('ep_child_user', self.child_id_list)
        self.mysql.sql_delete("delete from ep_user_company_app where id=%s" % self.auth_id)

        print('查询子账号接口api_url：=================>', self.url)
        data = {
            "appId": self.appId,
            "loginName": "cxh122222212"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询子账号接口入参：=================>\n', data)
        print('查询子账号接口响应：=================>\n', re)

        # 断言响应数据
        # 断言响应数据
        expect_status = '用户名不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status)

    # 清除测试数据
    def tearDown(self):
        '''根据id清除测试所创数据'''
        ChildUserSqlUtil.delete_datas_by_id('ep_child_user', self.child_id_list)
        self.mysql.sql_delete("delete from ep_user_company_app where id=%s" % self.auth_id)
        self.mysql.db_sql.close()


if __name__ == '__main__':
    unittest.main()
