# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/9/24
@File : getGesturePassword.py
@describe : 鉴权1.0 生物信息维护-获取手势密码

"""

from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.ConfigPerson import ConfigPerson as CP
import unittest
import time
from ep_common.child_user_sql import ChildUserSqlUtil


class GetGesture(unittest.TestCase):
    def setUp(self):
        self.api_url = 'coding/authinfo/getGesturePassword'
        self.url = conf_url() + self.api_url
        self.mysql = MySqlUtil()

    def insert_gesture(self):
        u'通过sql查询配置用户的手势用于修改，若手势不存在或值为空则创建或更新手势'
        # Todo 验证缺陷ID1000705
        # 查询用户id用于查询和插入手势
        self.mysql.cursor.execute("select id from ep_users where login_name ='" + CP().conf_loginName() + "'")
        user_id = self.mysql.cursor.fetchone()[0]
        print('用户id：', user_id)
        # 查询用户手势
        self.mysql.cursor.execute("select gesture_data from ep_user_auth_info where user_id='%s'" % user_id)
        result = self.mysql.cursor.fetchone()
        print('查询原手势结果：', result)
        gesture = '12345678'
        if result is None:
            id = ChildUserSqlUtil.get_id('ep_user_auth_info')
            insert_sql = "INSERT INTO ep_user_auth_info(id, user_id, face_model_id, voice_model_id, otp_key, gesture_data, qq_account, wechat_account, face_pic_url, app_awake_type, lock_type) VALUES (%s, %s, '', NULL,NULL, '%s', NULL, NULL, NULL, 'password', '')" % (
                id, user_id, gesture)
            print('手势不存在则执行sql创建', insert_sql)
            self.mysql.sql_insert(insert_sql)
        elif result == ('',):
            update_sql = "update ep_user_auth_info set gesture_data='%s' where user_id='%s' " % (
                gesture, user_id)
            print('手势存在且为空则执行sql更新', update_sql)
            self.mysql.sql_update(update_sql)
        else:
            gesture = result[0]
        return gesture

    def test_get_gesture_password_01(self):
        u'用户名正确且手势密码存在，请求成功'
        # Todo 验证缺陷ID1000705
        self.insert_gesture()
        data = {
            "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '操作成功'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def test_get_gesture_password_02(self):
        u'用户名正确且手势密码不存在，请求成功'
        # Todo 验证缺陷ID1000705
        # 删除测试用户的手势
        delete_gesture_sql = "delete from ep_user_auth_info where user_id in (select id from ep_users where login_name = '" + CP().conf_loginName() + "')"
        self.mysql.sql_delete(delete_gesture_sql)
        data = {
            "loginName": CP().conf_loginName()
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '操作成功'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def test_get_gesture_password_03(self):
        u'用户名为空，请求失败'
        # Todo 验证缺陷ID1000705
        self.insert_gesture()
        data = {
            "loginName": ""
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(self.url, data)
        print("response:", re)
        expect_msg = '用户名不能为空'
        actual_msg = re['message']
        self.assertEqual(expect_msg, actual_msg)

    def tearDown(self):
        # 删除测试用户的手势
        delete_gesture_sql = "delete from ep_user_auth_info where user_id in (select id from ep_users where login_name = '" + CP().conf_loginName() + "')"
        self.mysql.sql_delete(delete_gesture_sql)
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
