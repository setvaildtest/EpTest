# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/9/24
@File : test_feedbacksave.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
import unittest




class SaveDevice(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/feedback/save'
        self.url = conf_url() + self.api_url
        self.mysql = MySqlUtil()

    def test_save_device_01(self):
        u"必填参数正确，用户反馈保存接口请求成功"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "13458530487",
            "content": "反馈内容",
            "name": "竹云科技",
            "sortName": "epass_app",
            "urlList": [],
            "user": "cxh"
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
        u"app参数为空，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "",
            "contactInformation": "13458530487",
            "content": "反馈内容",
            "name": "竹云科技",
            "sortName": "epass_app",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:反馈服务名不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_03(self):
        u"app参数为空串，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "   ",
            "contactInformation": "13458530487",
            "content": "反馈内容",
            "name": "竹云科技",
            "sortName": "epass_app",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:反馈服务名不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_04(self):
        u"联系方式参数为空，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "",
            "content": "反馈内容",
            "name": "竹云科技",
            "sortName": "epass_app",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:联系方式不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_05(self):
        u"联系方式参数为空串，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "   ",
            "content": "反馈内容",
            "name": "竹云科技",
            "sortName": "epass_app",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:联系方式不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_06(self):
        u"反馈内容参数为空，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "13458530487",
            "content": "",
            "name": "竹云科技",
            "sortName": "epass_app",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:反馈内容不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_07(self):
        u"反馈内容参数为空串，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "13458530487",
            "content": "    ",
            "name": "竹云科技",
            "sortName": "epass_app",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:反馈内容不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_08(self):
        u"企业名称参数为空，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "13458530487",
            "content": "反馈内容",
            "name": "",
            "sortName": "epass_app",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:企业名称不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_09(self):
        u"企业名称参数为空串，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "13458530487",
            "content": "反馈内容",
            "name": "    ",
            "sortName": "epass_app",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:企业名称不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_10(self):
        u"企业简称参数为空，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "13458530487",
            "content": "反馈内容",
            "name": "竹云科技",
            "sortName": "",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:企业简称不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_11(self):
        u"企业简称参数为空串，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "13458530487",
            "content": "反馈内容",
            "name": "竹云科技",
            "sortName": "   ",
            "urlList": [],
            "user": "cxh"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:企业简称不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_12(self):
        u"用户登录名参数为空，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "13458530487",
            "content": "反馈内容",
            "name": "竹云科技",
            "sortName": "epass_app",
            "urlList": [],
            "user": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:用户登录名不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_device_13(self):
        u"用户登录名参数为空串，用户反馈保存接口请求失败"
        url = self.url
        data = {
            "app": "epass_app",
            "contactInformation": "13458530487",
            "content": "反馈内容",
            "name": "竹云科技",
            "sortName": "epass_app",
            "urlList": [],
            "user": "   "
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:用户登录名不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()


