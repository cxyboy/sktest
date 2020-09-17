# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/22 20:17
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from common.elements import el
from common.locator import locating_element
from common.globals import g


class Action:
    def __init__(self):
        pass

    @staticmethod
    def open(step):
        element = step['element']
        value = el.get(element)[1]
        g.driver.get(value)
        sleep(0.5)

    @staticmethod
    def input(step):
        data = step.get('data', '')
        element = step['element']
        location_ele = locating_element(element)
        if data:
            if data.startswith('text'):
                data = str(data).split('=')[1]
                location_ele.send_keys(data)
            else:
                location_ele.send_keys(data)
        else:
            location_ele.send_keys(g.data)
        sleep(0.5)
        return location_ele

    @staticmethod
    def click(step):
        element = step['element']
        location_ele = locating_element(element)
        location_ele.click()
        sleep(0.5)

    @staticmethod
    def hover(step):
        actions = ActionChains(g.driver)
        element = step['element']
        element_location = locating_element(element)
        actions.move_to_element(element_location).perform()
        sleep(0.5)
        return element_location

    def select(self):
        pass

    def upload(self):
        pass

    def right_click(self):
        pass

    def double_click(self):
        pass

    def check(self):
        pass

    def no_check(self):
        pass

    @staticmethod
    def recognition(step):
        element = step['element']
        location_ele = locating_element(element)
        from common.snapshot import snapshot
        from common.ocr import ocr_image
        snapshot(location_ele, 'captcha/code.bmp')
        g.data = ocr_image('snapshot/captcha/code.bmp')
        sleep(0.5)


act = Action()

if __name__ == '__main__':
    pass

# TODO 部分操作待完善
