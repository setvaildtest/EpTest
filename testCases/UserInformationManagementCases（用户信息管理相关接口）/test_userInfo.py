# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui  更新：zhanaihua
@Time : 2019/8/21
@File : userInfo(获取用户信息).py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.DoauthCheck import doauth_check
from ep_common.ConfigPerson import ConfigPerson
import unittest


class UserInfo(unittest.TestCase):

	def setUp(self):

		self.api_url = 'coding/v3/user/userInfo'
		self.url = conf_url() + self.api_url
		conf_person = ConfigPerson()
		self.login_name = conf_person.conf_loginName()

	def test_userinfo_01(self):
		u"选择强刷取用户信息内容，请求成功"
		url = self.url
		data = {
			"isForceFefresh": 1
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "操作成功"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message)

	def test_userinfo_02(self):
		u"选择不强刷获取用户信息内容，请求成功"
		url = self.url
		data = {
			"isForceFefresh": 2
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：', re)
		# 断言响应消息
		expect_message = "操作成功"
		actual_message = re['message']
		self.assertEqual(expect_message, actual_message)
		#断言数据
		expect_data=self.login_name
		actual_data=re["body"]["data"]["loginName"]
		self.assertEqual(expect_data,actual_data)

	def test_userinfo_03(self):
		u"参数错误，请求失败"
		url = self.url
		data = {
			"isForceFefresh": ""
		}
		data = jsonTostr(data)
		print('data：', data)
		re = sceneDecide(url, data)
		print('re：',re)
		# 断言响应消息
		expect_message = "may not be null;"
		actual_message = re['message']
		self.assertIn(expect_message, actual_message)

if __name__ == "__main__":
	unittest.main()