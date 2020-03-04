# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/21 0019
@File : updateGesturePassword(删除手势密码).py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP
import unittest


class RemoveGesture(unittest.TestCase):

    def setUp(self):
        # mysql = MySqlUtil()
        # mysql.cursor.execute("select id from ep_users where login_name ='" + CP().conf_loginName() + "'")
        # user_id = mysql.cursor.fetchone()[0]
        # self.sql = "update ep_user_auth_info set gesture_data = '123456' where user_id = %s" % user_id
        # mysql.sql_update(self.sql)
        self.api_url = 'coding/v3/user/authinfo/removeGesturePassword'
        self.url = conf_url() + self.api_url

    def test_remove_gesture_password_01(self):
        u"登录名正确，带原密码参数，删除用户手势密码操作成功"
        data = {
            "gestureData": "123456",
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

    def test_remove_gesture_password_02(self):
        u"登录名正确，不带带原密码参数，删除用户手势密码操作成功"
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
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_remove_gesture_password_03(self):
        u"不传递任何参数，删除用户手势密码"
        # todo 需要确认不传递任何参数可以删除
        data = {
            "gestureData": "",
            "loginName": '',
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

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
