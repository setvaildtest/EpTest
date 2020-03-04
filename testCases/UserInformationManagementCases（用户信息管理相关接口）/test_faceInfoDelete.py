# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/27 0027
@File : test_faceInfoDelete.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

import unittest
from ep_common.ConfigServer import conf_url
from ep_common.SceneDecide import sceneDecide
from ep_common.VoiceBase64Util import deviceFingerprint, voiceBase64
from ep_common.MysqldbUtil import MySqlUtil
import json


class FaceInfoDelete(unittest.TestCase):
    def setUp(self) -> None:
        self.api_url = 'coding/v3/userInfo/faceInfoDelete'
        self.url = conf_url() + self.api_url

    def tearDown(self) -> None:
        pass

    def test_face_info_detele_01(self):
        u'删除远鉴人脸'
        data = {
            "deviceFingerprint": deviceFingerprint
        }
        data = json.dumps(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    @unittest.skip('切换远鉴配置')
    def test_face_info_detele_02(self):
        u'人脸信息不存在，删除远鉴人脸'
        data = {
            "deviceFingerprint": ''
        }
        data = json.dumps(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '人脸信息不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')


if __name__ == '__main__':
    unittest.main()
