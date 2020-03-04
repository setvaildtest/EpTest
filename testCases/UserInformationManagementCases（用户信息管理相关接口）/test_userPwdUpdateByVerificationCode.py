# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/21
@File : userPwdUpdateByVerificationCode(忘记密码-设置新密码).py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.VerCode import sendcode
from ep_common.RedisPhoneCode import redis_phone_code
from ep_common.ConfigPerson import ConfigPerson as CP
import unittest
import os



class UpdatePwdByCode(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/v3/user/userPwdUpdateByVerificationCode'
        self.url = conf_url() + self.api_url
        self.new_passwd = 'cxh123456'


    def test_update_pwd_code_01(self):
        u"手机号、验证码和新密码正确，通过验证码修改密码请求成功"
        sendcode()
        url = self.url
        data = {
            "newPassword": self.new_passwd,
            "phone": CP().conf_phone(),
            "verificationCode": redis_phone_code()
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(actual_status, expect_status, msg=re['status'])

    def test_update_pwd_code_02(self):
        u"手机号输入为空，通过验证码修改密码请求失败"
        sendcode()
        url = self.url
        data = {
            "newPassword": self.new_passwd,
            "phone": "",
            "verificationCode": redis_phone_code()
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_pwd_code_03(self):
        u"手机号输入空串，通过验证码修改密码请求失败"
        sendcode()
        url = self.url
        data = {
            "newPassword": self.new_passwd,
            "phone": "    ",
            "verificationCode": redis_phone_code()
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '没有找到此用户'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_pwd_code_04(self):
        u"手机号输入不合法，通过验证码修改密码请求失败"
        sendcode()
        url = self.url
        data = {
            "newPassword": self.new_passwd,
            "phone": "1323232",
            "verificationCode": redis_phone_code()
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '没有找到此用户'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_pwd_code_05(self):
        u"手机号用户不存在，通过验证码修改密码请求失败"
        sendcode()
        url = self.url
        data = {
            "newPassword": self.new_passwd,
            "phone": "13458530499",
            "verificationCode": redis_phone_code()
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '没有找到此用户'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_pwd_code_06(self):
        u"验证码输入错误，通过验证码修改密码请求失败"
        url = self.url
        data = {
            "newPassword": self.new_passwd,
            "phone": CP().conf_phone(),
            "verificationCode": "123"
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '您的验证码不正确'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_pwd_code_07(self):
        u"验证码输入为空，通过验证码修改密码请求失败"
        url = self.url
        data = {
            "newPassword": self.new_passwd,
            "phone": CP().conf_phone(),
            "verificationCode": ""
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_pwd_code_08(self):
        u"验证码输入为空串，通过验证码修改密码请求失败"
        url = self.url
        data = {
            "newPassword": self.new_passwd,
            "phone": CP().conf_phone(),
            "verificationCode": "    "
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '您的验证码不正确'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_pwd_code_09(self):
        u"新密码为空，通过验证码修改密码请求失败"
        sendcode()
        url = self.url
        data = {
            "newPassword": "",
            "phone": CP().conf_phone(),
            "verificationCode": redis_phone_code()
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])

    def test_update_pwd_code_10(self):
        u"新密码为空串，通过验证码修改密码请求失败"
        sendcode()
        url = self.url
        data = {
            "newPassword": "   ",
            "phone": CP().conf_phone(),
            "verificationCode": redis_phone_code()
        }
        data = jsonTostr(data)
        print('通过sql获取到的data：', data)
        print('数据类型：', type(data))
        re = sceneDecide(url, data)
        print(re)
        expect_status = '参数错误;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg=re['status'])


    def tearDown(self):
        cp = CP()
        cp.conf_write_passwd(self.new_passwd)
        # 清空jwt_data中的jwt，避免会话失效的情况
        file_path = os.path.dirname(__file__)  # 获取当前目录
        parent_path = os.path.dirname(file_path)  # 获得当前所在目录的父级目录
        jwt_data_path = os.path.dirname(parent_path) + '\\ep_config\\jwt_data'
        open(jwt_data_path, "w").close()

if __name__ == '__main__':
    unittest.main()
