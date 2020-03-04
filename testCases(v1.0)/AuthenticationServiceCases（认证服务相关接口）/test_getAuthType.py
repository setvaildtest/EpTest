# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/9/16 0016
@File : test_getAuthType.py
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
from ep_common.RedisPhoneCode import set_bind_auto, set_bind_normal
import unittest
import time


class GetAuthType(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/auth/getAuthType'
        self.url = conf_url() + self.api_url

    def tearDown(self):
        pass

    def test_get_auth_type_01(self):
        u'通过企业应用id获取该应用的认证列表'
        data = {
            "appId": "epass"
        }
        re = sceneDecide(self.url, data, 'get')
        expect_status = 'success'
        actual_status = re['status']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')


if __name__ == '__main__':
    unittest.main()
