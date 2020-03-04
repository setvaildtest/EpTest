#!/usr/bin/python
#-*- coding:utf-8 -*-
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : zhangaihua
@Time : 2019/8/21
@File : test_viewTokenDetail.py
@describe :鉴权1.0会话详情查看接口，根据loginName查看用户会话

"""
from ep_common.ConfigServer import conf_url
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide
from ep_common.DoauthCheck import doauth_check
from ep_common.ConfigPerson import ConfigPerson

import unittest

class ViewTokenDetail(unittest.TestCase):

    def setUp(self):
        self.api_url = 'coding/outSessionManager/viewTokenDetail'
        self.url = conf_url() + self.api_url
        self.loginName=ConfigPerson().conf_loginName()

    def test_view_token_01(self):
        u'请求查看会话详情接口，请求成功'
        print('查询会话详情api_url：=================>',self.url)
        data ={
            "loginName":self.loginName
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询会话详情接口入参：=================>\n', data)
        print('查询会话详情接口响应：=================>\n',re)
        expect_status='success'
        actual_status=re['status']
        self.assertEqual(expect_status,actual_status)

    def test_view_token_02(self):
        u'登录名为空，请求失败'
        print('查询会话详情api_url：=================>',self.url)
        data ={
            "loginName":""
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询会话详情接口入参：=================>\n', data)
        print('查询会话详情接口响应：=================>\n',re)
        expect_message='登录名不能为空或空串;'
        actual_message=re['message']
        self.assertEqual(expect_message,actual_message)

    def test_view_token_03(self):
        u'登录名为空串，请求失败'
        print('查询会话详情api_url：=================>', self.url)
        data = {
            "loginName": "        "
        }
        data = jsonTostr(data)
        re = sceneDecide(self.url, data)
        print('查询会话详情接口入参：=================>\n', data)
        print('查询会话详情接口响应：=================>\n', re)
        expect_message = '登录名不能为空或空串;'
        actual_message = re['message']
        self.assertEqual(expect_message, actual_message)


if __name__=="__main__":
    unittest.main()

