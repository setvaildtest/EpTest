# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/9/23
@File : test_Devicesave.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP
import unittest




class SaveDevice(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/outDevice/save'
        self.url = conf_url() + self.api_url
        self.mysql = MySqlUtil()

    def test_save_device_01(self):
        u"参数正确，新增设备指纹请求成功"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QPEoqGGSoiNZ9SbXLIxdmGG7NkKy3LFYg",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "v1ci2Do3UARZTtyttQo9",
            "remarks": "l7ISTBEckfgls1ExoqfBKxucneBiEAET5H9Msw4dg6a41",
            "user": "cxh121"
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

    def test_save_device_02(self):
        u"设备指纹参数为空，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "012F5DA2C5FF",
            "remarks": "host-name",
            "user": CP().conf_loginName()
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '用户绑定的设备指纹不能为空'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_03(self):
        u"设备指纹参数为空串，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "     ",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "012F5DA2C5FF",
            "remarks": "host-name",
            "user": CP().conf_loginName()
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '用户绑定的设备指纹不能为空'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_04(self):
        u"设备指纹参数超过50个字符，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QPEoqGGSoiNZ9SbXLIxdmGG7NkKy3LFYgP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "012F5DA2C5FF",
            "remarks": "host-name",
            "user": CP().conf_loginName()
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'fail'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_05(self):
        u"设备类型不存在，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "3",
            "loginName": CP().conf_loginName(),
            "mac": "012F5DA2C5FF",
            "remarks": "host-name",
            "user": CP().conf_loginName()
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '不支持的绑定类型'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_06(self):
        u"设备类型参数为空，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "",
            "loginName": CP().conf_loginName(),
            "mac": "012F5DA2C5FF",
            "remarks": "host-name",
            "user": CP().conf_loginName()
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


    def test_save_device_07(self):
        u"设备类型参数为空串，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "    ",
            "loginName": CP().conf_loginName(),
            "mac": "012F5DA2C5FF",
            "remarks": "host-name",
            "user": CP().conf_loginName()
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

    def test_save_device_08(self):
        u"E账通账户名参数为空，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": "",
            "mac": "012F5DA2C5FF",
            "remarks": "host-name",
            "user": CP().conf_loginName()
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

    def test_save_device_09(self):
        u"E账通账户名参数为空串，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": "   ",
            "mac": "012F5DA2C5FF",
            "remarks": "host-name",
            "user": CP().conf_loginName()
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


    def test_save_device_10(self):
        u"E账通账户名不存在，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": "cxh121",
            "mac": "012F5DA2C5FF",
            "remarks": "host-name",
            "user": CP().conf_loginName()
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'fail'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_11(self):
        u"mac地址为空，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "",
            "remarks": "host-name",
            "user": CP().conf_loginName()
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

    def test_save_device_12(self):
        u"mac地址为空串，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "      ",
            "remarks": "host-name",
            "user": CP().conf_loginName()
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


    def test_save_device_13(self):
        u"mac地址参数超过20个字符，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "wktxmy2YvkBwoOm15v4lg",
            "remarks": "host-name",
            "user": CP().conf_loginName()
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'mac地址长度不超过20;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_14(self):
        u"备注参数为空，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "wktxmy2YvkBwoOm15v4l",
            "remarks": "",
            "user": CP().conf_loginName()
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

    def test_save_device_15(self):
        u"备注参数为空串，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "wktxmy2YvkBwoOm15v4l",
            "remarks": "    ",
            "user": CP().conf_loginName()
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

    def test_save_device_16(self):
        u"备注参数超过45个字符，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "wktxmy2YvkBwoOm15v4l",
            "remarks": "aHxmNXYV9RrMMaCZy1qAklQaQLDhFLbFK7RDY5kp1SENmb",
            "user": CP().conf_loginName()
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '机器备注名长度不超过45;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_17(self):
        u"用户账户名参数为空，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "wktxmy2YvkBwoOm15v4l",
            "remarks": "aHxmNXYV9RrMMaCZ",
            "user": ""
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

    def test_save_device_18(self):
        u"用户账户名参数为空串，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "wktxmy2YvkBwoOm15v4l",
            "remarks": "aHxmNXYV9RrMMaCZ",
            "user": "    "
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

    def test_save_device_19(self):
        u"用户账户名参数超过45个字符，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": CP().conf_loginName(),
            "mac": "wktxmy2YvkBwoOm15v4l",
            "remarks": "aHxmNXYV9RrMMaCZ",
            "user": "iwA7KCd45YlebetN5RuUzZ3a3qADB4EXbaf49i3UQcoscZ"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '用户账户名长度不超过45;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_20(self):
        u"E账通账户名参数超过45个字符，新增设备指纹请求失败"
        url = self.url
        data = {
            "deviceFingerpring": "2YXleepaXZUyqVDa1QP",
            "deviceType": "1",
            "loginName": "iwA7KCd45YlebetN5RuUzZ3a3qADB4EXbaf49i3UQcoscZ",
            "mac": "wktxmy2YvkBwoOm15v4l",
            "remarks": "aHxmNXYV9RrMMaCZ",
            "user": CP().conf_loginName()
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'E账通账户名长度不超过45;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def tearDown(self):
        self.mysql.sql_delete("delete from ep_user_device where f_user like 'cxh%'")
        self.mysql.db_sql.close()

    if __name__ == '__main__':
        unittest.main()
