import time
from random import choice
from ep_common.MysqldbUtil import MySqlUtil


class ChildUserSqlUtil(object):
    db = MySqlUtil()
    cursor = db.cursor

    @classmethod
    def get_id(cls, table_name):
        sql = "SELECT * FROM %s ORDER BY id DESC LIMIT 1" % table_name
        cls.cursor.execute(sql)
        data = cls.cursor.fetchall()
        if data:
            cls.cursor.execute(sql)
            max_id = cls.cursor.fetchone()[0]
            id = max_id + 1
        else:
            id = 1
        return id

    @classmethod
    def delete_datas_by_id(cls, table_name, id_list):
        for i in id_list:
            cls.db.sql_delete("delete from %s where id=%s" % (table_name, i))

    @classmethod
    def insert_users(cls, data_num, is_disabled):
        user_id_list = []
        login_name_list = []
        phone = choice(['13333333333', '131233322323', '13134443444'])
        password = '6B9A5A73D3D3E7D3DD8F4979029ADAD9'
        id = cls.get_id('ep_users')
        x = 0
        while x < data_num:
            login_name = 'apiTestUser_sql' + str(id)
            create_time = time.strftime('%Y-%m-%d %H:%M:%S')
            sql = "INSERT INTO `ep_users`" \
                  "(`id`,`login_name`,`password`,`name`,`sex`,`age`,`birthday`,`phone`,`email`,`id_card_number`,`position`,`department`,`company_id`,`extend_attrs`,`is_disabled`,`is_deleted`,`creator`,`updator`,`create_time`,`update_time`,`pass_expire_date`,`lock_expire_date`,`locked`)" \
                  "VALUES ('%s', '%s','%s', '%s', '1', '18', NULL, '%s', 'apiTestEmail@bam.cn', '51167812345678xxxx', '测试工程师', '测试部', 1, '', '%s', '0', 'apiTest', 'apiTest', '%s', '%s', '2029-02-09 15:43:30', '1970-01-01 00:00:00', '0')" % (
                      id, login_name, password, login_name, phone, is_disabled, create_time, create_time)
            cls.db.sql_insert(sql)
            user_id_list.append(id)
            login_name_list.append(login_name)
            x += 1
            id += 1
        return user_id_list, login_name_list

    @classmethod
    def insert_user(cls, user_info):
        id = cls.get_id('ep_users')
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = "insert into ep_users(id,login_name,password,name,sex,age,birthday, phone, email, id_card_number, position, department,company_id,extend_attrs,is_disabled,is_deleted,creator,updator,create_time,update_time, pass_expire_date, lock_expire_date, locked)VALUES(%s,'%s','%s','%s','%s','%s','%s', '%s','%s', '%s', '%s','%s',%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            id, user_info['login_name'], user_info['password'], user_info['name'],
            user_info['sex'], user_info['age'], user_info['birthday'],
            user_info['phone'],
            user_info['email'], user_info['id_card_number'], user_info['position'],
            user_info['department'], user_info['company_id'], user_info['extend_attrs'],
            user_info['is_disabled'], user_info['is_deleted'], user_info['creator'],
            user_info['updator'], create_time, create_time, user_info['pass_expire_date'],
            user_info['lock_expire_date'], user_info['locked'])
        cls.db.sql_insert(sql)
        print(sql)
        return id

    @classmethod
    def insert_extend_attr(cls, user_id):
        id = cls.get_id("ep_user_extends_attrs")
        attr="apiTestAttr_sql"+str(id)
        value = "apiTestValue_sql" + str(id)
        sql = "INSERT INTO `ep_user_extends_attrs`(`id`, `user_id`, `deleted`, `attr`, `value`) VALUES (%s, '%s', '%s', '%s', '%s')" % (
            id, user_id, '0', attr, value)
        cls.db.sql_insert(sql)
        return id,attr,value

    @classmethod
    def insert_auth(cls, user_id, company_app_id):
        id = cls.get_id('ep_user_company_app')
        sql = "insert into ep_user_company_app(id,user_id,company_id,company_app_id) values(%s,'%s',1,%s)" % (
            id, user_id, company_app_id)
        print(sql)
        cls.db.sql_insert(sql)
        return id

    @classmethod
    def insert_child_users(cls, data_num, user_id, company_app_id):
        child_id_list = []
        child_name_list = []
        id = cls.get_id("ep_child_user")
        x = 0
        while x < data_num:
            name = "apiTestChild_sql" + str(id)
            sql = "insert into ep_child_user(id, name, description, user_id, company_id, company_app_id) VALUES (%s, '%s', 'sql插入的测试子账号', '%s', 1, %s)" % (
                id, name, user_id, company_app_id)
            cls.db.sql_insert(sql)
            child_id_list.append(id)
            child_name_list.append(name)
            x += 1
            id += 1
        return child_id_list, child_name_list

    @classmethod
    def insert_app(cls,data_num):
        id_list = []
        appId_list = []
        id = cls.get_id('ep_company_app')
        x = 0
        while x < data_num:
            name ="apiTestApp_sql" + str(id)
            appId="apiTestApp_sql" + str(id)
            sql = "INSERT INTO ep_company_app(id, name, description, security_level_id, company_id, sort_name, create_time, update_time, create_user, update_user, type, app_id, sso_address, android_package_name, downdload_addr, download_type, app_icon, is_relay) VALUES (%s, '%s', '', 2, 1, '%s', '2019-09-10 00:10:59', '2019-09-10 00:10:59', 'apiTest', 'apiTest', '0', '%s', 'ios协议', 'andriod协议', '', 'app_market', '', '0')"%(id,name,name,appId)
            cls.db.sql_insert(sql)
            id_list.append(id)
            appId_list.append(appId)
            x += 1
            id+=1
        return id_list,appId_list

    @classmethod
    def find_child_user(cls,user_id,company_app_id):
        child_user_name_list=[]
        cls.cursor.execute("select name from ep_child_user where user_id='%s' and company_app_id='%s'"%(user_id,company_app_id))
        tuple=cls.cursor.fetchall()
        for c in range(len(tuple)):
            child_user_name_list.append(tuple[c][0])
        return child_user_name_list



if __name__ == '__main__':
    id,appId=ChildUserSqlUtil.insert_app(1)
    print(id,appId)