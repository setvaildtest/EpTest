# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/22 0022
@File : ConfigPerson.py
@describe : 关联配置文件configPerson.ini文件，读取用户名，密码，电话号码信息

"""
from configparser import ConfigParser
import os


class ConfigPerson():

    def __init__(self):
        self.file_path = os.path.realpath(__file__)
        self.path = os.path.dirname(os.path.dirname(self.file_path)) + '\\' + 'ep_config\\configPerson.ini'

    def conf_loginName(self):
        conf = ConfigParser()
        conf.read(self.path, encoding='utf-8')
        loginName = conf.get('information', 'loginName')
        return loginName

    def conf_password(self):
        conf = ConfigParser()
        conf.read(self.path, encoding='utf-8')
        passwd = conf.get('information', 'password')
        return passwd

    def conf_phone(self):
        conf = ConfigParser()
        conf.read(self.path, encoding='utf-8')
        phone = conf.get('information', 'phone')
        return phone

    def conf_email(self):
        conf = ConfigParser()
        conf.read(self.path, encoding='utf-8')
        email = conf.get('information', 'email')
        # print(email)
        return email

    def conf_write_passwd(self,new_password):
        conf = ConfigParser()
        conf.read(self.path, encoding='utf-8')
        conf.set('information', 'password', new_password)
        passwd = conf.get('information', 'password')
        with open(self.path,'w+') as f:
            conf.write(f)
            return passwd


if __name__ == '__main__':
    l = ConfigPerson()
    l1 = l.conf_write_passwd('123456789')
    l.conf_email()
    print(l1)
