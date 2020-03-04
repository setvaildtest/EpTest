# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/21
@File : userPwdUpdate（用户密码修改）.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.ConfigPerson import ConfigPerson as CP
import unittest
import os


class UpdatePwd(unittest.TestCase):

	def setUp(self):

		self.api_url = 'coding/v3/user/userPwdUpdate'
		self.url = conf_url() + self.api_url
		self.new_passwd = 'cxh123456'

	def test_update_pwd_01(self):
		u"旧密码、新密码输入正确，修改用户密码请求成功"
		url = self.url
		data = {
			"newPassword": self.new_passwd,
			"oldPassword": CP().conf_password()
		}
		# sql = 'select * from ts_gesture_password'
		# data = sql_connect(sql,0,1)
		data = jsonTostr(data)
		print('通过sql获取到的data：', data)
		print('数据类型：', type(data))
		re = sceneDecide(url, data)
		print(re)
		expect_status = 'success'
		actual_status = re['status']
		self.assertEqual(expect_status, actual_status, msg=re['status'])

	def test_update_pwd_02(self):
		u"旧密码为空，修改用户密码请求失败"
		url = self.url
		data = {
			"newPassword": self.new_passwd,
			"oldPassword": ""
		}
		# sql = 'select * from ts_gesture_password'
		# data = sql_connect(sql,0,1)
		data = jsonTostr(data)
		print('通过sql获取到的data：', data)
		print('数据类型：', type(data))
		re = sceneDecide(url, data)
		print(re)
		expect_status = '参数错误;'
		actual_status = re['message']
		self.assertEqual(expect_status, actual_status, msg=re['status'])

	def test_update_pwd_03(self):
		u"旧密码为空串，修改用户密码请求失败"
		url = self.url
		data = {
			"newPassword": self.new_passwd,
			"oldPassword": "   "
		}
		# sql = 'select * from ts_gesture_password'
		# data = sql_connect(sql,0,1)
		data = jsonTostr(data)
		print('通过sql获取到的data：', data)
		print('数据类型：', type(data))
		re = sceneDecide(url, data)
		print(re)
		expect_status = '参数错误;'
		actual_status = re['message']
		self.assertEqual(expect_status, actual_status, msg=re['status'])


	def test_update_pwd_04(self):
		u"旧密码为输入错误，修改用户密码请求失败"
		url = self.url
		data = {
			"newPassword": self.new_passwd,
			"oldPassword": "123"
		}
		# sql = 'select * from ts_gesture_password'
		# data = sql_connect(sql,0,1)
		data = jsonTostr(data)
		print('通过sql获取到的data：', data)
		print('数据类型：', type(data))
		re = sceneDecide(url, data)
		print(re)
		expect_status = '原密码校验失败'
		actual_status = re['message']
		self.assertEqual(expect_status, actual_status, msg=re['status'])

	def test_update_pwd_05(self):
		u"新密码为输入为空，修改用户密码请求失败"
		url = self.url
		data = {
			"newPassword": "",
			"oldPassword": CP().conf_password()
		}
		# sql = 'select * from ts_gesture_password'
		# data = sql_connect(sql,0,1)
		data = jsonTostr(data)
		print('通过sql获取到的data：', data)
		print('数据类型：', type(data))
		re = sceneDecide(url, data)
		print(re)
		expect_status = '参数错误;'
		actual_status = re['message']
		self.assertEqual(expect_status, actual_status, msg=re['status'])

	def test_update_pwd_06(self):
		u"新密码为输入为空串，修改用户密码请求失败"
		url = self.url
		data = {
			"newPassword": "   ",
			"oldPassword": CP().conf_password()
		}
		# sql = 'select * from ts_gesture_password'
		# data = sql_connect(sql,0,1)
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


if __name__ == "__main__":
	unittest.main()