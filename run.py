# -*- coding:utf8 -*-
# @author：X.
# @time：2021/3/5:13:26


from sktest.test.autotest import AutoTest


class Test:

    def __init__(self, file_path, sheet_name, browser="Chrome", drive=""):
        """
        :param file_path: Test file address
        :param sheet_name:The name of the test form
        :param browser: Used browser
        :param drive: Drive executable_path
        :return:
        """
        self.__path = file_path
        self.__name = sheet_name
        self.__browser = browser
        self.__drive = drive

    def main(self):
        executable_config = {"browser_name": self.__browser, "executable_path": self.__drive}
        auto = AutoTest(self.__path, self.__name, executable_config)
        auto.run()

