#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging

logging.basicConfig(filename='/tmp/test.log',format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10,'log')

'''
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0
'''


