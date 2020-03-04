# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/13
@File : JwtGetSignEncryptPermission.py
@describe : 单独doauth接口业务判断

"""

def jwt_per_enc_sign(Permission, encrypt, sign):
    # 全部关闭
    if Permission == 0 and encrypt == 0 and sign == 0:
        return 0
    # 开启【鉴权】
    elif Permission == 1 and encrypt == 0 and sign == 0:
        return 1
    # 开启【加密】
    elif Permission == 0 and encrypt == 1 and sign == 0:
        return 2
    # 开启【签名】
    elif Permission == 0 and encrypt == 0 and sign == 1:
        return 3
    # 开启【鉴权，加密】
    elif Permission == 1 and encrypt == 1 and sign == 0:
        return 4
    # 开启【鉴权，签名】
    elif Permission == 1 and encrypt == 0 and sign == 1:
        return 5
    # 开启【加密，签名】
    elif Permission == 0 and encrypt == 1 and sign == 1:
        return 6
    # 开启【鉴权，加密，签名】
    elif Permission == 1 and encrypt == 1 and sign == 1:
        return 7




