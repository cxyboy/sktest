# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 10:00

import os
from datetime import datetime
from sktest.autotest import AutoTest
from common.emailtool import send_email
from common.log import logger


class Config:
    def __init__(self, excel_file_path='testcase/testcase.xlsx', case_sheet_name='case', browser_name="Chrome",
                 executable_path='', case_object_name='UI Automation testing', email_account='', email_password='',
                 email_receiver=None):
        self.excel_file_path = excel_file_path
        self.case_sheet_name = case_sheet_name
        self.browser_name = browser_name
        self.executable_path = executable_path
        self.case_object_name = case_object_name
        self.email_accuont = email_account
        self.email_password = email_password
        self.email_receiver = email_receiver


cfg = Config()

browser_config = {"browserName": cfg.browser_name, "executable_path": cfg.executable_path}
email_config = {'user': cfg.email_accuont, "password": cfg.email_password}


auto = AutoTest(cfg.excel_file_path, cfg.case_sheet_name, browser_config)
run_time = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")
auto.run()

receiver = cfg.email_receiver
email_content = f"""
        测试项目：{cfg.case_object_name}
        测试环境：{os.name}
        执行时间：{run_time}
        测试执行人：{os.getlogin()}
        自动化测试完成，详情请查阅附件。。。
    """
send_email(email_config, receiver, email_content)

# TODO 后续扩展：
#                1.错误截图 --  done 出错截取整个屏幕
#               2.日志可以考虑分类保存  -- done 按天分割
#              3.生成测试报告  -- done
#             4.邮件发送 -- done
#            5.集成到Jenkins -- 待完成
#           6.整体框架容错性检测  -- 待完成

# TODO v2.0
#         1.增加时间监测
#         2.兼容app测试
