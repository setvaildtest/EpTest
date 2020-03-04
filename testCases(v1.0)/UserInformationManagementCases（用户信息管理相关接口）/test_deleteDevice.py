# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : chenxiaohui
@Time : 2019/8/22
@File : delete（删除设备指纹）.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.MysqldbUtil import MySqlUtil
from ep_common.user_device_sql import SqlUtil
import unittest




class DeleteDevice(unittest.TestCase):

	def setUp(self):
		self.api_url = 'coding/outDevice/remove'
		self.url = conf_url() + self.api_url
		self.mysql = MySqlUtil()
		SqlUtil.insert_user_data(2, 3)
		SqlUtil.insert_device_data(20, 2)


	def test_delete_Device_01(self):
		u"设备id正确，根据id删除本人设备指纹请求成功"
		self.mysql.cursor.execute('select id from ep_user_device where user_id = 2')
		device_id = self.mysql.cursor.fetchall()[0][0]
		print(device_id)
		url=self.url
		data = {
			"id": device_id
		}
		# sql = 'select * from ts_gesture_password'
		# data = sql_connect(sql,0,1)
		data = jsonTostr(data)
		print('通过sql获取到的data：', data)
		print('数据类型：', type(data))
		re = sceneDecide(url, data)
		print(re)
		self.mysql.cursor.execute("select * from ep_user_device where id =%s"%device_id)
		id = self.mysql.cursor.fetchall()[0][0]
		if id == None:
			print("删除成功")
		expect_status = 'success'
		actual_status = re['status']
		self.assertEqual(expect_status, actual_status, msg=re['status'])


	def test_delete_Device_02(self):
		u"设备id非本人设备，根据id删除本人设备指纹请求成功"
		self.mysql.cursor.execute('select id from ep_user_device where user_id != 2')
		device_id = self.mysql.cursor.fetchall()[0][0]
		print(device_id)
		url=self.url
		data = {
			"id": device_id
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

	def test_delete_Device_03(self):
		u"设备id不存在，根据id删除本人设备指纹请求成功"
		#todo 验证缺陷
		url=self.url
		data = {
			"id": "999"
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

	def test_delete_Device_04(self):
		u"设备id为空，根据id删除本人设备指纹请求成功"
		# todo 验证缺陷
		url=self.url
		data = {
			"id": ""
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

	def test_delete_Device_05(self):
		u"设备id为空串，根据id删除本人设备指纹请求成功"
		# todo 验证缺陷
		url=self.url
		data = {
			"id": "    "
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
		self.mysql.sql_delete("delete from ep_user_device where f_user like 'zxh%'")
		self.mysql.sql_delete("delete from ep_users where name like 'zxh%'")
		self.mysql.db_sql.close()



if __name__ == "__main__":
	unittest.main()

