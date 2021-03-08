# -*- coding:utf8 -*-
# @author：X.
# @time：2021/3/5:13:26


from sktest.test.autotest import AutoTest


def run(file_path, sheet_name, chrome_executable_path=''):
    """
    :param file_path: Test file address
    :param sheet_name:The name of the test form
    :chrome_executable_path:Drive path
    :return:
    """

    browser_config = {"browserName": "Chrome", "executable_path": chrome_executable_path}
    auto = AutoTest(file_path, sheet_name, browser_config)
    auto.run()

if __name__ == '__main__':
    run(r"E:\sktest\sktest\testcase\testcase.xlsx", "case")
