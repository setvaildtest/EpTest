# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/13
@File : SessionCheck.py
@describe : 会话管理，生成会话

"""

from ep_common import Headers
from ep_common import ConfigServer
from ep_common.JwtWriteRead import jwt_write_read
from ep_common.JwtGet import get_jwt

def session():
    headers = Headers.headers()
    print('session原始headers为：',headers)
    appId = ConfigServer.conf_appid()
    print('session返回的appId为：',appId)
    headers.update({'appid':appId})
    jwt = jwt_write_read()
    # jwt = get_jwt()
    print(jwt)
    # jwt = JwtWriteRead.jwt_write_read()
    # jwt = 'eyJhbGciOiJIUzI1NiJ9.eyJlcHRva2VuIjoidG9rZW46MTU2NTY5ODAwMTg1MSIsImFwcGlkIjoiZXBhc3NfYXBwIiwic3VidG9rZW4iOiIiLCJ1c2VyaWQiOiJ3YW5namluZyIsImlhdCI6IjIwMTktMDgtMTMgMjAuMDYuNDEiLCJ1cGR0IjoiMjAxOS0wOC0xMyAyMC4wNi40MSJ9.zDdL7D2PuqQ7MwiA3vI0t43t5a2ciWWfWsFj-qRUDDk'
    headers.update({'jwt':jwt})
    print('session最终生成的headers为：',headers)
    # print(jwt)
    return headers


if __name__ == '__main__':
    session()