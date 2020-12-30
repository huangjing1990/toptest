# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午5:23
# @Author  : maxiang
# @File    : Log.py

"""
封装log方法

"""
import os
import logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps
import warnings

check_path='.'
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = path + '/Log'
LOG_DIR = os.path.join(log_file)
file_stream = False
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True
def get_logger(name='LOGINFO', file_log=file_stream, level=''):
    """ get logger Factory function """
    logbook.set_datetime_format('local')

    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
            os.path.join(LOG_DIR, '%s.log' % name),
            date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)

LOG = get_logger(file_log=file_stream, level='INFO')
def logger(param):
    """ fcuntion from logger meta """
    def wrap(function):
        """ logger wrapper """
        @wraps(function)
        def _wrap(*args, **kwargs):
            """ wrap tool """
            LOG.info("当前模块 {}".format(param))
            #LOG.info("全部args参数参数信息 , {}".format(str(args)))
            #LOG.info("全部kwargs参数信息 , {}".format(str(kwargs)))
            warnings.simplefilter("ignore", ResourceWarning)
            return function(*args, **kwargs)
        return _wrap
    return wrap