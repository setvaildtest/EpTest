#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/26
@File : test_userUpdate.py
@describe : 该模块用于测试鉴权2.0 bim融合-企业用户管理-根据登录名更新用户

"""
import time
import unittest
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.child_user_sql import ChildUserSqlUtil
from ep_common.GenerateRandomStr import generate_random_str
from ep_common.ConfigPerson import ConfigPerson


class UserUpdate(unittest.TestCase):
    def setUp(self):
        api_url = "coding/service/admin/user/update"
        self.url = conf_url() + api_url
        self.mysql = MySqlUtil()
        self.conf_user=ConfigPerson()
        # 通过sql创建测试用户及其扩展属性用于更新
        self.user_id_list, self.login_name_list = ChildUserSqlUtil.insert_users(1, '0')
        self.attr_id,self.attr,self.attr_value=ChildUserSqlUtil.insert_extend_attr(self.user_id_list[0])

    def test_user_update_01(self):
        u'修改用户的姓名、手机号、性别、电话号码，请求成功'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        expect_data = (data["name"], data["phone"], data["sex"], data["age"])  # 用于断言修改后的数据
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应code
        actual_code = re['code']
        expect_code = "info.common.success"
        self.assertEqual(expect_code, actual_code)
        # 断言响应状态
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status)
        # 断言响应数据
        query_new_user = "select name,phone,sex,age from ep_users where login_name='%s'" % self.login_name_list[0]
        self.mysql.cursor.execute(query_new_user)
        actual_data = self.mysql.cursor.fetchall()[0]
        self.assertEqual(expect_data, actual_data)

    def test_user_update_02(self):
        u'登录名为空，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": "",
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
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

    def test_user_update_03(self):
        u'姓名为空，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "姓名必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_04(self):
        u'性别为空，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": ""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "性别必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_05(self):
        u'手机号为空，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "手机号必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_06(self):
        u'所属企业ID为空，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": "",
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "公司ID必填;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_07(self):
        u'用户不存在，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": "notfoundUser",
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "该用户不存在"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_08(self):
        u'所属企业ID不存在，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 6,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "所选企业无效"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_09(self):
        u'性别无效，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "无"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "性别无效，请检查数据字典相关配置"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_10(self):
        u'手机号已被注册，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": self.conf_user.conf_phone(),
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "手机已被注册"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_11(self):
        u'邮箱已被注册，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": self.conf_user.conf_email(),
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "邮箱已被注册"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_12(self):
        u'身份证已被使用，请求失败'
        exist_id_card='12345678'
        self.mysql.sql_update("update ep_users set id_card_number='%s' where login_name='%s'" % (exist_id_card,self.conf_user.conf_loginName()))
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": exist_id_card,
            "loginName":self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "身份证已被使用"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_13(self):
        u'extendsAttr属性非法，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "附加属性",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "extendsAttr属性非法"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_14(self):
        u'姓名长度超长，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": generate_random_str(46),
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "姓名长度超长;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_15(self):
        u'年龄字段超长，请求失败'
        data = {
            "age": "1000",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "年龄字段超长;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_16(self):
        u'邮箱字段超长，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": generate_random_str(256),
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "邮箱字段长度超长;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_17(self):
        u'身份证长度超长，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": generate_random_str(101),
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "身份证长度超长;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_18(self):
        u'职位字段长度超长，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": generate_random_str(46),
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "职位字段长度超长;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_19(self):
        u'部门字段长度超长，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": generate_random_str(46),
            "email": "",
            "expandAttributes": [],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "部门字段长度超长;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_20(self):
        u'扩展属性attr为空，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{'attr': '', 'value': "apiTestValue20"}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "扩展属性attr不能为空"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_21(self):
        u'扩展属性attr包含除字母数字以及_-以外的字符,请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{'attr': 'apiTestAttr%123', 'value': "apiTestValue21"}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "扩展属性attr只能由字母数字以及_-组成"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_22(self):
        u'扩展属性attr超过50个字符,请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{'attr': generate_random_str(51), 'value': "apiTestValue22"}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "扩展属性的attr或者value长度需在1-50之间"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_23(self):
        u'扩展属性value超过50个字符,请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{'attr': self.attr, 'value': generate_random_str(51)}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "扩展属性的attr或者value长度需在1-50之间"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_24(self):
        u'扩展属性的值已被使用,请求失败'
        self.mysql.cursor.execute("select id from ep_users where login_name='%s'" % self.conf_user.conf_loginName())
        conf_user_id = self.mysql.cursor.fetchone()[0]
        exist_attr_id,exist_attr,exist_attr_value=ChildUserSqlUtil.insert_extend_attr(str(conf_user_id))
        try:
            data = {
                "age": "23",
                "birthday": "",
                "companyId": 1,
                "department": "",
                "email": "",
                "expandAttributes": [{'attr': self.attr, 'value': exist_attr_value}],
                "extendAttrs": "",
                "idCardNumber": "",
                "loginName": self.login_name_list[0],
                "name": "apiTestUser_update",
                "phone": "12100000001",
                "position": "",
                "sex": "0"
            }
            data = jsonTostr(data)
            re = sceneDecide(self.url, data)
        except(Exception) as e:
            print(e)
        finally:
            #删除测试扩展属性
            self.mysql.sql_delete("delete from ep_user_extends_attrs where id=%s"%exist_attr_id)
            print('用户更新接口入参：=================>\n', data)
            print('用户更新接口响应：=================>\n', re)
            # 断言响应message
            expect_message = "扩展属性的值已被使用"
            actual_message = re['message']
            self.assertEqual(expect_message, actual_message)

    def test_user_update_25(self):
        u'新增扩展属性时存在重复的attr，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{"attr": "apiTestAttr25", "value": "apiTestValue25"},
                                 {"attr": "apiTestAttr25", "value": "apiTestValue251"}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "扩展属性存在重复的attr"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_26(self):
        u'新增扩展属性时存在重复的value，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{"attr": "apiTestAttr25", "value": "apiTestValue25"},
                                 {"attr": "apiTestAttr26", "value": "apiTestValue25"}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "扩展属性存在重复的value."
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_27(self):
        u'新增扩展属性，请求成功'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{"attr": "apiTestAttr27", "value": "apiTestValue27"}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        new_attr = data["expandAttributes"][0]["attr"]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)
        # 检查扩展属性是否新增成功
        expect_data = 1
        self.mysql.cursor.execute(
            "select count(*) from ep_user_extends_attrs where user_id='%s' and attr='%s'" % (
                self.user_id_list[0], new_attr))
        actual_data = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_data, actual_data)
        # 删除新增的扩展属性
        self.mysql.sql_delete(
            "delete from ep_user_extends_attrs where user_id='%s' and attr='%s'" % (self.user_id_list[0], new_attr))

    def test_user_update_28(self):
        u'新增扩展属性时value为空，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{"attr": "apiTestAttr28", "value": ""}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        extend_attr = data["expandAttributes"][0]["attr"]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "扩展属性" + extend_attr + "的值，在新增时不能为空或NULL值"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_29(self):
        u'新增扩展属性时value为null，请求失败'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{"attr": "apiTestAttr29", "value": "null"}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        extend_attr = data["expandAttributes"][0]["attr"]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('用户更新接口入参：=================>\n', data)
        print('用户更新接口响应：=================>\n', re)
        # 断言响应message
        expect_message = "扩展属性" + extend_attr + "的值，在新增时不能为空或NULL值"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)

    def test_user_update_30(self):
        u'修改扩展属性值，请求成功'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{"attr": self.attr, "value": "apiTestValue30"}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        new_attr_value = data["expandAttributes"][0]["value"]
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
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

    def test_user_update_31(self):
        u'删除扩展属性：设置扩展属性值为null，请求成功'
        data = {
            "age": "23",
            "birthday": "",
            "companyId": 1,
            "department": "",
            "email": "",
            "expandAttributes": [{"attr": self.attr, "value": "null"}],
            "extendAttrs": "",
            "idCardNumber": "",
            "loginName": self.login_name_list[0],
            "name": "apiTestUser_update",
            "phone": "12100000001",
            "position": "",
            "sex": "0"
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
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
                self.attr_id, self.user_id_list[0]))
        actual_data = self.mysql.cursor.fetchall()[0][0]
        self.assertEqual(expect_data, actual_data)

    def tearDown(self):
        # 删除sql创建的测试用户及其扩展属性
        self.mysql.sql_delete("delete from ep_user_extends_attrs where user_id='%s'" % str(self.user_id_list[0]))
        self.mysql.sql_delete("delete from ep_users where id=%s" % self.user_id_list[0])
        self.mysql.db_sql.close()

if __name__ == "__main__":
    unittest.main()
