# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 10:00
import os

from sktest.autotest import AutoTest
from common.config import chrome_executable_path, ie_executable_path, firefox_executable_path

file_path = 'testcase/testcase.xlsx'
sheet_name = 'case'

browser_config = {"browserName": "Chrome", "executable_path": chrome_executable_path}

auto = AutoTest(file_path, sheet_name, browser_config)
auto.run()

# TODO 后续扩展：
#                1.错误截图 --  现在是 出错截取整个屏幕
#               2.日志可以考虑分类保存  -- 现在是 按天分割
#              3.生成测试报告  -- done
#             4.邮件发送
#            5.集成到Jenkins
#           6.整体框架容错性检测
