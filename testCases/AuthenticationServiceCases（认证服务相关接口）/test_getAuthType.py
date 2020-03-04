# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_getAuthType.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.ConfigServer import conf_appid
from ep_common.MysqldbUtil import MySqlUtil
import unittest


class GetAuth(unittest.TestCase):

    def setUp(self):

        self.api_url = 'xxx/auth/getAuthType'
        self.url = conf_url() + self.api_url

    def test_getauth_01(self):
        u"应用id正确，获取应用认证列表请求成功"
        url = self.url
        data = {
            "appId": conf_appid()
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

    def test_getauth_02(self):
        u"应用id为空，获取应用认证列表请求失败"
        url = self.url
        data = {
            "appId": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '企业应用ID不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_getauth_03(self):
        u"应用id为空格，获取应用认证列表请求失败"
        url = self.url
        data = {
            "appId": " "
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '企业应用ID不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_getauth_04(self):
        u"应用id不存在，获取应用认证列表请求失败"
        url = self.url
        data = {
            "appId": "appxxx"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '企业应用ID不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()






