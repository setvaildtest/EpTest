# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/22 0022
@File : ConfigRedis.py
@describe : 关联配置文件configRedis.ini文件，读取redis信息

"""
from configparser import ConfigParser
import os


def conf_redis():
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configRedis.ini'
    conf.read(path, encoding='utf-8')
    try:
        host = conf.get('redis', 'host')
        port = conf.get('redis', 'port')
        db = conf.get('redis', 'db')
        passwd = conf.get('redis', 'passwd')
    except:
        return host,port,db
    else:
        return host, port, db, passwd


if __name__ == '__main__':
    t = conf_redis()
    print(t)