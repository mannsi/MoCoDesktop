__author__ = 'mannsi'


import logging
import os


def initialize_logging(log_level):
    logger = logging.getLogger('moco')
    logger.setLevel(log_level)

    fh = logging.FileHandler(os.path.join(os.path.expanduser('~'), 'moco.log'))
    fh.setLevel(log_level)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)


def get_logger():
    return logging.getLogger("moco")

