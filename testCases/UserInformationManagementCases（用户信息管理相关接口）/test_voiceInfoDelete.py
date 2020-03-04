# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/27 0027
@File : test_voiceInfoDelete.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

import unittest
from ep_common.ConfigServer import conf_url
from ep_common.SceneDecide import sceneDecide
from ep_common.VoiceBase64Util import deviceFingerprint
import json


class VoiceInfoDelete(unittest.TestCase):
    def setUp(self) -> None:
        self.api_url = 'coding/v3/userInfo/voiceInfoDelete'
        self.url = conf_url() + self.api_url

    def tearDown(self) -> None:
        pass

    def test_voice_info_detele_01(self):
        u'删除远鉴声纹'
        data = {
            "deviceFingerprint": deviceFingerprint
        }
        data = json.dumps(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '操作成功'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')

    @unittest.skip('调试')
    def test_voice_info_detele_02(self):
        u'删除远鉴声纹'
        data = {
            "deviceFingerprint": ''
        }
        data = json.dumps(data)
        re = sceneDecide(self.url, data)
        print(re)
        expect_status = '声纹信息不存在'
        actual_status = re['message']
        self.assertEqual(expect_status, actual_status, msg='测试通过!')


if __name__ == '__main__':
    unittest.main()
