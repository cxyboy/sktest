# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/25 10:57


import sys
import logging
from sktest.common.utility import get_today, mkdir_, Path

mkdir_('logs/'+get_today())
logger = logging.getLogger('x')  # 实例化logger对象
logger.setLevel(logging.INFO)  # 设置日志输出级别
logfile = Path('logs/'+get_today()) / f"{get_today()}.log"  # 日志文件路径
formatter = logging.Formatter('%(asctime)s [%(levelname)s]: #  %(message)s')  # 日志输出格式
file_handle = logging.FileHandler(filename=logfile, encoding='utf8')
# file_handle.setLevel(logging.INFO)
file_handle.setFormatter(formatter)
control_handle = logging.StreamHandler(sys.stdout)
control_handle.setFormatter(formatter)

logger.addHandler(file_handle)
logger.addHandler(control_handle)

