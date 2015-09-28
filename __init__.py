# -*- Encoding: utf-8 -*-
from os.path import join, dirname
from log import get_4f_logger

BASE_DIR = dirname(dirname(__file__))


debug_log = get_4f_logger(__name__, join(BASE_DIR, 'log'), 'INFO')


if __name__ == "__main__":
    logger = debug_log()
    logger.warning('this is a warning write by debug_log module')
