# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/9/17
@File : user_device_sql.py
@describe : 插入用户后自动插入对应绑定设备

"""

import pymysql as MySQLdb
import time
from random import choice
from ep_common.MysqldbUtil import MySqlUtil


class SqlUtil(object):
    db = MySqlUtil().sql_connect(1)
    cursor = db.cursor()
    # sql = 'SELECT * FROM epass.ep_users ORDER BY id DESC LIMIT 1'
    sql_ep_users = 'SELECT MAX(id) FROM ep_users'
    sql_ep_user_device = 'SELECT MAX(id) FROM ep_user_device'

    @classmethod
    def insert_user_data(cls, user_data_num, device_data_num):
        cls.cursor.execute(SqlUtil.sql_ep_users)
        id = cls.cursor.fetchone()[0]
        phone = choice(['13333333333', '13123332232', '13134443444'])
        password = '6B9A5A73D3D3E7D3DD8F4979029ADAD9'
        if id:
            # cls.sql = 'SELECT * FROM epass.ep_users ORDER BY id DESC LIMIT 1'
            # cls.cursor.execute(cls.sql)
            # id = cls.cursor.fetchone()[0]
            x = 0
            id += 1
            while x < user_data_num:
                login_name = 'zxh' + str(id)
                sql = "INSERT INTO `ep_users`" \
                      "(`id`,`login_name`,`password`,`name`,`sex`,`age`,`birthday`,`phone`,`email`,`id_card_number`,`position`,`department`,`company_id`,`extend_attrs`,`is_disabled`,`is_deleted`,`creator`,`updator`,`create_time`,`update_time`,`pass_expire_date`,`lock_expire_date`,`locked`)" \
                      "VALUES ('%s', '%s','%s', '%s', '1', '1', '2019-08-30', '%s', '1', '1', '1', '1', '1', '1', '0', '0', 'admin', 'admin', '2019-08-13 15:43:30', '2019-08-13 15:43:30', '2020-02-09 15:43:30', '1970-01-01 00:00:00', '0')" % (
                          id, login_name, password, login_name, phone)
                print(sql)
                cls.cursor.execute(sql)
                cls.db.commit()
                # 插入一条用户后，关联并插入对应的设备数据
                SqlUtil.insert_device_data(device_data_num, id)
                x += 1
                id += 1
        else:
            num = 0
            while num < user_data_num:
                login_name = 'zxh' + str(num + 1)
                sql = "INSERT INTO `ep_users`" \
                      "(`id`,`login_name`,`password`,`name`,`sex`,`age`,`birthday`,`phone`,`email`,`id_card_number`,`position`,`department`,`company_id`,`extend_attrs`,`is_disabled`,`is_deleted`,`creator`,`updator`,`create_time`,`update_time`,`pass_expire_date`,`lock_expire_date`,`locked`)" \
                      "VALUES ('%s', '%s','%s', '%s', '1', '1', '2019-08-30', '%s', '1', '1', '1', '1', '1', '1', '0', '0', 'admin', 'admin', '2019-08-13 15:43:30', '2019-08-13 15:43:30', '2020-02-09 15:43:30', '1970-01-01 00:00:00', '0')" % (
                          num + 1, login_name, password, login_name, phone)
                print(sql)
                cls.cursor.execute(sql)
                cls.db.commit()
                SqlUtil.insert_device_data(device_data_num, num + 1)
                num += 1

    @classmethod
    def insert_device_data(self, device_num, user_id):
        self.cursor.execute(SqlUtil.sql_ep_user_device)
        device_id = self.cursor.fetchone()[0]
        if device_id:
            i = 0
            device_id += 1
            while i < device_num:
                # sql = 'SELECT * FROM epass.ep_user_device ORDER BY id DESC LIMIT 1'
                # SqlUtil.cursor.execute(sql)
                # new_id = id + 1
                print('=======================>>>>', id)
                remarks_list = ['LYA-AL00', 'iPhone 7', 'vivo X9L', 'vivo', 'HUAWEI', 'iPhone X', 'iPhone 5', 'XIAOMI']
                login_name = ['zxh1', 'zxh2', 'zxh3']
                print('开始插入时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                # print('===================>', id)
                mac = ''

                f_user = choice(login_name) + str(i)
                remarks = choice(remarks_list)
                device_type = 1
                user_id = user_id
                bind_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                device_fingerprint = ''
                # PASS_EXPIRTE_DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                expire_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                sql = 'insert into ep_user_device(id,mac,f_user,remarks,device_type,user_id,bind_time,device_fingerprint,expire_date) values'
                sql = sql + '("%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
                    device_id, mac, f_user, remarks, device_type, user_id, bind_time, device_fingerprint, expire_date)
                print(sql)
                SqlUtil.cursor.execute(sql)
                SqlUtil.db.commit()
                i += 1
                device_id += 1
            print('插入完成时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            count = SqlUtil.cursor.execute('select count(*) from ep_user_device')
            print(count)
        else:
            num = 0
            while num < device_num:
                print('=======================>>>>', id)
                remarks_list = ['LYA-AL00', 'iPhone 7', 'vivo X9L', 'vivo', 'HUAWEI', 'iPhone X', 'iPhone 5', 'XIAOMI']
                login_name = ['zxh1', 'zxh2', 'zxh3']
                print('开始插入时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                # print('===================>', id)
                mac = ''
                f_user = choice(login_name) + str(num + 1)
                remarks = choice(remarks_list)
                device_type = 1
                user_id = user_id
                bind_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                device_fingerprint = ''
                # PASS_EXPIRTE_DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                expire_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                sql = 'insert into ep_user_device(id,mac,f_user,remarks,device_type,user_id,bind_time,device_fingerprint,expire_date) values'
                sql = sql + '("%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
                    num + 1, mac, f_user, remarks, device_type, user_id, bind_time, device_fingerprint, expire_date)
                print(sql)
                SqlUtil.cursor.execute(sql)
                SqlUtil.db.commit()
                num += 1
            print('插入完成时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            count = SqlUtil.cursor.execute('select count(*) from ep_user_device')
            print(count)
            print('测试' * 10)


if __name__ == '__main__':
    SqlUtil.insert_user_data(2,4)
    # SqlUtil.insert_device_data(4, 1)
