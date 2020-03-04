# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/22
@File : update（修改设备指纹备注名）.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.user_device_sql import SqlUtil
import unittest




class UpdateDevice(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/outDevice/update'
        self.url = conf_url() + self.api_url
        SqlUtil.insert_user_data(2, 3)
        SqlUtil.insert_device_data(20, 2)
        self.mysql = MySqlUtil()

    def test_update_device_01(self):
        u"设备id正确，修改本人设备备注请求成功"
        self.mysql.cursor.execute('select id from ep_user_device where user_id = 2')
        device_id = self.mysql.cursor.fetchall()[0][0]
        print(device_id)
        url = self.url
        data = {
            "id": device_id,
            "remarks": "huawei"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        self.mysql.cursor.execute("select remarks from ep_user_device where id =%s" % device_id)
        remarks = self.mysql.cursor.fetchall()[0][0]
        if remarks == 'huawei':
            print("更新成功")
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_device_02(self):
        u"设备id不存在，修改设备备注请求返回报错信息"
        url = self.url
        data = {
            "id": 999,
            "remarks": "huawei"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '该设备不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_device_03(self):
        u"设备id为空，修改设备备注请求返回报错信息"
        url = self.url
        data = {
            "id": "",
            "remarks": "huawei"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def test_update_device_04(self):
        u"设备id为空串，修改设备备注请求返回报错信息"
        url = self.url
        data = {
            "id": "   ",
            "remarks": "huawei"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def test_update_device_05(self):
        u"设备id非本人设备，修改设备备注请求返回报错信息"
        self.mysql.cursor.execute('select id from ep_user_device where user_id != 2')
        self.device_id = self.mysql.cursor.fetchall()[0][0]
        print(self.device_id)
        url = self.url
        data = {
            "id": self.device_id,
            "remarks": "huawei"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '只能修改本人设备'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def test_update_device_06(self):
        u"设备备注为空，修改本人设备备注请求失败"
        self.mysql.cursor.execute('select id from ep_user_device where user_id = 2')
        self.device_id = self.mysql.cursor.fetchall()[0][0]
        print(self.device_id)
        url = self.url
        data = {
            "id": self.device_id,
            "remarks": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def test_update_device_07(self):
        u"设备备注为空串，修改本人设备备注请求失败"
        self.mysql.cursor.execute('select id from ep_user_device where user_id = 2')
        self.device_id = self.mysql.cursor.fetchall()[0][0]
        print(self.device_id)
        url = self.url
        data = {
            "id": self.device_id,
            "remarks": "    "
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def tearDown(self):
        self.mysql.sql_delete("delete from ep_user_device where f_user like 'zxh%'")
        self.mysql.sql_delete("delete from ep_users where name like 'zxh%'")



if __name__ == "__main__":
    unittest.main()


