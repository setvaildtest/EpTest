# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/9/24
@File : test_updateIdAuthInfo.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import *
from ep_common.ConfigPerson import ConfigPerson
import unittest
from ep_common.ConfigPerson import ConfigPerson as CP


class UpdateIdAuthInfo(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/userInfo/updateIdAuthInfo'
        self.url = conf_url() + self.api_url
        conf_person = ConfigPerson()
        self.login_name = conf_person.conf_loginName()

    def test_update_IdAuthInfo_01(self):
        u"用户名参数正确，请求成功"
        url = self.url
        data = {
            "age": "24",
            "birthday": "1997-01-01",
            "idCardAddress": "四川省",
            "idCardAuthority": "南充市公安局",
            "idCardBack": "",
            "idCardFront": "",
            "idCardNumber": "493849199401208900",
            "idCardValidDate": "",
            "loginName": CP().conf_loginName(),
            "name": "陈晓慧",
            "nation": "中国",
            "sex": "0",
            "userId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "操作成功"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])


    def test_update_IdAuthInfo_02(self):
        u"年龄参数为空，请求失败"
        url = self.url
        data = {
            "age": "",
            "birthday": "1997-01-01",
            "idCardAddress": "四川省",
            "idCardAuthority": "南充市公安局",
            "idCardBack": "",
            "idCardFront": "",
            "idCardNumber": "493849199401208900",
            "idCardValidDate": "",
            "loginName": CP().conf_loginName(),
            "name": "陈晓慧",
            "nation": "中国",
            "sex": "0",
            "userId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "年龄必须是两位到三位数字;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message,msg=re['status'])


    def test_update_IdAuthInfo_03(self):
        u"年龄参数为空串，请求失败"
        url = self.url
        data = {
            "age": "",
            "birthday": "1997-01-01",
            "idCardAddress": "四川省",
            "idCardAuthority": "南充市公安局",
            "idCardBack": "",
            "idCardFront": "",
            "idCardNumber": "493849199401208900",
            "idCardValidDate": "",
            "loginName": CP().conf_loginName(),
            "name": "陈晓慧",
            "nation": "中国",
            "sex": "0",
            "userId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "年龄必须是两位到三位数字;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def test_update_IdAuthInfo_04(self):
        u"年龄参数错误，请求失败"
        #todo 验证缺陷
        url = self.url
        data = {
            "age": "122",
            "birthday": "1997-01-01",
            "idCardAddress": "四川省",
            "idCardAuthority": "南充市公安局",
            "idCardBack": "",
            "idCardFront": "",
            "idCardNumber": "493849199401208900",
            "idCardValidDate": "",
            "loginName": CP().conf_loginName(),
            "name": "陈晓慧",
            "nation": "中国",
            "sex": "0",
            "userId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "年龄必须是两位到三位数字;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def test_update_IdAuthInfo_05(self):
        u"用户名参数为空，请求失败"
        url = self.url
        data = {
            "age": "122",
            "birthday": "1997-01-01",
            "idCardAddress": "四川省",
            "idCardAuthority": "南充市公安局",
            "idCardBack": "",
            "idCardFront": "",
            "idCardNumber": "493849199401208900",
            "idCardValidDate": "",
            "loginName": "",
            "name": "陈晓慧",
            "nation": "中国",
            "sex": "0",
            "userId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "用户名不能为空;"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def test_update_IdAuthInfo_06(self):
        u"用户名参数为空串，请求失败"
        url = self.url
        data = {
            "age": "122",
            "birthday": "1997-01-01",
            "idCardAddress": "四川省",
            "idCardAuthority": "南充市公安局",
            "idCardBack": "",
            "idCardFront": "",
            "idCardNumber": "493849199401208900",
            "idCardValidDate": "",
            "loginName": "   ",
            "name": "陈晓慧",
            "nation": "中国",
            "sex": "0",
            "userId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "该用户不存在"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def test_update_IdAuthInfo_07(self):
        u"用户名参数不存在，请求失败"
        url = self.url
        data = {
            "age": "122",
            "birthday": "1997-01-01",
            "idCardAddress": "四川省",
            "idCardAuthority": "南充市公安局",
            "idCardBack": "",
            "idCardFront": "",
            "idCardNumber": "493849199401208900",
            "idCardValidDate": "",
            "loginName": "cxh12121",
            "name": "陈晓慧",
            "nation": "中国",
            "sex": "0",
            "userId": "2"
        }
        data = jsonTostr(data)
        print('data：', data)
        re = sceneDecide(url, data)
        print('re：', re)
        # 断言响应消息
        expect_message = "该用户不存在"
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message, msg=re['status'])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()