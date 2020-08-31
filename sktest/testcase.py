# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/22 20:10
from time import sleep
from common.elements import el
from common.acction import Action
from common.globals import g
from common.log import logger


class TestCase:
    def __init__(self, test_case):
        self.test_case = test_case

    def run(self):
        for step in self.test_case['steps']:
            logger.info("Run The Step: %s|%s|%s" % (int(float(step['step'])), step['operation'], step['element']))
            page = step['page']
            element = step['element']
            step['element'] = el.have(page, element)
            try:
                getattr(Action, step['operation'].lower())(step)
                logger.info("Run The Step: %s|%s|%s Success" % (int(float(step['step'])), step['operation'], step['element']))
                self.test_case['result'] = 'ok'
                sleep(0.3)
            except:
                self.test_case['result'] = 'err'
                logger.info("Run The Step: %s|%s|%s Fail" % (int(float(step['step'])), step['operation'], step['element']))
            g.result.append(self.test_case['result'])
        sleep(0.5)
