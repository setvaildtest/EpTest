# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/27 0027
@File : test_voiceInfoAdd.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

import unittest
from ep_common.ConfigServer import conf_url
from ep_common.SceneDecide import sceneDecide
from ep_common.VoiceBase64Util import voiceBase64
from ep_common.MysqldbUtil import MySqlUtil
import json
import time


class VoiceInfoAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.user_id = 4
        self.api_url = 'coding/v3/userInfo/voiceInfoAdd'
        self.url = conf_url() + self.api_url
        print(self.url)

    def tearDown(self) -> None:
        # self.mysql = MySqlUtil()
        # self.sql = "update ep_user_auth_info set voice_model_id = null where user_id = %s" % (self.user_id)
        # self.mysql.sql_update(self.sql)
        # self.mysql.cursor.close()
        pass

    # @unittest.skip('调试')
    def test_voice_info_add_01(self):
        u'远鉴首次新增声纹'
        data = voiceBase64('voice1.wav', 'voice2.wav', 'voice3.wav')
        data = json.dumps(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    @unittest.skip
    def test_voice_info_add_02(self):
        u'远鉴新增重复声纹，提示声纹信息已存在'
        data = voiceBase64('voice1.wav', 'voice2.wav', 'voice3.wav')
        data = json.dumps(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '声纹信息已存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    @unittest.skip
    def test_voice_info_add_03(self):
        u'远鉴新增声纹，声纹中有1条重复，该条语音为重复添加'
        data = voiceBase64('voice1.wav', 'voice2.wav', 'voice3.wav')
        data = json.dumps(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '该条语音为重复添加'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
