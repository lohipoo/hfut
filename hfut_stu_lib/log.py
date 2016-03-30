# -*- coding:utf-8 -*-
"""
日志模块
"""
from __future__ import unicode_literals
from logging import Logger, WARNING, StreamHandler, Formatter

__all__ = ['logger', 'unstable', 'log_result_not_found']

logger = Logger('hfut_stu_lib', level=WARNING)

sh = StreamHandler()
fmt = Formatter('[%(levelname)s]%(filename)s[%(lineno)d]: %(message)s')
sh.setFormatter(fmt)
logger.addHandler(sh)


def unstable(func):
    logger.warning('%s 功能尚不稳定, 建议使用时验证结果的正确性', func.__name__)
    return func


def log_result_not_found(page):
    logger.error('没有解析到结果, 请检查你的参数是否正确 \n %s', page)
