# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/22 20:10
from time import sleep
from common.elements import el
from common.acction import Action
from common.globals import g
from common.log import logger
from common.snapshot import snapshot


class TestCase:
    def __init__(self, test_case):
        self.test_case = test_case

    def run(self):
        case_result = 'success'
        # if self.test_case['flag'].upper() == 'Y':

        g.case_run_num += 1
        for step in self.test_case['steps']:
            logger.info(
                ">>> Executed The Step: %s|%s|%s" % (int(float(step['step'])), step['operation'], step['element']))
            page = step['page']
            element = step['element']
            step['element'] = el.have(page, element)
            step_result = 'ok'
            try:
                getattr(Action, step['operation'].lower())(step)
                logger.info(
                    ">>> Executed The Step: %s|%s|%s Successfully" % (
                        int(float(step['step'])), step['operation'], step['element']))
                sleep(0.3)
            except:
                string_ = step['operation'] + step['element'] + '.png'
                snapshot(string_)
                step_result = 'err'
                case_result = 'fail'
                logger.info(
                    "Executed The Step: %s|%s|%s Failure" % (
                        int(float(step['step'])), step['operation'], step['element']))
            g.step_result.append(step_result)

        if self.test_case['expected'] == case_result:
            g.case_result.append(
                [self.test_case['id'], self.test_case['title'], self.test_case['expected'], case_result, 'pass'])
        else:
            g.case_result.append(
                [self.test_case['id'], self.test_case['title'], self.test_case['expected'], case_result, 'failure'])
            # else:
            #     case_result = 'skipped'
            #     g.case_result.append(
            #         [self.test_case['id'], self.test_case['title'], self.test_case['expected'], case_result, 'skipped'])
            sleep(0.5)
