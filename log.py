# -*- Encoding: utf-8 -*-
import logging
from os.path import join, exists
from os import makedirs


log_format = '%(asctime)s|%(levelname)s|%(message)s|%(filename)s-%(lineno)s'


def get_4f_logger(name, log_path, log_level='INFO'):
    lvls = ['debug', 'info', 'warn', 'error']
    _logger = logging.getLogger(name)
    _logger.setLevel(getattr(logging, log_level.upper()))

    if not exists(log_path):
        makedirs(log_path)

    for lvl in lvls:
        logfile = join(log_path, '{}.log'.format(lvl.lower()))
        fh = logging.FileHandler(logfile)
        fh.setLevel(getattr(logging, lvl.upper()))
        fh.setFormatter(logging.Formatter(log_format))
        _logger.addHandler(fh)
    return _logger


if __name__ == "__main__":
    logger = get_4f_logger(__name__, 'var/log')
    logger.warning('this is a warning')
