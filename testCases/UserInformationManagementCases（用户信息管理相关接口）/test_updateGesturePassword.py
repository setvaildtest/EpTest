# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/19 0019
@File : updateGesturePassword(修改手势密码).py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP
import unittest


class UpdateGesture(unittest.TestCase):

    def setUp(self):
        mysql = MySqlUtil()
        mysql.cursor.execute("select id from ep_users where login_name ='" + CP().conf_loginName() + "'")
        user_id = mysql.cursor.fetchone()[0]
        self.sql = "update ep_user_auth_info set gesture_data = '123456' where user_id = %s" % user_id
        mysql.sql_update(self.sql)
        self.api_url = 'coding/v3/user/authinfo/updateGesturePassword'
        self.url = conf_url() + self.api_url

    def test_update_gesture_password_01(self):
        u"登录名、原手势密码正确，修改手势密码请求成功"
        data = {
            "gestureData": "123456",
            "loginName": CP().conf_loginName(),
            "newGestureData": "123456789"
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(self.url, data)
        print(re)
        result = re['status']
        self.assertEqual(result, 'success', msg=re['status'])

    def test_update_gesture_password_02(self):
        u"新手势密码为空"
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

    def test_update_gesture_password_03(self):
        u"新手势密码小于4位（3位）"
        # todo 后端没有校验，确认后修改验证bugID1000696
        data = {
            "gestureData": "123456",
            "loginName": CP().conf_loginName(),
            "newGestureData": "123"
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '手势密码长度错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_gesture_password_04(self):
        u"新手势密码长度参数位相同位数"
        #todo 验证缺陷ID1000695
        data = {
            "gestureData": "123456",
            "loginName": CP().conf_loginName(),
            "newGestureData": "11111"
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
