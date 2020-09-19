# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 10:00

import os
from datetime import datetime
from sktest.autotest import AutoTest
from common.emailtool import send_email

case_object_name = 'Your Object name'

file_path = 'testcase/testcase.xlsx'
sheet_name = 'case'

chrome_executable_path = ''
ie_executable_path = ''

browser_config = {"browserName": "Chrome", "executable_path": chrome_executable_path}

auto = AutoTest(file_path, sheet_name, browser_config)
run_time = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")
auto.run()

email_config = {'user': "Your email", "password": "Email authorization code"}
email_receiver = ['18573208753@163.com']
email_content = f"""
        测试项目：{case_object_name}
        测试环境：{os.name}
        执行时间：{run_time}
        测试执行人：{os.getlogin()}
        自动化测试完成，详情请查阅附件。。。
    """
send_email(email_config, email_receiver, email_content)

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
