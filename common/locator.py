# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 8:58


from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sktest.common.config import element_wait_time
from sktest.common.elements import el
from sktest.common.globals import g
from sktest.common.log import logger


def locating_element(element):
    element_location = ''
    el_, value = el.get(element)
    wait = WebDriverWait(g.driver, element_wait_time)
    if el_['by'] in ('', 'url', 'title', 'current_url'):
        return None
    try:
        element_location = wait.until(EC.presence_of_element_located((getattr(By, el_['by'].upper()), value)))
    except:
        logger.exception(f"元素：'{element}'第一次定位超时，等待三秒重试！！！")
        sleep(3)
        try:
            element_location = wait.until(EC.presence_of_element_located((getattr(By, el_['by'].upper()), value)))
        except:
            logger.exception(f"元素：'{element}'定位超时")
        else:
            pass
    return element_location


def locating_elements():
    pass
