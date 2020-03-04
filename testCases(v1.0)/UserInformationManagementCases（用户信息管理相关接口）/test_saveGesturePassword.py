# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/9/24
@File : saveGesturePassword.py
@describe : 鉴权1.0 生物信息维护-新增手势密码

"""

from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP
import unittest
import time
from ep_common.child_user_sql import ChildUserSqlUtil


class SaveGesture(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/authinfo/saveGesturePassword'
        self.url = conf_url() + self.api_url
        self.mysql = MySqlUtil()
        # 获取用户id，用于向用户插入手势测试手势已存在的用例和断言
        self.mysql.cursor.execute("select id from ep_users where login_name ='" + CP().conf_loginName() + "'")
        self.user_id = self.mysql.cursor.fetchone()[0]
        # 清空手势，用于测试手势新增
        self.clear_gesture_sql = "update ep_user_auth_info set gesture_data='' where user_id in (select id from ep_users where login_name='" + CP().conf_loginName() + "')"
        self.mysql.sql_update(self.clear_gesture_sql)

    def test_save_gesture_password_01(self):
        u"登录名正确，手势密码字符长度（大于或等于4位）正确，新增手势密码请求成功"
        data = {
            "gestureData": "12345",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '操作成功'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def test_save_gesture_password_02(self):
        u"用户名为空,请求失败"
        data = {
            "gestureData": "12345",
            "loginName": "",
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '用户名不能为空'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def test_save_gesture_password_03(self):
        u"用户不存在,请求失败"
        data = {
            "gestureData": "12345",
            "loginName": "notfound",
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '该用户不存在'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def test_save_gesture_password_04(self):
        u"用户手势密码已存在,请求失败"
        self.mysql.cursor.execute("select gesture_data from ep_user_auth_info where user_id='%s'" % self.user_id)
        result = self.mysql.cursor.fetchone()
        if result is None:
            id = ChildUserSqlUtil.get_id('ep_user_auth_info')
            insert_sql = "INSERT INTO ep_user_auth_info(id, user_id, face_model_id, voice_model_id, otp_key, gesture_data, qq_account, wechat_account, face_pic_url, app_awake_type, lock_type) VALUES (%s, %s, '', NULL,NULL, '12345678', NULL, NULL, NULL, 'password', '')" % (
                id, self.user_id)
            print('手势不存在则执行sql创建', insert_sql)
            self.mysql.sql_insert(insert_sql)
        elif result == ('',):
            update_sql = "update ep_user_auth_info set gesture_data='12345678' where user_id='%s' " % self.user_id
            print('手势存在且为空则执行sql更新', update_sql)
            self.mysql.sql_update(update_sql)
        else:
            pass
        data = {
            "gestureData": "12345",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '该用户手势密码已存在'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def test_save_gesture_password_05(self):
        u"手势密码长度小于4位，请求失败"
        data = {
            "gestureData": "123",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码长度错误'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def test_save_gesture_password_06(self):
        u"手势密码超长,请求失败"
        data = {
            "gestureData": "1234567891",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码长度错误'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_save_gesture_password_07(self):
        u"手势密码为空，请求失败"
        data = {
            "gestureData": "",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码长度错误'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def test_save_gesture_password_08(self):
        u"手势密码包含非数字字符，请求失败"
        # Todo 验证bug ID1000710
        data = {
            "gestureData": "asdf 123",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '参数错误'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def test_save_gesture_password_09(self):
        u"手势密码参数位相同,请求失败"
        # Todo 验证bug ID1000694
        data = {
            "gestureData": "11111",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '参数错误'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def tearDown(self):
        # 删除测试数据
        self.mysql.sql_update(self.clear_gesture_sql)
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
