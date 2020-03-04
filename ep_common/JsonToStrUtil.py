# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/7
@File : JsonToStrUtil.py
@describe : json对象转换为str

"""
import json
def jsonTostr(data):
    j_str = json.JSONEncoder().encode(data)
    return j_str