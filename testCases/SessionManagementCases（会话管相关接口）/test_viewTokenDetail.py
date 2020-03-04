#!/usr/bin/python
#-*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/21
@File : test_viewTokenDetail.py
@describe :该模块主要用于测试查看会话详情接口，该接口需要登录且当前登录用户只能查看自己的账号的会话详情

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.DoauthCheck import doauth_check

import unittest

class ViewTokenDetail(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/v3/session/viewTokenDetail'
        self.url = conf_url() + self.api_url

    def test_view_token_01(self):
        u'登录之后请求查看会话详情接口，请求成功'
        print('查询会话详情api_url：=================>',self.url)
        data ={}
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询会话详情接口响应：=================>\n',re)
        expect_status='success'
        actual_status=re['status']
        self.assertEqual(expect_status,actual_status)

    def test_view_token_02(self):
        u'不登录请求查看会话详情接口，请求失败'
        print('查询会话详情api_url：=================>',self.url)
        data ={}
        data = jsonTostr(data)
        re=doauth_check(self.url,data)
        print('查询会话详情接口响应：=================>\n',re)
        # 断言
        expect_status = "fail"
        actual_staus = re['status']
        self.assertIn(expect_status, actual_staus)


if __name__=="__main__":
    unittest.main()

