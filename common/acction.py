# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/22 20:17
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from sktest.common.elements import el
from sktest.common.locator import locating_element
from sktest.common.globals import g


class Action:
    def __init__(self):
        pass

    @staticmethod
    def open(step):
        """
        打开浏览器至目标网址
        """
        element = step.get('element', '')
        value = el.get(element)[1]
        g.driver.get(value)
        sleep(0.5)

    @staticmethod
    def input(step):
        """
        输入
        """
        data = step.get('data', '')
        element = step.get('element', '')
        location_ele = locating_element(element)
        if data:
            if data.get("清除文本框") == "否":
                pass
            else:
                location_ele.clear()
            for k, v in data.items():
                if k.startswith("text"):
                    if v.startswith("*"):
                        for w in v.strip("*"):
                            location_ele.send_keys(w)
                            sleep(0.3)
                    else:
                        location_ele.send_keys(v)
        elif hasattr(g, data):
            # 输入验证码
            location_ele.send_keys(g.data)
        sleep(0.5)
        return location_ele

    @staticmethod
    def click(step):
        """
        单击
        """
        element = step.get('element', '')
        location_ele = locating_element(element)
        location_ele.click()  # TODO 考虑优化事件 元素不可点击 等待处理
        sleep(0.5)

    @staticmethod
    def right_click(step):
        actions = ActionChains(g.driver)
        element = step.get('element', '')
        location_ele = locating_element(element)
        actions.context_click(location_ele)
        actions.perform()
        sleep(0.5)

    @staticmethod
    def double_click(step):
        """
        双击
        """
        actions = ActionChains(g.driver)
        element = step.get('element', '')
        location_ele = locating_element(element)
        actions.double_click(location_ele)
        actions.perform()
        sleep(0.5)
        return location_ele

    @staticmethod
    def hover(step):
        """
        移动到指定元素的位置
        """
        actions = ActionChains(g.driver)
        element = step.get('element', '')
        location_ele = locating_element(element)
        actions.move_to_element(location_ele).perform()
        sleep(0.5)
        return location_ele

    @staticmethod
    def select(step):
        """
        下拉框选择
        """
        data = step.get('data', '')
        element = step.get('element', '')
        location_ele = locating_element(element)
        for key, val in data.items():
            if key.startswith('index'):
                Select(location_ele).select_by_index(val)
            elif key.startswith('value'):
                Select(location_ele).select_by_value(val)
            else:
                Select(location_ele).select_by_visible_text(val)

    @staticmethod
    def upload(step):
        """
        非input标签上传文件
        """
        import win32com.client

        data = step.get('data', '')
        element = step.get('element', '')
        location_ele = locating_element(element)
        file_path = data.get('text', '') or data.get('file', '')
        location_ele.click()
        sleep(3)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.Sendkeys(file_path)
        sleep(2)
        shell.Sendkeys("{ENTER}")
        sleep(2)

    @staticmethod
    def recognition(step):
        element = step.get('element', '')
        location_ele = locating_element(element)
        from common.snapshot import snapshot
        from common.ocr import ocr_image
        snapshot(location_ele, 'captcha/code.bmp')
        g.data = ocr_image('snapshot/captcha/code.bmp')
        sleep(0.5)

    @staticmethod
    def scroll(step):
        data = step.get('data')
        element = step.get('element')
        x = data.get("x", '')
        y = data.get("y", '')
        if not element:
            if y:
                g.driver.execute_script(
                    f"document.documentElement.scrollTop={y}")
            if x:
                g.driver.execute_script(
                    f"document.documentElement.scrollLeft={x}")
        else:
            # 滚动至元素可见的位置
            location_ele = locating_element(element)

            g.driver.execute_script(
                f"arguments[0].scrollIntoView()", location_ele)

    def check(self):
        pass

    def no_check(self):
        pass


act = Action()

if __name__ == '__main__':
    pass

# TODO 部分操作待完善
