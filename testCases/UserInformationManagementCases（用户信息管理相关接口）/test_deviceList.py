#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/21
@File : deviceList(获取设备指纹列表外部接口).py
@describe : 该模块用于测试获取设备指纹列表外部接口，包括向数据库表插入测试数据，请求路径、入参定义和响应内容接收

"""

import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.user_device_sql import *


class DeviceList(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/v3/outDevice/list'
        self.url = conf_url() + self.api_url
        self.mysql = MySqlUtil()
        SqlUtil.insert_user_data(2, 3)
        SqlUtil.insert_device_data(20,2)
    # 测试获取设备指纹列表接口
    def test_deviceList_01(self):
        '''查询条件为空，根据页码、记录数，返回登录用户全部设备信息'''
        print('获取设备指纹列表api_url：=================>', self.url)
        # 三个入参都非必填，当data为空时，默认返回第一个分页10条数据
        condition = ""
        page = 1
        pagesize = 30
        data = {
            "condition": condition,
            "page": page,
            "pageSize": pagesize
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('获取设备指纹列表接口入参：=================>\n', data)
        print('获取设备指纹列表接口响应：=================>\n', re)
        # 断言响应code
        expect_code = 'info.common.success'
        actual_code = re['code']
        self.assertEqual(expect_code, actual_code)
        # 断言响应数据
        # 1获取接口返回的设备id列表
        re_data = re['body']['data']

        re_device_id_list = []
        for d in re_data:
            re_device_id = d['id']
            re_device_id_list.append(re_device_id)
        # 2通过sql语句从数据库中查询期望的设备id列表：根据入参中的查询条件、页数、每页的个数组合sql
        sql = "select * from ep_user_device where user_id = 2 order by id desc limit "+str(pagesize * (page - 1))+","+str(pagesize)
        print(sql)
        self.mysql.cursor.execute(sql)
        sql_result = self.mysql.cursor.fetchall()
        sql_device_id_list = []
        for t in sql_result:
            device_id = t[0]
            sql_device_id_list.append(device_id)
        # 3判断接口返回的设备列表和数据库查询的期望结果列表是否相符
        self.assertEqual(sql_device_id_list, re_device_id_list)
        print('期望结果',sql_device_id_list)
        print('实际结果', re_device_id_list)

    def test_deviceList_02(self):
        '''查询条件为空，返回登录用户第1页10条的设备信息'''
        print('获取设备指纹列表api_url：=================>', self.url)
        # 三个入参都非必填，当data为空时，默认返回第一个分页10条数据
        condition = ""
        page = 1
        pagesize = 10
        data = {
            "condition": condition,
            "page": page,
            "pageSize": pagesize
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('获取设备指纹列表接口入参：=================>\n', data)
        print('获取设备指纹列表接口响应：=================>\n', re)
        # 断言响应code
        expect_code = 'info.common.success'
        actual_code = re['code']
        self.assertEqual(expect_code, actual_code)
        # 断言响应数据
        # 1获取接口返回的设备id列表
        re_data = re['body']['data']

        re_device_id_list = []
        for d in re_data:
            re_device_id = d['id']
            re_device_id_list.append(re_device_id)
        # 2通过sql语句从数据库中查询期望的设备id列表：根据入参中的查询条件、页数、每页的个数组合sql
        sql = "select * from ep_user_device where user_id = 2 order by id desc limit "+str(pagesize * (page - 1))+","+str(pagesize)
        print(sql)
        self.mysql.cursor.execute(sql)
        sql_result = self.mysql.cursor.fetchall()
        sql_device_id_list = []
        for t in sql_result:
            device_id = t[0]
            sql_device_id_list.append(device_id)
        # 3判断接口返回的设备列表和数据库查询的期望结果列表是否相符
        self.assertEqual(sql_device_id_list, re_device_id_list)
        print('期望结果',sql_device_id_list)
        print('实际结果', re_device_id_list)

    def test_deviceList_03(self):
        '''查询条件为空，返回登录用户第2页9条的设备信息'''
        print('获取设备指纹列表api_url：=================>', self.url)
        # 三个入参都非必填，当data为空时，默认返回第一个分页10条数据
        condition = ""
        page = 2
        pagesize = 9
        data = {
            "condition": condition,
            "page": page,
            "pageSize": pagesize
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('获取设备指纹列表接口入参：=================>\n', data)
        print('获取设备指纹列表接口响应：=================>\n', re)
        # 断言响应code
        expect_code = 'info.common.success'
        actual_code = re['code']
        self.assertEqual(expect_code, actual_code)
        # 断言响应数据
        # 1获取接口返回的设备id列表
        re_data = re['body']['data']

        re_device_id_list = []
        for d in re_data:
            re_device_id = d['id']
            re_device_id_list.append(re_device_id)
        # 2通过sql语句从数据库中查询期望的设备id列表：根据入参中的查询条件、页数、每页的个数组合sql
        sql = "select * from ep_user_device where user_id= 2 order by id desc limit "+str(pagesize * (page - 1))+","+str(pagesize)
        print(sql)
        self.mysql.cursor.execute(sql)
        sql_result = self.mysql.cursor.fetchall()
        sql_device_id_list = []
        for t in sql_result:
            device_id = t[0]
            sql_device_id_list.append(device_id)
        # 3判断接口返回的设备列表和数据库查询的期望结果列表是否相符
        self.assertEqual(sql_device_id_list, re_device_id_list)
        print('期望结果',sql_device_id_list)
        print('实际结果', re_device_id_list)

    def test_deviceList_04(self):
        '''根据备注名进行精确查询，返回登录用户的设备信息'''
        print('获取设备指纹列表api_url：=================>', self.url)
        # 三个入参都非必填，当data为空时，默认返回第一个分页10条数据
        condition = "vivo"
        page = 1
        pagesize = 10
        data = {
            "condition": condition,
            "page": page,
            "pageSize": pagesize
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('获取设备指纹列表接口入参：=================>\n', data)
        print('获取设备指纹列表接口响应：=================>\n', re)
        # 断言响应code
        expect_code = 'info.common.success'
        actual_code = re['code']
        self.assertEqual(expect_code, actual_code)
        # 断言响应数据
        # 1获取接口返回的设备id列表
        re_data = re['body']['data']

        re_device_id_list = []
        for d in re_data:
            re_device_id = d['id']
            re_device_id_list.append(re_device_id)
        # 2通过sql语句从数据库中查询期望的设备id列表：根据入参中的查询条件、页数、每页的个数组合sql
        sql = "select * from ep_user_device where user_id = 2 and CONCAT(mac,remarks,device_fingerprint) like '%" + condition + "%' order by id desc limit "+str(pagesize * (page - 1))+","+str(pagesize)
        print(sql)
        self.mysql.cursor.execute(sql)
        sql_result = self.mysql.cursor.fetchall()
        sql_device_id_list = []
        for t in sql_result:
            device_id = t[0]
            sql_device_id_list.append(device_id)
        # 3判断接口返回的设备列表和数据库查询的期望结果列表是否相符
        self.assertEqual(sql_device_id_list, re_device_id_list)
        print('期望结果',sql_device_id_list)
        print('实际结果', re_device_id_list)

    def test_deviceList_05(self):
        '''根据备注名进行模糊查询，返回登录用户的设备信息'''
        print('获取设备指纹列表api_url：=================>', self.url)
        # 三个入参都非必填，当data为空时，默认返回第一个分页10条数据
        condition = "vi"
        page = 1
        pagesize = 10
        data = {
            "condition": condition,
            "page": page,
            "pageSize": pagesize
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('获取设备指纹列表接口入参：=================>\n', data)
        print('获取设备指纹列表接口响应：=================>\n', re)
        # 断言响应code
        expect_code = 'info.common.success'
        actual_code = re['code']
        self.assertEqual(expect_code, actual_code)
        # 断言响应数据
        # 1获取接口返回的设备id列表
        re_data = re['body']['data']

        re_device_id_list = []
        for d in re_data:
            re_device_id = d['id']
            re_device_id_list.append(re_device_id)
        # 2通过sql语句从数据库中查询期望的设备id列表：根据入参中的查询条件、页数、每页的个数组合sql
        sql = "select * from ep_user_device where user_id = 2 and CONCAT(mac,remarks,device_fingerprint) like '%" + condition + "%' order by id desc limit "+str(pagesize * (page - 1))+","+str(pagesize)
        print(sql)
        self.mysql.cursor.execute(sql)
        sql_result = self.mysql.cursor.fetchall()
        sql_device_id_list = []
        for t in sql_result:
            device_id = t[0]
            sql_device_id_list.append(device_id)
        # 3判断接口返回的设备列表和数据库查询的期望结果列表是否相符
        self.assertEqual(sql_device_id_list, re_device_id_list)
        print('期望结果',sql_device_id_list)
        print('实际结果', re_device_id_list)

    def test_deviceList_06(self):
        '''参数错误，获取设备信息失败'''
        print('获取设备指纹列表api_url：=================>', self.url)
        # 三个入参都非必填，当data为空时，默认返回第一个分页10条数据
        data = {
            "condition": "",
            "page": "",
            "pageSize": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('获取设备指纹列表接口入参：=================>\n', data)
        print('获取设备指纹列表接口响应：=================>\n', re)
        # 断言响应code
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    # 清除测试数据，关闭数据库连接
    def tearDown(self):
        self.mysql.sql_delete("delete from ep_user_device where f_user like 'zxh%'")
        self.mysql.sql_delete("delete from ep_users where name like 'zxh%'")
        self.mysql.db_sql.close()

    if __name__ == '__main__':
        unittest.main()
