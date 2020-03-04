# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/9/16
@File : authDoauth(统一认证接口).py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

from ep_common.ConfigServer import conf_url, conf_appid
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.ConfigPerson import ConfigPerson as CP
from ep_common.DoauthCheck import doauth_check
from ep_common.GenerateRandomStr import generate_random_str
from ep_common.RedisPhoneCode import redis_phone_code
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.RedisPhoneCode import set_bind_auto,set_bind_normal
import unittest
import time

appId = conf_appid()


class DoAuth(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/auth/doauth'
        self.url = conf_url() + self.api_url
        self.conf = MySqlUtil()

    def tearDown(self):
        pass

    def test_doauth_01(self):
        u'用户名作为登录名，正确的用户名密码，请求成功'
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "app",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": "vivo X9L",
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_02(self):
        u'手机号码作为登录名，正确的号码密码，请求成功'
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_phone(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "app",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": "vivo X9L",
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_03(self):
        u'邮箱作为登录名，正确的邮箱密码，请求成功'
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": '123@qq.com',
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "app",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": "vivo X9L",
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_04(self):
        u'用户名为空，请求失败'
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": '',
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "app",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": "vivo X9L",
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '认证失败，缺少参数'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_05(self):
        u'密码为空，请求失败'
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": 'wangjing',
                "password": ""
            },
            "authType": "pwd",
            "device": "app",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": "vivo X9L",
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '认证失败，缺少参数'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_06(self):
        u'密码错误，认证失败'
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": "123457"
            },
            "authType": "pwd",
            "device": "app",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": "vivo X9L",
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '账号或密码错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_07(self):
        u'认证设备指纹参数错误，长度限制255位'
        DeviceFingerPrint = generate_random_str(256)
        print(DeviceFingerPrint)
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "app",
            "deviceFingerprint": DeviceFingerPrint,
            "epsessionId": "",
            "hostname": "vivo X9L",
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '认证设备指纹参数错误，长度限制255位'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    @unittest.skip
    def test_doauth_08(self):
        u'认证设备主机名参数错误，长度限制50位'
        # todo 后端没有校验，确认后修改
        HostName = generate_random_str(55)
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "app",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": HostName,
            "requestType": "1"
        }
        print(data)
        print('hostname:', data['hostname'])
        print('字符串统计：', len(data['hostname']))
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '认证设备主机名参数错误，长度限制50位'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_09(self):
        u'参数错误:设备类型不能为空'
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": 'iphone7',
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '参数错误:设备类型不能为空;'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_10(self):
        u'认证设备参数错误'
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "123",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": 'iphone7',
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '认证设备参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_11(self):
        u'没有应用正在等待人脸认证'
        data = {
            "appId": appId,
            "authPara": {
                "userInfo": {
                    "userId": "wangjing",
                    "loginName": "wangjing",
                    "email": "123@qq.com",
                    "mobileNum": "15680665321"
                },
                "modelid": "1",
                "macAddress": ""
            },
            "authType": "pwd",
            "device": "123",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": 'iphone7',
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '没有应用正在等待人脸认证'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    @unittest.skip('返回信息需要确认，需要后期配置二级认证')
    def test_doauth_12(self):
        u'认证会话状态错误, 认证可能已经超时或者超过错误限制, 建议重新开启认证'
        # todo 需要后期配置二级认证
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "web",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": 'iphone7',
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '认证设备参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    @unittest.skip('返回信息需要确认，需要后期配置二级认证')
    def test_doauth_13(self):
        u'认证超时, 请在{0}分钟内完成本次认证挑战, 3秒后将跳转到登录页'
        # todo 这个返回信息需要确认，需要后期配置二级认证
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "web",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": 'iphone7',
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '认证设备参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    @unittest.skip('返回信息需要确认，需要后期配置二级认证')
    def test_doauth_14(self):
        u'非常用设备登录，请选择信任设备类型进行设备绑定'
        # todo 这个返回信息需要确认，需要后期配置二级认证
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "web",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": 'iphone7',
            "requestType": "3"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        expect_status = '认证设备参数错误'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def test_doauth_15(self):
        u'非常用设备登录，请根据提示进行增强认证完成绑定设备'
        set_bind_auto()
        # sql = "UPDATE ep_sys_config set `value` = 'auto' WHERE `code` = 'system.userDevices.boundMode'"
        # self.conf.sql_update(sql)
        data = {
            "appId": appId,
            "authPara": {
                "loginName": CP().conf_loginName(),
                "password": CP().conf_password()
            },
            "authType": "pwd",
            "device": "app",
            "deviceFingerprint": "D74A9F68-ADF3-4237-BAC5-DFEE3817ADEF",
            "epsessionId": "",
            "hostname": 'iPhone 7',
            "requestType": "1"
        }
        data = jsonTostr(data)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = '非常用设备登录，请根据提示进行增强认证完成绑定设备'
        actual_status = re['message']
        set_bind_normal()
        # sql = "UPDATE ep_sys_config set `value` = 'normal' WHERE `code` = 'system.userDevices.boundMode'"
        # self.conf.sql_update(sql)
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def phone_code(self):
        self.api_url = 'coding/login/sendSMS'
        self.url = conf_url() + self.api_url
        data = {
            "mobile": CP().conf_phone(),
            "templateType": "sms.send.resetpwd.template"
        }
        data = jsonTostr(data)
        print('手机验证码data==========>', data)
        print('url===========>', self.url)
        re = sceneDecide(self.url, data=data)
        print(re)

    def test_doauth_16(self):
        u'短信认证，认证成功'
        self.phone_code()
        self.api_url = 'coding/auth/doauth'
        self.url = conf_url() + self.api_url
        data = {
            "appId": appId,
            "authPara": {
                "deviceBindType": "",
                "mobileNum": CP().conf_phone(),
                "smsCode": str(redis_phone_code())
            },
            "authType": "sms",
            "device": "web",
            "deviceFingerprint": "ce153e7c-f002-33f0-b639-846546b1fd8f",
            "epsessionId": "",
            "hostname": "vivo X9L",
            "requestType": "1"
        }
        print('短信认证data', data)
        print('====================>', self.url)
        data = jsonTostr(data)
        time.sleep(2)
        re = doauth_check(self.url, data)
        print(re)
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')


if __name__ == "__main__":
    unittest.main()
    # t = DoAuth()
    # t.test_doauth_15()
