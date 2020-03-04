# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/13 0013
@File : RequnestsUtil.py
@describe : requests模块封装，get请求，post请求

"""

import requests
import json


def post(url, data, headers):
    r_text = requests.post(url=url, data=data, headers=headers).text
    dict = json.loads(r_text)
    return dict


def get(url, data, headers):
    r_text = requests.get(url=url, params=data, headers=headers).text
    dict = json.loads(r_text)
    return dict
