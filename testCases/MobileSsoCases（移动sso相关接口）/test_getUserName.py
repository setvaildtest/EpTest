# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/26
@File : test_getUserName.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.JwtGet import get_jwt
import unittest
import time
from ep_common.ConfigPerson import ConfigPerson


class GetUserName(unittest.TestCase):

    def setUp(self):

        self.api_url = 'coding/v3/getUserName'
        self.url = conf_url() + self.api_url

    def get_encryptedstring(self):
        mysql = MySqlUtil()
        person = ConfigPerson()

        login_name = person.conf_loginName()
        mysql.cursor.execute("select id from ep_users where login_name='%s'" % login_name)
        user_id = mysql.cursor.fetchall()[0][0]
        app_id = 'epass_web'
        # 向数据库插入测试应用
        mysql.cursor.execute('select max(id) from ep_company_app')
        app_max_id = mysql.cursor.fetchall()[0][0]
        if app_max_id == None:
            company_app_id = 1
        else:
            company_app_id = app_max_id + 1
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql_insert_app = "INSERT INTO `ep_company_app` (`id`, `name`, `description`, `security_level_id`, `company_id`, `sort_name`, `create_time`, `update_time`, `create_user`, `update_user`, `type`, `app_id`, `sso_address`, `android_package_name`, `downdload_addr`, `download_type`, `app_icon`, `is_relay`)" \
                         "VALUES ('%s', 'pytestApp', '用于获取字符串接口测试APP', '2', '1', 'pytestApp', '%s', '%s', 'pytest', 'pytest', '0', '%s', 'pytestApp', 'pytestApp', '', 'app_market', NULL, '0')" % (
                             company_app_id, create_time, create_time, app_id)
        mysql.sql_insert(sql_insert_app)
        # 通过sql授权应用
        mysql.cursor.execute('select max(id) from ep_user_company_app')
        auth_max_id = mysql.cursor.fetchall()[0][0]
        if auth_max_id == None:
            auth_id = 1
        else:
            auth_id = auth_max_id + 1
        auth_sql = "insert into ep_user_company_app(id,user_id,company_id,company_app_id) values('%s','%s',1,'%s')" % (
            auth_id, user_id, company_app_id)
        mysql.sql_insert(auth_sql)

        api_url = 'coding/v3/getEncryptedStringByApp'
        url = conf_url() + api_url

        url = url
        data = {
            "appId": "epass_web",
            "jwt": get_jwt('jwt'),
            "subAccount": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        encryptedString = re['body']['encryptedString']
        print(encryptedString)
        return encryptedString

    def test_get_username_01(self):
        u"加密串正确，获取用户名请求成功"

        url = self.url
        data = {
            "device": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "encryptedString": self.get_encryptedstring()
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

    def test_get_username_02(self):
        u"加密串参数错误，获取用户名请求失败"

        url = self.url
        data = {
            "device": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "encryptedString": "112321233"
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '临时票据失效'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_username_03(self):
        u"加密串参数已过期，获取用户名请求失败"

        url = self.url
        data = {
            "device": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "encryptedString": "vNCxWOBNd8gpY+qcLgiZcOHqnnQQxAPgZE9Ncp5UKldj4scSdAiH44S+PxKk0ML0LwLwsYaU+ODyGf0F7o4O5omawi4S4USilo7uN1mjdWM="
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '解密失败，请重新登录'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_username_04(self):
        u"加密串参数为空，获取用户名请求失败"

        url = self.url
        data = {
            "device": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "encryptedString": ""
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '加密串不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_get_username_05(self):
        u"加密串参数为空串，获取用户名请求失败"

        url = self.url
        data = {
            "device": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "encryptedString": "         "
        }
        # sql = 'select * from ts_gesture_password'
        # data = sql_connect(sql,0,1)
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '加密串不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def tearDown(self):
        '''根据id清除测试所创数据'''
        self.mysql = MySqlUtil()
        self.mysql.sql_delete("delete from ep_user_company_app where company_app_id in (select id from ep_company_app where app_id='epass_web')")
        self.mysql.sql_delete("delete from ep_company_app where app_id='epass_web'")
        self.mysql.db_sql.close()



if __name__ == "__main__":
    unittest.main()