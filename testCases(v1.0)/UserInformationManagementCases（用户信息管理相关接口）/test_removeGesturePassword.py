#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/9/24
@File : test_removeGesturePassword.py
@describe : 鉴权1.0 生物信息维护-删除手势密码

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP
from ep_common.child_user_sql import ChildUserSqlUtil
import unittest


class RemoveGesture(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/authinfo/removeGesturePassword'
        self.url = conf_url() + self.api_url
        self.mysql = MySqlUtil()
        # 查询用户id，用于获取用户原手势以及断言
        self.mysql.cursor.execute("select id from ep_users where login_name ='" + CP().conf_loginName() + "'")
        self.user_id = self.mysql.cursor.fetchone()[0]
        # 清空手势sql，用于测试手势不存在的用例和清除测试数据
        self.clear_gesture_sql = "update ep_user_auth_info set gesture_data='' where user_id in (select id from ep_users where login_name='" + CP().conf_loginName() + "')"

    def get_gesture(self):
        u'通过sql查询配置用户的手势用于修改，若手势不存在或值为空则创建或更新手势'
        self.mysql.cursor.execute("select gesture_data from ep_user_auth_info where user_id='%s'" % self.user_id)
        result = self.mysql.cursor.fetchone()
        print('查询原手势结果：', result)
        gesture = '12345678'
        if result is None:
            id = ChildUserSqlUtil.get_id('ep_user_auth_info')
            insert_sql = "INSERT INTO ep_user_auth_info(id, user_id, face_model_id, voice_model_id, otp_key, gesture_data, qq_account, wechat_account, face_pic_url, app_awake_type, lock_type) VALUES (%s, %s, '', NULL,'Y2GGCGHBMWH67Q45', '%s', NULL, NULL, NULL, 'password', '')" % (
                id, self.user_id, gesture)
            print('手势不存在：执行sql创建', insert_sql)
            self.mysql.sql_insert(insert_sql)
        elif result == ('',):
            update_sql = "update ep_user_auth_info set gesture_data='%s' where user_id='%s' " % (
                gesture, self.user_id)
            print('手势存在且为空：执行sql更新', update_sql)
            self.mysql.sql_update(update_sql)
        else:
            print('手势存在且不为空：获取手势')
            gesture = result[0]
        return gesture

    def test_delete_gesture_password_01(self):
        u"用户名正确、手势密码正确，请求成功"
        gesture = self.get_gesture()
        data = {
            "gestureData": gesture,
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '操作成功'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_delete_gesture_password_02(self):
        u"用户名为空，请求失败"
        gesture = self.get_gesture()
        data = {
            "gestureData": gesture,
            "loginName": "",
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '用户名不能为空'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_delete_gesture_password_03(self):
        u"用户名不存在、请求成功"
        gesture = self.get_gesture()
        data = {
            "gestureData": gesture,
            "loginName": "notfounduser",
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '该用户不存在'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_delete_gesture_password_04(self):
        u"手势密码不正确，请求失败"
        # Todo 验证bug ID1000714
        gesture = self.get_gesture()
        data = {
            "gestureData": gesture + '1',
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码不匹配'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_delete_gesture_password_05(self):
        u"手势密码不存在，请求失败"
        self.mysql.sql_update(self.clear_gesture_sql)
        data = {
            "gestureData": "",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码不存在'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def tearDown(self):
        # 删除测试数据
        self.mysql.sql_update(self.clear_gesture_sql)
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
