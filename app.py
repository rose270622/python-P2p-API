# 初始化日志配置
import logging
import os
from logging import handlers


BASE_URL = "http://user-p2p-test.itheima.net/"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_URL = "52.83.144.39"
DB_USERNAME = "root"
DB_PASSWORD = "Itcast_p2p_20191228"
DB_MEMBER = "czbk_member"
DB_FINANCE = "czbk_finance"
def init_log_config():
# 创建日志对象
   logger=logging.getLogger()

# 创建日志等级
   logger.setLevel(logging.INFO)
# 创建控制台日志处理器和文件日志处理器
   sh = logging.StreamHandler()
   log_path = BASE_DIR + os.sep + "log" + os.sep+"p2p.log"
   fh = logging.handlers.TimedRotatingFileHandler(log_path, when="m", interval=5, backupCount=5, encoding="utf-8")
# 设置日志格式和创建格式化器
   fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
   formatter = logging.Formatter(fmt)

# 将格式化器添加到日志器中
   sh.setFormatter(formatter)
   fh.setFormatter(formatter)
# 将日志处理器添加到日志对象中
   logger.addHandler(sh)
   logger.addHandler(fh)
