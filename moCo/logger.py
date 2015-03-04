__author__ = 'mannsi'


import logging


def initialize_logging(log_level):
    logger = logging.getLogger('moco')
    logger.setLevel(log_level)
    fh = logging.FileHandler('moco.log')
    fh.setLevel(log_level)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
