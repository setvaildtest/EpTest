# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/27 0027
@File : VerCode.py
@describe : 发送短信验证码接口封装

"""

from ep_common.ConfigServer import conf_url
from ep_common.ConfigPerson import ConfigPerson as CP
from ep_common.JsonToStrUtil import jsonTostr
from ep_common.SceneDecide import sceneDecide


def sendcode():
    api_url = 'xxx/sendVerificationCode'
    url = conf_url() + api_url
    data = {
        "phone": CP().conf_phone(),
        "templateType": "sms.send.resetpwd.template"
    }
    data = jsonTostr(data)
    print('通过sql获取到的data：', data)
    print('数据类型：', type(data))
    re = sceneDecide(url, data)
    print(re)
    return re['status']


if __name__ == '__main__':
    sendcode()
