# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/27 10:35
import os
from datetime import datetime
from common.utility import get_today,mkdir
from common.globals import g


def snapshot(img_file, element=None, ):
    """
    截取指定元素的图片/屏幕
    :param element:
    :param img_file:
    :return: bool
    """
    if element:
        result = element.screenshot('snapshot/' + str(img_file))
        return result
    path = mkdir(os.path.join("D:/sktest/snapshot", get_today()))
    result = g.driver.save_screenshot(path + '/' + datetime.strftime(datetime.now(), '%H%M%S') + '_' + img_file)
    return result
