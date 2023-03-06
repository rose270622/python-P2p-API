
import logging
import time
from logging import handlers

from app import BASE_DIR
def init_logger_config():
    logger = logging.getLogger()
    logger.setLevel("info")
    sh = logging.StreamHandler()
    log_path = BASE_DIR + "/log/p2p{}.log".format(time.strftime("%Y%m%d-%H%M%S"))
    fh = logging.handlers.TimedRotatingFileHandler(log_path)
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(fh)

# 初始化日志配置
def init_logging_config():
    logger = logging.getLogger()
    logger.setLevel("info")
    sh = logging.StreamHandler()
    file_path = BASE_DIR +"/log/p2p{}.log".format(time.strftime("%Y%m%d-%H%M%S"))
    fh = logging.handlers.TimedRotatingFileHandler(file_path)
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(fh)
