# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/20 0020
@File : MysqlDbUtil.py
@describe : sql数据库，封装增删改查功能

"""

import pymysql as Mysql
from ep_common.ConfigMysql import conf_mysql


class MySqlUtil():

    def __init__(self):
        host, user, passwd, db = conf_mysql(1)
        self.db_sql = Mysql.connect(host, user, passwd, db)
        self.cursor = self.db_sql.cursor()

    def sql_connect(sql, caseNum=None, dataNum=None):
        host, user, passwd, db = conf_mysql(1)
        db_sql = Mysql.connect(host, user, passwd, db)
        # dataCase = new_data[caseNum][dataNum]
        # print('获取表中所有的数据元素：', new_data)
        # print('取出ts_gesture_password数据用例：', dataCase)
        # return dataCase
        return db_sql

    def sql_find(self, sql, caseNum=None, dataNum=None):
        self.cursor.execute(sql)
        new_data = self.cursor.fetchall()
        if caseNum ==None and dataNum == None:
            print('返回数据：>>>>', new_data)
        elif caseNum ==None:
            print('返回数据：>>>>', new_data)
        elif dataNum == None:
            print('返回数据：>>>>', new_data)
        else:
            dataCase = new_data[caseNum][dataNum]
            print('获取表中所有的数据元素：', new_data)
            print('取出ts_gesture_password数据用例：', dataCase)
            print(dataCase)
            return dataCase

    def sql_insert(self, sql):
        self.cursor.execute(sql)
        self.db_sql.commit()

    def sql_update(self, sql):
        self.cursor.execute(sql)
        self.db_sql.commit()

    def sql_delete(self, sql):
        self.cursor.execute(sql)
        self.db_sql.commit()


if __name__ == '__main__':
    msql = MySqlUtil()
    sql_find = 'select * from ts_gesture_password'
    sql_insert = ''
    # sql_update = "update epass.ep_user_auth_info set gesture_data = null where user_id = 4"
    sql_detele = ''
    msql.sql_find(sql_find,0,1)
    # msql.sql_update(sql_update)
