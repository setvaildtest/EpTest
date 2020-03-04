#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/26
@File : test_userSave.py
@describe : 测试鉴权2.0 bim融合-企业用户管理-用户创建接口

"""
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil
from ep_common.GenerateRandomStr import generate_random_str
from ep_common.ConfigPerson import ConfigPerson


class UserSave(unittest.TestCase):
    def setUp(self):
        api_url = "coding/service/admin/user/save"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        self.conf_user = ConfigPerson()

    def test_user_save_01(self):
        u'所有参数正确，请求成功'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [{'attr': 'apiTestAttr01', 'value': 'apiTestValue01'}],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "apiTestUser",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "攻城狮",
            "sex": "1"
        }

        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 查询数据库用户表和扩展属性表
        re_userId = re['body']['userId']
        self.mysql.cursor.execute("select count(*) from ep_users where id=%s" % re_userId)
        actual_user_count = self.mysql.cursor.fetchall()[0][0]
        self.mysql.cursor.execute(
            "select count(*) from ep_user_extends_attrs where user_id='%s'" % re_userId)
        actual_attr_count = self.mysql.cursor.fetchall()[0][0]
        # 删除接口测试创建的用户数据
        self.mysql.sql_delete("delete from ep_users where id=%s" % re_userId)
        self.mysql.sql_delete("delete from ep_user_extends_attrs where user_id='%s'" % re_userId)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 断言用户数据是否新增成功
        expect_user_count = 1  # 期望数据库查询到与新建用户数据匹配的记录数为1
        self.assertEqual(expect_user_count, actual_user_count)
        # 断言扩展属性表是否有对应的扩展属性
        expect_attr_count = 1
        self.assertEqual(expect_attr_count, actual_attr_count)

    def test_user_save_02(self):
        u'只传必填参数，请求成功'
        data = {
            "age": "",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应message
        print('响应：', re)
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 检查用户数据是否新增成功
        expect_user_count = 1  # 期望数据库查询到与新建用户数据匹配的记录数为1
        re_userId = re['body']['userId']
        self.mysql.cursor.execute("select count(*) from ep_users where id=%s " % re_userId)
        actual_user_count = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_user_count, actual_user_count)
        # 删除接口测试创建的用户数据
        self.mysql.sql_delete("delete from ep_users where id=%s" % re_userId)

    def test_user_save_03(self):
        u'登录名为空，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "登录名必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_04(self):
        u'用户姓名为空，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "用户姓名必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_05(self):
        u'用户密码为空，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "用户密码必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_06(self):
        u'手机号为空，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "手机号必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_07(self):
        u'企业id不存在，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 20190911,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "12000000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "所选企业无效"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_08(self):
        u'性别无效，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "12000000000",
            "position": "开发工程师",
            "sex": "notfound"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "性别无效，请检查数据字典相关配置"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_09(self):
        u'用户名已存在，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": self.conf_user.conf_loginName(),
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "用户名已存在"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_10(self):
        u'手机号已被注册，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": self.conf_user.conf_phone(),
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "手机已被注册"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_11(self):
        u'邮箱已被注册，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": self.conf_user.conf_email(),
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "邮箱已被注册"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_12(self):
        u'身份证已被使用，请求失败'
        # 通过sql创建用户和扩展属性，用于测试用户信息唯一性校验
        exist_user = {"login_name": "apiTestUser_sql", "password": "6B9A5A73D3D3E7D3DD8F4979029ADAD9",
                      "name": "sql创建的测试用户", "sex": "1", "age": "22", "birthday": "1997-01-01",
                      "phone": "12100000000", "email": "12100000000@163.com",
                      "id_card_number": "493849199401208900",
                      "position": "攻城狮", "department": "研发部", "company_id": 1, "extend_attrs": "",
                      "is_disabled": "0", "is_deleted": "0", "creator": "apiTest", "updator": "apiTest",
                      "pass_expire_date": "2030-02-22 17:05:03", "lock_expire_date": "1970-01-01 00:00:00",
                      "locked": "0"}
        ChildUserSqlUtil.insert_user(exist_user)
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": exist_user["id_card_number"],
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "身份证已被使用"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_save_13(self):
        u'extendsAttr属性非法,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [],
            "extendAttrs": "241356436851",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "extendsAttr属性非法"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_14(self):
        u'扩展属性attr为空,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [{'attr': '', 'value': 'value14'}],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "扩展属性attr不能为空"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_15(self):
        u'扩展属性attr包含除字母数字以及_-以外的字符,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [{'attr': 'apiTestAttr@123', 'value': 'apiTestValue15'}],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "扩展属性attr只能由字母数字以及_-组成"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_16(self):
        u'扩展属性attr长度超过50,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [{'attr': generate_random_str(51), 'value': 'apiTestValue16'}],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "扩展属性的attr或者value长度需在1-50之间"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_17(self):
        u'扩展属性value长度超过50,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [{'attr': 'apiTestAttr17', 'value': generate_random_str(51)}],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "扩展属性的attr或者value长度需在1-50之间"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_18(self):
        u'扩展属性的值已被使用,请求失败'
        self.mysql.cursor.execute("select id from ep_users where login_name='%s'" % self.conf_user.conf_loginName())
        conf_user_id = self.mysql.cursor.fetchone()[0]
        exist_attr_id, exist_attr, exist_attr_value = ChildUserSqlUtil.insert_extend_attr(str(conf_user_id))
        try:
            data = {
                "age": "23",
                "birthday": "1995-01-20",
                "companyId": 1,
                "department": "研发部",
                "email": "763149560@qq.com",
                "expandAttributes": [{'attr': 'apiTestAttr18', 'value': exist_attr_value}],
                "extendAttrs": "",
                "idCardNumber": "393849199401208900",
                "loginName": "apiTestUser",
                "name": "测试用户",
                "passExpireDate": "20220712235959",
                "password": "123456",
                "phone": "1200000000",
                "position": "开发工程师",
                "sex": "1"
            }
            data = jsonTostr(data)
            re = sceneDecide(self.url, data)
        except(Exception)as e:
            print(e)
        finally:
            # 删除测试扩展属性
            self.mysql.sql_delete("delete from ep_user_extends_attrs where id=%s" % exist_attr_id)
            print('响应', re)
            # 断言响应message
            expect_message = "扩展属性的值已被使用"
            actual_message = re['message']
            self.assertEqual(expect_message, actual_message)

    def test_save_user_19(self):
        u'扩展属性存在重复的attr,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [{'attr': 'apiTestAttr19', 'value': "apiTestValue19"},
                                 {'attr': 'apiTestAttr19', 'value': "apiTestValue191"}],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "扩展属性存在重复的attr"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_20(self):
        u'扩展属性存在重复的value,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "763149560@qq.com",
            "expandAttributes": [{'attr': 'apiTestAttr200', 'value': "apiTestValue200"},
                                 {'attr': 'apiTestAttr201', 'value': "apiTestValue200"}],
            "extendAttrs": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('响应：', re)
        # 断言响应message
        expect_message = "扩展属性存在重复的value."
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_21(self):
        u'用户账户登录名称长度超过45，请求失败'
        data = {
            "age": "",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": generate_random_str(46),
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应message
        print('响应：', re)
        expect_message = "用户账户登录名称长度不超过45;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_22(self):
        u'用户姓名长度超过45，请求失败'
        data = {
            "age": "",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": "apiTestuser",
            "name": generate_random_str(46),
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应message
        print('响应：', re)
        expect_message = "用户姓名长度不超过45;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_23(self):
        u'年龄字段长度超过3，请求失败'
        data = {
            "age": "1000",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": "apiTestuser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应message
        print('响应：', re)
        expect_message = "年龄字段长度不超过3;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_24(self):
        u'邮箱字段长度超过255，请求失败'
        data = {
            "age": "",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": generate_random_str(256),
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": "apiTestuser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "开发工程师",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应message
        print('响应：', re)
        expect_message = "邮箱字段长度不超过255;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_25(self):
        u'职位字段长度超过45，请求失败'
        data = {
            "age": "",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": "apiTestuser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": generate_random_str(46),
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应message
        print('响应：', re)
        expect_message = "职位字段长度不超过45;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_save_user_26(self):
        u'部门字段长度超过45，请求失败'
        data = {
            "age": "",
            "birthday": "",
            "companyId": 1,
            "department": generate_random_str(46),
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": "apiTestuser",
            "name": "测试用户",
            "passExpireDate": "20220712235959",
            "password": "123456",
            "phone": "1200000000",
            "position": "",
            "sex": "1"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应message
        print('响应：', re)
        expect_message = "部门字段长度不超过45;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def tearDown(self):
        u'清除测试数据'
        self.mysql.sql_delete("delete from ep_users where login_name like '%apiTest%'")  # 删除sql创建的测试用户
        self.mysql.sql_delete("delete from ep_user_extends_attrs where attr like'%apiTest%'")  # 删除sql创建的测试扩展属性
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
