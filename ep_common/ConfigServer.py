# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/7
@File : Config.py
@describe : 关联配置文件configServer.ini文件，读取服务器地址，鉴权用户配置信息

"""
from configparser import ConfigParser
import os


def conf_url():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    # 获取当前文件的上一级目录，再拼接configServer.ini的路径
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    # print(path)
    conf.read(path,encoding='utf-8')
    host = conf.get('server', 'host')
    port = conf.get('server', 'port')
    url = host + ':' + port + '/'
    # print(url)
    return url


def conf_type_Permission():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    permission = conf.items('type')[0][1]
    return permission


def conf_type_Encrypt():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    encrypt = conf.items('type')[1][1]
    return encrypt


def conf_type_Sign():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    sign = conf.items('type')[2][1]
    return sign


def conf_type_session():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    session = conf.items('type')[3][1]
    return session


def conf_permission_key():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    permission = conf.items('key')[0][1]
    print(permission)
    return permission


def conf_encrypt_key():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    encrypt = conf.items('key')[1][1]
    return encrypt


def conf_sign_key():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    sign = conf.items('key')[2][1]
    print('签名密钥：',sign)
    return sign


def conf_operator_v1():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    operator = conf.get('operator_v1','operator')
    print(operator)
    return operator

def conf_operator_v2():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    operator = conf.get('operator_v2','operator')
    print(operator)
    return operator

def conf_version():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path,encoding='utf-8')
    version = conf.get('permission_version','version')
    print(version)
    print(type(version))
    return version

def conf_appid():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configServer.ini'
    conf.read(path, encoding='utf-8')
    appId = conf.get('appId', 'appId')
    print('conf配置的appId为：',appId)
    return appId


if __name__ == '__main__':
    conf_url()
    # conf_type()
    conf_sign_key()
    conf_operator_v1()
    conf_operator_v2()
    conf_version()

