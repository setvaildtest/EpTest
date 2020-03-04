# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/20 0020
@File : ConfigMysql.py
@describe : 关联配置文件configDb.ini文件，读取数据库信息

"""

from configparser import ConfigParser
import os


def conf_mysql(secid):
    conf = ConfigParser()
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\configDb.ini'
    conf.read(path, encoding='utf-8')
    secs = conf.sections()
    print(secs)
    if secs[secid] == 'db':
        host = conf.get('db', 'host')
        user = conf.get('db', 'user')
        passwd = conf.get('db', 'passwd')
        db = conf.get('db', 'db')
        return host, user, passwd, db
    elif secs[secid] == 'db1':
        host = conf.get('db1', 'host')
        user = conf.get('db1', 'user')
        passwd = conf.get('db1', 'passwd')
        db = conf.get('db1', 'db')
        return host, user, passwd, db


if __name__ == '__main__':
    conf_mysql(1)
