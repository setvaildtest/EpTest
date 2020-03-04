# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/22 0022
@File : Redisutil.py
@describe : 获取redis用户短信验证码

"""

from redis import StrictRedis
from ep_common.ConfigRedis import conf_redis
from ep_common.ConfigPerson import ConfigPerson as CP


def redis_phone_code():
    try:
        host, port, db, passwd = conf_redis()
    except:
        host, port, db = conf_redis()
        r = StrictRedis(host=host, port=port, db=db)
    else:
        r = StrictRedis(host=host, port=port, db=db, password=passwd)
    finally:
        try:
            num = CP().conf_phone()
            code = r.get('smsCode:' + num)
            new_code = int(code)
            print(int(code))
            return new_code
        except Exception as result:
            print('错误：=======> %s' % result)
            print('重新获取验证码！')


def set_bind_auto():
    try:
        host, port, db, passwd = conf_redis()
    except:
        host, port, db = conf_redis()
        r = StrictRedis(host=host, port=port, db=db)
    else:
        r = StrictRedis(host=host, port=port, db=db, password=passwd)
    finally:
        try:
            bind_key = 'sysConfig:system.userDevices.boundMode'
            get_bind_key = r.get(bind_key)
            get_bind_key = str(get_bind_key, encoding='utf-8')
            print(get_bind_key)
            if get_bind_key == 'normal':
                print(get_bind_key)
                new_value = r.set(bind_key, 'auto')
                print('修改成功，修改后的状态为：', new_value)
                # return bing_value
            elif get_bind_key == 'auto':
                print('状态为：', get_bind_key)
        except:
            print('修改失败！')


def set_bind_normal():
    try:
        host, port, db, passwd = conf_redis()
    except:
        host, port, db = conf_redis()
        r = StrictRedis(host=host, port=port, db=db)
    else:
        r = StrictRedis(host=host, port=port, db=db, password=passwd)
    finally:
        try:
            bind_key = 'sysConfig:system.userDevices.boundMode'
            get_bind_key = r.get(bind_key)
            get_bind_key = str(get_bind_key, encoding='utf-8')
            print(get_bind_key)
            if get_bind_key == 'auto':
                print(get_bind_key)
                new_value = r.set(bind_key, 'normal')
                print('修改成功，修改后的状态为：', new_value)
                # return bing_value
            elif get_bind_key == 'normal':
                print('状态为：', get_bind_key)
        except:
            print('修改失败！')


if __name__ == '__main__':
    # redis_phone_code()
    set_bind_auto()
