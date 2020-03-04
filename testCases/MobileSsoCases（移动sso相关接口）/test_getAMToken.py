# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/9/10
@File : test_getAMToken.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.JwtGet import get_jwt
import unittest
import time

from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigServer import conf_url
from ep_common.child_user_sql import ChildUserSqlUtil


class GetAmToken(unittest.TestCase):

    def setUp(self):
        api_url = "coding/v3/getAMToken"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()


    def test_get_am_token_01(self):
        u"正确填写IP参数，用户登录后获取amtoken请求成功"
        url = self.url
        data = {
            "ip" : "192.168.0.194"
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

    def test_get_am_token_02(self):
        u"ip为空，用户登录后获取amtoken请求失败"
        url = self.url
        data = {
            "ip" : ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误:ip不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
