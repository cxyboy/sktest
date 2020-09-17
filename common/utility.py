# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/22 10:01
from datetime import datetime
import openpyxl, xlrd
from common.config import header, keywords, result_col
from common.globals import g
from pathlib import Path


class Excel:

    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        if mode == 'r':
            self.workbook = xlrd.open_workbook(file_path)

        elif mode == 'w':
            self.workbook = openpyxl.load_workbook(file_path)

    def read(self, sheet_name):
        """
        读取excel数据
        :param sheet_name: 表格标签名
        :return:[[],……]
        """
        sheet = self.workbook.sheet_by_name(sheet_name)
        rows = sheet.nrows
        data = []
        for i in range(rows):
            data.append(sheet.row_values(i))
        return data

    def write(self, sheet_name, data):
        sheet = self.workbook[sheet_name]
        for i, v in enumerate(data):
            sheet.cell(i + 2, result_col, v)
        self.workbook.save(self.file_path)

    def close(self):
        self.workbook.close()


def data_to_dict(data):
    """
    格式化excel表头为键数据为值的字典
    :param data:[[],……]
    :return:[{},……{}]
    """
    header_dict = {}
    dict_data_list = []
    key = []
    for i in data[0]:
        k = i.strip()
        h = header.get(k, k).lower()
        key.append(h)
        header_dict[h] = k
    for i in data[1:]:
        data_dict = {}
        for j in range(len(key)):
            data_dict[key[j]] = i[j]
        dict_data_list.append(data_dict)
    return dict_data_list


def testsuit_format(data):
    """
    格式化测试套件 将用例组成一个套件
    [
    {'id': 'test-1', 'title': '百度搜索', 'condition': '', 'flag': '', 'result': '',
        'steps': [{'step': '1.0', 'operation': '打开', 'page': '百度', 'element': '百度搜索链接', 'testdata': ''},
                  {'step': '2.0', 'operation': '检查', 'page': '百度', 'element': '页面标题', 'testdata': ''}]},
    {'id': 'test-2', 'title': '打开搜狗', 'condition': '', 'flag': '', 'result': '',
        'steps': [{'step': '1.0', 'operation': '查看', 'page': '搜狗', 'element': '搜狗页面', 'testdata': ''}]}
    ]
    :param data:
    :return: iter@迭代器
    """
    test_suite = []
    test_case = {}
    data = data_to_dict(data)
    for i in data:
        if i['id'].strip():
            if test_case.get('id'):
                test_suite.append(test_case)
                test_case = {}
            for key in ('id', 'title', 'condition', 'flag', 'expected'):
                test_case[key] = i[key]

            test_case['steps'] = []
        stp = i['step']
        if stp:
            step = {'step': str(stp)}
            for key in ('operation', 'page', 'element', 'data'):
                if i[key]:
                    if i['page']:
                        g.page = i['page']
                    else:
                        i['page'] = g.page
                    step[key] = i[key]
            test_case['steps'].append(step)
    if test_case:
        test_suite.append(test_case)
    return test_suite
    # return iter(test_suite)


def element_format(data):
    """
    格式化元素，返回一个以页面+元素为key的字典
    :param data:
    :return:{{}，……}
    """
    elements = {}
    data = data_to_dict(data)
    for d in data:
        if d['page']:
            g.page = d['page']
        else:
            d['page'] = g.page
        elements[d['page'] + '-' + d['element']] = d
    return elements


def check_keyword(k):
    k_ = keywords.get(k)
    return k_


def parse(test_case):
    """
    解析测用例
    将 打开 百度搜索链接 转换成 open https://www.baidu.com
    """
    for step in test_case['steps']:
        step['operation'] = check_keyword(step['operation'])


def get_today():
    now = datetime.now()
    return now.strftime('%Y%m%d')


def mkdir(directory):
    path = Path(directory)
    if not path.is_dir():
        path.mkdir()
    return str(path)


if __name__ == '__main__':
    # e = Excel(r'D:\Desktop\Excel File\test.xlsx', mode='r')
    # print('==' * 20)
    # print(testsuit_format(e.read('case')))
    # print(element_format(e.read('elements')))

    pass
