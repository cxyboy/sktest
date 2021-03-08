# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 10:02
from sktest.common.globals import g
from sktest.common.log import logger
from sktest.common.utility import parse
from sktest.test.testcase import TestCase


class TestSuit:

    def __init__(self, test_suit):

        pass
        self.test_suit = test_suit

    def run(self):
        for test_case in self.test_suit:
            g.case_sum_num += 1
            if test_case['flag'].upper() != 'N':
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
                        logger.exception(f'**** case {test_case["id"]}:{test_case["title"]} executed  lose ****')
                    else:
                        logger.info(f"**** Executed Test Case: {test_case['id']}:{test_case['title']}  done ****")
            else:
                case_result = 'skip'
                g.case_result.append(
                    [test_case['id'], test_case['title'], test_case['expected'], case_result, 'skipped'])

        g.driver.quit()
