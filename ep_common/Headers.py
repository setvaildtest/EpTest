# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/8
@File : Headers.py
@describe : 默认headers封装

"""
from ep_common.ConfigServer import conf_operator_v1, conf_operator_v2, conf_version


# 定义headers
def headers():
    if conf_version() == '1':
        headers = {
            "appuser": conf_operator_v1(),
            "Content-Type": "application/json;charset=UTF-8",
        }
        print(headers)
        return headers
    elif conf_version() == '2':
        headers = {
            "operator": conf_operator_v2(),
            "Content-Type": "application/json;charset=UTF-8",
        }
        print(headers)
        return headers

if __name__ == '__main__':
    headers()
