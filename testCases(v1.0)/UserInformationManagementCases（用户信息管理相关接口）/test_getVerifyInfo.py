# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/9/25
@File : test_getVerifyInfo.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import *
from ep_common.ConfigPerson import ConfigPerson
import unittest


class GetVerifyInfo(unittest.TestCase):

	def setUp(self):

		self.api_url = 'coding/userInfo'
		self.url = conf_url() + self.api_url
		conf_person = ConfigPerson()
		self.login_name = conf_person.conf_loginName()

	def test_get_VerifyInfo_01(self):
		u"jwt参数正确，请求成功"
		url = self.url
		data = {
            "u": ""
        }
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "操作成功"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message,msg=re['status'])