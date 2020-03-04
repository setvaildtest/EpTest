# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/13
@File : saveGesturePassword(新增手势密码).py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP
import unittest


class SaveGesture(unittest.TestCase):

    def setUp(self):
        mysql = MySqlUtil()
        self.sql = "update ep_user_auth_info set gesture_data = '' where user_id in (select id from ep_users where login_name = '" + CP().conf_loginName() + "')"
        print('初始化sql==================>>>',self.sql)
        mysql.sql_update(self.sql)
        self.api_url = 'coding/v3/user/authinfo/saveGesturePassword'
        self.url = conf_url() + self.api_url

    def test_save_gesture_password_01(self):
        u"登录名正确，手势密码字符长度（大于或等于4位）正确，新增手势密码请求成功"
        data = {
            "gestureData": "12345",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_gesture_password_02(self):
        u"登录名正确，手势密码长度小于4位，提示手势密码长度错误"
        data = {
            "gestureData": "123",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '手势密码长度错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_gesture_password_03(self):
        u"登录名正确，手势密码长度参数位相同位数"
        #Todo 验证bug ID1000694
        data = {
            "gestureData": "11111",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_save_gesture_password_04(self):
        u"登录名正确，手势密码为空"
        data = {
            "gestureData": "",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '手势密码长度错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()