# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/7
@File : SignEncryptPermission.py
@describe : 鉴权，加密，签名，会话，每一种组合的判断

"""

def SignEncryptPermission(Permission, encrypt, sign, Session):

    # 全部关闭
    if Permission == 0 and encrypt == 0 and sign == 0 and Session == 0:
        return 0
    # 开启【鉴权】
    elif Permission == 1 and encrypt == 0 and sign == 0 and Session == 0:
        return 1
    # 开启【加密】
    elif Permission == 0 and encrypt == 1 and sign == 0 and Session == 0:
        return 2
    # 开启【签名】
    elif Permission == 0 and encrypt == 0 and sign == 1 and Session == 0:
        return 3
    # 开启【会话】
    elif Permission == 0 and encrypt == 0 and sign == 0 and Session == 1:
        return 4
    # 开启【鉴权加密】
    elif Permission == 1 and encrypt == 1 and sign == 0 and Session == 0:
        return 5
    # 开启【鉴权加密签名】
    elif Permission == 1 and encrypt == 1 and sign == 1 and Session == 0:
        return 6
    # 开启【鉴权加密签名会话】
    elif Permission == 1 and encrypt == 1 and sign == 1 and Session == 1:
        return 7
    # 开启【鉴权签名】
    elif Permission == 1 and encrypt == 0 and sign == 1 and Session == 0:
        return 8
    # 开启【鉴权会话】
    elif Permission == 1 and encrypt == 0 and sign == 0 and Session == 1:
        return 9
    # 开启【加密签名】
    elif Permission == 0 and encrypt == 1 and sign == 1 and Session == 0:
        return 10
    # 开启【加密会话】
    elif Permission == 0 and encrypt == 1 and sign == 0 and Session == 1:
        return 11
    # 开启【签名会话】
    elif Permission == 0 and encrypt == 0 and sign == 1 and Session == 1:
        return 12
    # 开启【鉴权加密会话】
    elif Permission == 1 and encrypt == 1 and sign == 0 and Session == 1:
        return 13
    # 开启【鉴权签名会话】
    elif Permission == 1 and encrypt == 0 and sign == 1 and Session == 1:
        return 14
    # 开启【加密签名会话】
    elif Permission == 0 and encrypt == 1 and sign == 1 and Session == 1:
        return 15




