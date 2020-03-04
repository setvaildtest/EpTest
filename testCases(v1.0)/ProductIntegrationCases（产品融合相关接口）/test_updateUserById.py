#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/9/23
@File : test_updateUserById.py
@describe : 鉴权1.0BIM融合 - 企业用户管理 - 根据物理ID更新用户

"""
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil
from ep_common.GenerateRandomStr import generate_random_str
from ep_common.ConfigPerson import ConfigPerson


class UserUpdateById(unittest.TestCase):
    def setUp(self):
        api = "coding/userInfo/updateById"
        self.url = conf_url() + api
        self.mysql = MySqlUtil()
        self.conf_user = ConfigPerson()
        # 通过sql创建测试用户及其扩展属性用于更新
        self.user_id_list, self.login_name_list = ChildUserSqlUtil.insert_users(1, '0')
        self.test_user_id = self.user_id_list[0]
        self.attr_id, self.attr, self.attr_value = ChildUserSqlUtil.insert_extend_attr(self.test_user_id)

    def test_user_update_by_id_01(self):
        u'根据ID修改用户信息(登录名、姓名、性别、年龄、手机号、邮箱)，请求成功'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "po": {
                "age": "",
                "birthday": "",
                "companyId": 0,
                "companyName": "",
                "createTime": "",
                "creator": "",
                "department": "",
                "email": "",
                "expandAttributes": [
                    {
                        "attr": "age",
                        "deleted": "",
                        "id": 0,
                        "userId": 0,
                        "value": 123
                    }
                ],
                "expireTime": "",
                "extendAttrs": "",
                "faceModelId": "",
                "gestureData": "",
                "id": 0,
                "idCardNumber": "",
                "isDeleted": "",
                "isDisabled": "",
                "lockExpireDate": "",
                "locked": "",
                "loginName": "",
                "name": "",
                "otpKey": "",
                "password": "",
                "phone": "",
                "position": "",
                "sex": "",
                "updateTime": "",
                "updator": "",
                "voiceModelId": ""
            },
            "position": "开发工程师",
            "sex": "0"
        }
        expect_data = (
            data["loginName"], data["name"], data["sex"], data["age"], data["phone"], data["email"])  # 用于断言修改后的数据
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "操作成功"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)
        # 断言响应数据
        query_new_user = "select login_name,name,sex,age,phone,email from ep_users where id=%s" % self.test_user_id
        self.mysql.cursor.execute(query_new_user)
        actual_data = self.mysql.cursor.fetchall()[0]
        self.assertEqual(expect_data, actual_data)

    def test_user_update_by_id_02(self):
        u'登录名为空，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "登录名必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_03(self):
        u'性别为空，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "性别 必填请根据数据字典值进行配置;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_04(self):
        u'手机号为空，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "手机号 必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_05(self):
        u'公司id为空，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": "",
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "公司ID必填;"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_06(self):
        u'用户id为空，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": "",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "用户物理不能为空;"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_07(self):
        u'用户不存在，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": "0",
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "该用户不存在"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_08(self):
        u'用户名已存在，请求失败'
        cp = ConfigPerson()
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": cp.conf_loginName(),
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "用户名已存在"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_09(self):
        u'性别无效，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "a"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "性别无效，请检查数据字典相关配置"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_10(self):
        u'所选企业无效，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 9,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "所选企业无效"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_11(self):
        u'手机已被注册，请求失败'
        exist_phone = self.conf_user.conf_phone()
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": exist_phone,
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "手机已被注册"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_12(self):
        u'邮箱已被注册，请求失败'
        exist_email = self.conf_user.conf_email()
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": exist_email,
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "邮箱已被注册"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_13(self):
        u'身份证已被使用，请求失败'
        exist_id_card = '12345678'
        self.mysql.sql_update(
            "update ep_users set id_card_number='%s' where login_name='%s'" % (
                exist_id_card, self.conf_user.conf_loginName))
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": exist_id_card,
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "身份证已被使用"
        actual_message = re["message"]
        self.assertEqual(expect_message, actual_message)

    def test_user_update_by_id_14(self):
        u'登录名超长，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": generate_random_str(46),
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "登录名长度超长"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_15(self):
        u'姓名超长，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": generate_random_str(46),
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "姓名长度超长"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_16(self):
        u'年龄字段超长，请求失败'
        data = {
            "age": "1000",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "年龄字段超长"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_17(self):
        u'身份证长度超长，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": generate_random_str(101),
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "开发工程师",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "身份证长度超长"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_18(self):
        u'职位字段长度超长，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": generate_random_str(46),
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "职位字段长度超长"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_19(self):
        u'部门字段长度超长，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": generate_random_str(46),
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "部门字段长度超长"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_20(self):
        u'扩展属性参数格式错误，请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": "",
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "参数错误"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_21(self):
        u'新增扩展属性，请求成功'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "pyTestAttr", "value": "pyTestValue"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        new_attr = data["expandAttributes"][0]["attr"]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "操作成功"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)
        # 检查扩展属性是否新增成功
        expect_data = 1
        self.mysql.cursor.execute("select count(*) from ep_user_extends_attrs where user_id='%s' and attr='%s'" % (
            self.test_user_id, new_attr))
        actual_data = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_data, actual_data)

    def test_user_update_by_id_22(self):
        u'新增扩展属性attr为空，请求成功'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "", "value": "pyTestValue"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "扩展属性attr不能为空"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_23(self):
        u'扩展属性attr,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "pyTestAttr@123", "value": "pyTestValue"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "扩展属性attr只能由字母数字以及_-组成"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_24(self):
        u'扩展属性的attr超长,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": generate_random_str(51), "value": "pyTestValue"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "扩展属性的attr或者value长度需在1-50之间"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_25(self):
        u'扩展属性的value超长,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "pyTestAttr", "value": generate_random_str(51)}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "扩展属性的attr或者value长度需在1-50之间"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_26(self):
        u'扩展属性的value超长,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "pyTestAttr", "value": generate_random_str(51)}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应消息
        expect_message = "扩展属性的attr或者value长度需在1-50之间"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_27(self):
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
                "email": "19100000000@123.com",
                "expandAttributes": [{"attr": self.attr, "value": exist_attr_value}],
                "extendAttrs": "",
                "id": str(self.test_user_id),
                "idCardNumber": "393849199401208900",
                "loginName": "apiTestUser_updateById",
                "name": "apiTestUser_updateById",
                "phone": "19100000000",
                "position": "研发",
                "sex": "0"
            }
            data = jsonTostr(data)
            re = sceneDecide(self.url, data)
        except(Exception) as e:
            print(e)
        finally:
            self.mysql.sql_delete("delete from ep_user_extends_attrs where id=%s" % exist_attr_id)  # 删除测试扩展属性
            # 断言响应消息
            print('用户更新接口入参：=================>\n', data)
            print('用户更新接口响应：=================>\n', re)
            expect_message = "扩展属性的值已被使用"
            actual_message = re["message"]
            self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_28(self):
        u'扩展属性存在重复的attr,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "apiTestAttr28", "value": "apiTestValue280"},
                                 {"attr": "apiTestAttr28", "value": "apiTestValue281"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应消息
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        expect_message = "扩展属性存在重复的attr"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_29(self):
        u'扩展属性存在重复的value,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "apiTestAttr290", "value": "apiTestValue29"},
                                 {"attr": "apiTestAttr291", "value": "apiTestValue29"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应消息
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        expect_message = "扩展属性存在重复的value"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_30(self):
        u'扩展属性的值在新增时为空,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "apiTestAttr30", "value": ""}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        extend_attr = data["expandAttributes"][0]["attr"]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应消息
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        expect_message = "扩展属性" + extend_attr + "的值，在新增时不能为空或NULL值"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_31(self):
        u'扩展属性的值在新增时为null,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "apiTestAttr30", "value": "null"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        extend_attr = data["expandAttributes"][0]["attr"]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应消息
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        expect_message = "扩展属性" + extend_attr + "的值，在新增时不能为空或NULL值"
        actual_message = re["message"]
        self.assertIn(expect_message, actual_message)

    def test_user_update_by_id_32(self):
        u'新增扩展属性,请求成功'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": "apiTestAttr32", "value": "apiTestValue32"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        new_attr = data["expandAttributes"][0]["attr"]
        new_attr_value = data["expandAttributes"][0]["value"]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应消息
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 检查扩展属性值是否新增成功
        expect_data = 1
        self.mysql.cursor.execute(
            "select count(*) from ep_user_extends_attrs where user_id='%s'and attr='%s' and value='%s'" % (
                self.test_user_id, new_attr, new_attr_value))
        actual_data = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_data, actual_data)

    def test_user_update_by_id_33(self):
        u'修改扩展属性的值,请求成功'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": self.attr, "value": "apiTestValue33"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        new_attr_value = data["expandAttributes"][0]["value"]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应消息
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 检查扩展属性值是否修改成功
        expect_data = new_attr_value
        self.mysql.cursor.execute(
            "select value from ep_user_extends_attrs where id=%s and attr='%s'" % (
                self.attr_id, self.attr))
        actual_data = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_data, actual_data)

    def test_user_update_by_id_34(self):
        u'删除扩展属性,请求成功'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [{"attr": self.attr, "value": "null"}],
            "extendAttrs": "",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应消息
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 检查扩展属性是否被删除
        expect_data = "1"
        self.mysql.cursor.execute(
            "select deleted from ep_user_extends_attrs where id=%s and user_id='%s'" % (
                self.attr_id, self.test_user_id))
        actual_data = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_data, actual_data)

    def test_user_update_by_id_35(self):
        u'extendsAttr属性非法,请求失败'
        data = {
            "age": "23",
            "birthday": "1995-01-20",
            "companyId": 1,
            "department": "研发部",
            "email": "19100000000@123.com",
            "expandAttributes": [],
            "extendAttrs": "apiTestExtendAttrs",
            "id": str(self.test_user_id),
            "idCardNumber": "393849199401208900",
            "loginName": "apiTestUser_updateById",
            "name": "apiTestUser_updateById",
            "phone": "19100000000",
            "position": "研发",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        # 断言响应消息
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "extendsAttr属性非法"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def tearDown(self):
        # 删除sql创建的测试用户及其扩展属性
        self.mysql.sql_delete("delete from ep_user_extends_attrs where user_id='%s'" % str(self.test_user_id))
        self.mysql.sql_delete("delete from ep_users where id=%s" % self.test_user_id)
        self.mysql.db_sql.close()


if __name__ == "__main__":
    unittest.main()
