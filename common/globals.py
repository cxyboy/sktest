# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 9:43
from selenium import webdriver
from common.config import element_wait_time, page_flash_timeout


class Globals:

    def __init__(self):
        self.browser = ''
        self.driver = ''
        self.executable_path = ''
        self.page = ''
        self.step_result = []
        self.case_result = []
        self.data = 'gd'
        self.case_sum_num = 0
        self.case_run_num = 0

    def init(self, browser_config):
        self.browser = browser_config.get('browserName', '').lower()
        self.executable_path = browser_config.get('executable_path', '')

        if self.browser == 'ie':
            if self.executable_path:
                self.driver = webdriver.Ie(executable_path=self.executable_path)
            else:
                self.driver = webdriver.Ie()
        elif self.browser == 'firefox':
            if self.executable_path:
                self.driver = webdriver.Firefox(executable_path=self.executable_path)
            else:
                self.driver = webdriver.Firefox()
        elif self.browser == 'chrome':
            if self.executable_path:
                self.driver = webdriver.Chrome(executable_path=self.executable_path)
            else:
                self.driver = webdriver.Chrome()
        else:
            raise Exception("this browser is not supported or mistake name:%s " % self.browser)

        self.driver.implicitly_wait(element_wait_time)
        self.driver.set_page_load_timeout(page_flash_timeout)


g = Globals()
