# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/9/24
@File : test_unbindIdAuthInfo.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import *
from ep_common.ConfigPerson import ConfigPerson
import unittest
from ep_common.ConfigPerson import ConfigPerson as CP


class UnbindIdAuthInfo(unittest.TestCase):

	def setUp(self):

		self.api_url = 'coding/userInfo/unbindIdAuthInfo'
		self.url = conf_url() + self.api_url
		conf_person = ConfigPerson()
		self.login_name = conf_person.conf_loginName()

	def test_unbind_IdAuthInfo_01(self):
		u"用户名参数正确，请求成功"
		url = self.url
		data = {
			"loginName": CP().conf_loginName()
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "操作成功"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message,msg=re['status'])

	def test_unbind_IdAuthInfo_02(self):
		u"用户名参数为空，请求失败"
		url = self.url
		data = {
			"loginName": ""
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "用户名不能为空;"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message, msg=re['status'])

	def test_unbind_IdAuthInfo_03(self):
		u"用户名参数为空串，请求失败"
		url = self.url
		data = {
			"loginName": "    "
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "该用户不存在"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message, msg=re['status'])

	def test_unbind_IdAuthInfo_04(self):
		u"用户名参数为不存在，请求失败"
		url = self.url
		data = {
			"loginName": "cxh212121"
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