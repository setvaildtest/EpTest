# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/9/18
@File : LogUtil.py
@describe : 简要描述本文件的内容，包括主要模块、函数的说明

"""

import logging
from logging import handlers
import os.path
import time

class Logger():
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        t_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        file_path = os.path.realpath(__file__)
        log_path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'logs\\'
        log_file_name = log_path + 'testcase.log' + '.' + t_time
        self.logger = logging.getLogger(log_file_name)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        th = handlers.TimedRotatingFileHandler(filename=log_file_name, when=when, backupCount=backCount,
                                               encoding='utf-8')
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


if __name__ == '__main__':
    log = Logger(level='debug')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('警告')
    log.logger.error('报错')
    log.logger.critical('严重')
    Logger(level='debug').logger.error('error')