# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/26 0026
@File : test_faceInfoAdd.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

import unittest
from ep_common.ConfigServer import conf_url
from ep_common.SceneDecide import sceneDecide
from ep_common.PictureBase64Util import pictureBase64
from ep_common.MysqldbUtil import MySqlUtil
import time
import json


class FaceInfoAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.api_url = 'coding/v3/userInfo/faceInfoAdd'
        self.url = conf_url() + self.api_url
        self.user_id = 4
        print(self.url)

    def tearDown(self) -> None:
        # self.mysql = MySqlUtil()
        # self.sql = "update ep_user_auth_info set face_model_id = null where user_id = %s" % (self.user_id)
        # self.mysql.sql_update(self.sql)
        pass

    def test_faceinfo_add_01(self):
        u'远鉴首次新增人脸'
        # 如果返回响应操作成功，数据库人脸字段为空，检查是否切换远鉴配置信息
        data = pictureBase64('z.jpg', 'x.jpg', 'z')
        data = json.dumps(data)
        re = sceneDecide(self.url, data)
        print(re)
        time.sleep(2)
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    @unittest.skip('调试')
    def test_faceinfo_add_02(self):
        u'远鉴新增重复人脸，人脸信息已存在'
        data = pictureBase64('xxx', 'xxx', 'xx')
        data = json.dumps(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '人脸信息已存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

if __name__ == '__main__':
    unittest.main()
