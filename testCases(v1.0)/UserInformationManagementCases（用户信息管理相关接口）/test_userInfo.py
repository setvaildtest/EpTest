# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui  更新：zhanaihua
@Time : 2019/8/21
@File : userInfo(获取用户信息).py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.SceneDecide import sceneDecide
from ep_common.JwtGet import *
from ep_common.ConfigPerson import ConfigPerson
import unittest


class UserInfo(unittest.TestCase):

	def setUp(self):

		self.api_url = 'coding/userInfo'
		self.url = conf_url() + self.api_url
		conf_person = ConfigPerson()
		self.login_name = conf_person.conf_loginName()

	def test_userinfo_01(self):
		u"jwt参数正确，请求成功"
		url = self.url
		data = {
			"jwt": get_jwt_v1('jwt'),
			"token": ""
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "操作成功"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message,msg=re['status'])

	def test_userinfo_02(self):
		u"jwt参数为空，请求失败"
		url = self.url
		data = {
			"jwt": "",
			"token": ""
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "用户名不能为空"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message, msg=re['status'])

	def test_userinfo_03(self):
		u"jwt参数错误，请求失败"
		url = self.url
		data = {
			"jwt": "eyJhbGciOiJIUzI1NiJ9.eyJlcHRva2VuIjoidG9rZW46MTU2OTMwNDQ3NTA4OSIsImFwcGlkIjoiZXBhc3NfYXBwIiwic3VidG9rZW4iOiIiLCJ1c2VyaWQiOiJjeGgiLCJpYXQiOiIyMDE5LTA5LTIzIDIyLjU0LjM1IiwidXBkdCI6IjIwMTktMDktMjMgMjIuNTQuMzUifQ.7yLzmqfyTV-5FarMNWbDgVSnZCygUNjII-zGUlWFmc41",
			"token": ""
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "JWT解析失败"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message, msg=re['status'])

	def test_userinfo_04(self):
		u"jwt参数过期，请求失败"
		url = self.url
		data = {
			"jwt": "eyJhbGciOiJIUzI1NiJ9.eyJlcHRva2VuIjoidG9rZW46MTU2OTMwNDQ3NTA4OSIsImFwcGlkIjoiZXBhc3NfYXBwIiwic3VidG9rZW4iOiIiLCJ1c2VyaWQiOiJjeGgiLCJpYXQiOiIyMDE5LTA5LTIzIDIyLjU0LjM1IiwidXBkdCI6IjIwMTktMDktMjMgMjIuNTQuMzUifQ.7yLzmqfyTV-5FarMNWbDgVSnZCygUNjII-zGUlWFmc4",
			"token": ""
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "令牌失效,请重新开启认证"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message, msg=re['status'])

	def test_userinfo_05(self):
		u"jwt和token参数都传递，请求失败"
		url = self.url
		data = {
			"jwt": get_jwt_v1('jwt'),
			"token": "11111"
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "参数不正确，第三方token和jwt同时存在，请仅使用其中一个"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message,msg=re['status'])


	def tearDown(self):
		pass

if __name__ == "__main__":
	unittest.main()