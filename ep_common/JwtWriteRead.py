# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/13
@File : JwtWirteRead.py
@describe : jwt不存在，生成jwt并且写入文件，存在就读取

"""
import os
from ep_common.JwtGet import get_jwt, get_jwt_v1
from ep_common.ConfigServer import conf_version

file_path = os.path.realpath(__file__)
jwt_data = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\jwt_data'
jwt_data_v1 = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'ep_config\\jwt_data_v1.txt'
print(jwt_data)


def jwt_write_read():
    if conf_version() == '2':
        if os.path.getsize(jwt_data) == 0:
            with open(jwt_data, 'w+') as f:
                jwt = get_jwt('jwt')
                f.write(jwt)
                return jwt
        else:
            # with open(jwt_data, 'r+') as f:
            #     print('======>>>>>', f.read())
            #     con = f.read()
            #     print(con)
            #     return con
            f = open(jwt_data, 'r+')
            a = f.read()
            print(a)
            return a
        f.close()
    elif conf_version() == '1':
        if not os.path.exists(jwt_data_v1):
            with open(jwt_data_v1, 'w+') as f:
                jwt = get_jwt_v1('jwt')
                f.write(jwt)
                return jwt
        else:
            if os.path.getsize(jwt_data_v1) == 0:
                with open(jwt_data_v1, 'w+') as f:
                    jwt = get_jwt_v1('jwt')
                    f.write(jwt)
                    return jwt
            else:
                f = open(jwt_data_v1, 'r+')
                a = f.read()
                print(a)
                return a
            f.close()


def jwt_write():
    if conf_version() == '2':
        with open(jwt_data, 'w', encoding='utf-8') as f:
            jwt = get_jwt('jwt')
            f.write(jwt)
    elif conf_version() == '1':
        with open(jwt_data_v1, 'w', encoding='utf-8') as f:
            jwt = get_jwt_v1('jwt')
            f.write(jwt)
    else:
        print('写入错误！')


if __name__ == '__main__':
    # jwt_write()
    jwt_write_read()
