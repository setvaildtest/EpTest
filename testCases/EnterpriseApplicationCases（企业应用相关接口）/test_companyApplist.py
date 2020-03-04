# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_companyApplist.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
import unittest
import time
from random import choice


class CompanyAppList(unittest.TestCase):

    def setUp(self):

        self.api_url = 'coding/v3/companyApp/list'
        self.url = conf_url() + self.api_url

        self.mysql = MySqlUtil()
        i = 1
        while i < 20:
            self.mysql.cursor.execute('select max(id) from ep_company_app')
            app_max_id = self.mysql.cursor.fetchall()[0][0]
            print(app_max_id)
            if app_max_id == None:
                id = 1
            else:
                id = app_max_id + 1
            name = 'testapp' + str(i)
            security_level_id = '1'
            company_id = '1'
            sort_name = 'testapp' + str(i)
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            create_user = 'admin'
            update_user = 'admin'
            type = '1'
            app_id = 'testapp' + str(i)
            sso_address = '1'
            is_relay = '0'
            sql = 'insert into ep_company_app(id,name,security_level_id,company_id,sort_name,create_time,update_time,create_user,update_user,type,app_id,sso_address,is_relay) values'
            sql = sql + '("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (id,name,security_level_id,company_id,sort_name,create_time,update_time,create_user,update_user,type,app_id,sso_address,is_relay)
            i += 1
            # print('执行sql:',sql)
            self.mysql.sql_insert(sql)

    def test_companyApp_list_01(self):
        u"查询条件为空，获取所有企业应用列表成功"
        url = self.url
        data = {
            "condition": "",  #查询条件
            "limit": "",  #显示条数
            "page": 1,  #第几页
            "type": ""  #应用类型
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_companyApp_list_02(self):
        u"查询条件为模糊查询，获取包含关键字的企业应用列表成功"
        url = self.url
        data = {
            "condition": "e账通",
            "limit": "",
            "page": 1,
            "type": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_companyApp_list_03(self):
        u"查询条件为精确查询，获取该企业应用信息成功"
        url = self.url
        data = {
            "condition": "e账通控制台",
            "limit": "",
            "page": 1,
            "type": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_companyApp_list_04(self):
        u"查询条件为空，获取第1页10条企业应用信息成功"
        url = self.url
        data = {
            "condition": "",
            "limit": 10,
            "page": 1,
            "type": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_companyApp_list_05(self):
        u"查询条件为空，获取第2页11条企业应用信息成功"
        url = self.url
        data = {
            "condition": "",
            "limit": 11,
            "page": 2,
            "type": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_companyApp_list_06(self):
        u"查询应用类型为app的应用，获取企业应用信息成功"
        url = self.url
        data = {
            "condition": "",
            "limit": "",
            "page": 1,
            "type": "0"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def tearDown(self):
        mysql = MySqlUtil()
        self.sql = "delete from ep_company_app where name like 'testapp%'"
        mysql.sql_update(self.sql)

if __name__ == "__main__":
    unittest.main()






