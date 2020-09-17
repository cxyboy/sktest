# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 18:23
from pathlib import Path

from common.elements import el
from common.globals import g
from common.log import logger
from common.utility import Excel, testsuit_format
from sktest.testsuit import TestSuit
from common.report import Report


class AutoTest:

    def __init__(self, file_path, case_sheet_name, browser_config):
        self.case_sheet_name = case_sheet_name
        self.elements_file = file_path
        self.test_case_file = file_path
        self.test_case_workbook = Excel(self.test_case_file)
        self.report_workbook = Excel(self.test_case_file, 'w')
        g.init(browser_config)

    def run(self):
        try:
            el.get_elements(self.elements_file)
        except:
            logger.exception("**** 解析文件失败 ****")
        else:
            try:
                test_suit = testsuit_format(self.test_case_workbook.read(self.case_sheet_name))

                logger.info("**** 从Excel导入用例套件成功 ****")
            except:
                logger.exception("**** 从Excel导入用例套件失败 ****")

            else:
                ts = TestSuit(test_suit)
                ts.run()
                self.report_workbook.write(self.case_sheet_name, g.step_result)
                report = Report('report/report.xlsx')
                report.create_report_excel(g.case_result)
                report.create_summary_excel([g.case_sum_num, g.case_run_num, g.case_result])
                report.close_workbook()
