# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/22
@File : viewStatus（获取认证信息状态）.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
import unittest


class ViewStatus(unittest.TestCase):

	def setUp(self):

		self.api_url = 'coding/v3/user/authinfo/viewStatus'
		self.url = conf_url() + self.api_url

	def test_view_status_01(self):
		u"获取用户认证状态请求成功"
		url = self.url
		data = {
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

	def tearDown(self):
		pass



if __name__ == "__main__":
	unittest.main()
