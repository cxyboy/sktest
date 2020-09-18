# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 10:02
from common.globals import g
from common.log import logger
from common.utility import parse
from sktest.testcase import TestCase


class TestSuit:

    def __init__(self, test_suit):

        pass
        self.test_suit = test_suit

    def run(self):

        for test_case in self.test_suit:
            g.case_sum_num += 1
            if test_case['flag'].upper() == 'Y':
                try:
                    parse(test_case)
                    logger.info("**** Parse use case successful ****")
                except:
                    logger.exception("**** Parse use case failure ****")
                else:
                    try:
                        logger.info(">>> Executed The Test Case：%s %s" % (test_case['id'], test_case['title']))
                        tc = TestCase(test_case)
                        tc.run()
                    except:
                        logger.exception(f'**** case {test_case["id"]}:{test_case["title"]} executed  failure ****')
                    else:
                        logger.info(f"**** Executed Test Case: {test_case['id']}:{test_case['title']}  successfully ****")
            else:
                case_result = 'skipped'
                g.case_result.append(
                    [test_case['id'], test_case['title'], test_case['expected'], case_result, 'skipped'])

        g.driver.quit()
