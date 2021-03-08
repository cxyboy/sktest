# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 18:23

from datetime import datetime

from sktest.common.elements import el
from sktest.common.globals import g
from sktest.common.log import logger
from sktest.common.utility import Excel, test_suit_format, get_today,mkdir_
from sktest.test.testsuit import TestSuit
from sktest.common.report import Report


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
                test_suit = test_suit_format(self.test_case_workbook.read(self.case_sheet_name))

                logger.info("**** 从Excel导入用例套件成功 ****")
            except:
                logger.exception("**** 从Excel导入用例套件失败 ****")

            else:
                ts = TestSuit(test_suit)
                ts.run()
                self.report_workbook.write(self.case_sheet_name, g.step_result)
                report_sava_path = mkdir_("report/"+get_today())
                report = Report(f"{report_sava_path}/report_{datetime.strftime(datetime.now(), '%H%M%S')}.xlsx")
                report.create_report_excel(g.case_result)
                report.create_summary_excel([g.case_sum_num, g.case_run_num, g.case_result])
                report.close_workbook()
