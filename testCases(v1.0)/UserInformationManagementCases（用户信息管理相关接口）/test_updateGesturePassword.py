#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/9/24
@File : test_updateGesturePassword.py
@describe : 鉴权1.0 生物信息维护-修改手势密码

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP
from ep_common.child_user_sql import ChildUserSqlUtil
import unittest


class UpdateGesture(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/authinfo/updateGesturePassword'
        self.url = conf_url() + self.api_url
        self.mysql = MySqlUtil()
        self.mysql.cursor.execute("select id from ep_users where login_name ='" + CP().conf_loginName() + "'")
        self.user_id = self.mysql.cursor.fetchone()[0]
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
            print('手势不存在:执行sql创建', insert_sql)
            self.mysql.sql_insert(insert_sql)
        elif result == ('',):
            update_sql = "update ep_user_auth_info set gesture_data='%s' where user_id='%s' " % (
                gesture, self.user_id)
            print('手势存在且为空:执行sql更新', update_sql)
            self.mysql.sql_update(update_sql)
        else:
            print('手势存在且不为空:获取手势')
            gesture = result[0]
        return gesture

    def test_update_gesture_password_01(self):
        u"登录名正确、旧手势密码正确、新手势密码合法，修改手势密码，请求成功"
        old_gesture = self.get_gesture()
        data = {
            "gestureData": old_gesture,
            "loginName": CP().conf_loginName(),
            "newGestureData": "12345"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '操作成功'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_02(self):
        u"用户名为空，请求失败"
        old_gesture = self.get_gesture()
        data = {
            "gestureData": old_gesture,
            "loginName": "",
            "newGestureData": "12345"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '用户名不能为空'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_03(self):
        u"用户名不存在，请求失败"
        old_gesture = self.get_gesture()
        data = {
            "gestureData": old_gesture,
            "loginName": "notfounduser",
            "newGestureData": "12345"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '该用户不存在'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_04(self):
        u"用户名为空,请求失败"
        old_gesture = self.get_gesture()
        data = {
            "gestureData": old_gesture,
            "loginName": "",
            "newGestureData": "1234"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '用户名不能为空'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_05(self):
        u"原手势密码为空,请求失败"
        self.get_gesture()
        data = {
            "gestureData": "",
            "loginName": CP().conf_loginName(),
            "newGestureData": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码不能为空'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_06(self):
        u"用户不存在手势密码,请求失败"
        # 通过sql删除手势密码
        self.mysql.sql_update(self.clear_gesture_sql)
        data = {
            "gestureData": "123456",
            "loginName": CP().conf_loginName(),
            "newGestureData": "12345"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码不存在'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_07(self):
        u"原手势密码不正确,请求失败"
        old_gesture = self.get_gesture()
        data = {
            "gestureData": old_gesture + '1',
            "loginName": CP().conf_loginName(),
            "newGestureData": "12345"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码不匹配'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_08(self):
        u"新手势密码少于4位,请求失败"
        # Todo 验证bug ID1000696
        old_gesture = self.get_gesture()
        data = {
            "gestureData": old_gesture,
            "loginName": CP().conf_loginName(),
            "newGestureData": "123"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码长度错误'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_09(self):
        u"新手势密码超长,请求失败"
        # Todo 验证bugID1000709
        old_gesture = self.get_gesture()
        data = {
            "gestureData": old_gesture,
            "loginName": CP().conf_loginName(),
            "newGestureData": "1234567891234567891234567891234567891234567891234567891234567898"
        }
        print(len('1234567891234567891234567891234567891234567891234567891234567898'))
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '手势密码长度错误'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_10(self):
        u"新手势密码参数位相同,请求失败"
        # todo 验证缺陷ID1000695
        old_gesture = self.get_gesture()
        data = {
            "gestureData": old_gesture,
            "loginName": CP().conf_loginName(),
            "newGestureData": "111111"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '参数错误'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def test_update_gesture_password_11(self):
        u"新手势密码包含非数字字符,请求失败"
        # todo 验证缺陷ID1000695
        old_gesture = self.get_gesture()
        data = {
            "gestureData": old_gesture,
            "loginName": CP().conf_loginName(),
            "newGestureData": "asdf 123"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '参数错误'
        actual_msg = re['message']
        self.assertIn(expect_msg, actual_msg)

    def tearDown(self):
        # 删除测试数据
        self.mysql.sql_update(self.clear_gesture_sql)
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
