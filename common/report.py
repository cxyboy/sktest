# -*- coding:utf8 -*-
# @author：X.
# @time：2020/9/16:10:07


import xlsxwriter


class Report:

    def __init__(self, sheet_file):
        self.workbook = xlsxwriter.Workbook(sheet_file)

        self.bold = self.workbook.add_format({'bold': 1})
        self.red = self.workbook.add_format({'bg_color': 'red', 'color': 'white'})
        self.gray = self.workbook.add_format({'bg_color': 'gray', 'color': 'white'})
        self.green = self.workbook.add_format(
            {'bg_color': 'green', 'color': 'white'})
        self.blue = self.workbook.add_format({'bg_color': 'blue', 'color': 'white'})
        self.orange = self.workbook.add_format(
            {'bg_color': 'orange', 'color': 'white'})

    def create_report_excel(self, data):
        worksheet = self.workbook.add_worksheet('report')

        # 自定义样式，加粗

        # [['test-1', '打开OMP', 'success', 'success'], ['test-2', '提交咨询单', 'fail', 'success']]
        headings = ['用例编号', '用例标题', '预期结果', '实际结果', '测试结论']
        # 写入表头
        worksheet.write_row('A1', headings, self.bold)
        # 写入数据
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 'pass':
                    worksheet.write(i + 1, j, data[i][j], self.green)
                elif data[i][j] == 'failure':
                    worksheet.write(i + 1, j, data[i][j], self.red)
                elif data[i][j] == 'skipped':
                    worksheet.write(i + 1, j, data[i][j], self.gray)
                else:
                    worksheet.write(i + 1, j, data[i][j])
                    pass

    def create_summary_excel(self, data):
        worksheet = self.workbook.add_worksheet('summary')
        headings = ['用例数', '执行', '通过', '失败', '阻塞']
        worksheet.write_row('A1', headings, self.bold)
        lst = []
        pass_unm = 0
        failure_unm = 0
        skipped_unm = 0
        for i, v in enumerate(data):
            if isinstance(v, list):
                for j in v:
                    if j[-1] == 'pass':
                        pass_unm += 1
                    elif j[-1] == 'failure':
                        failure_unm += 1
                    elif j[-1] == 'skipped':
                        skipped_unm += 1
            else:
                lst.append(data[i])
        lst.append(pass_unm)
        lst.append(failure_unm)
        lst.append(skipped_unm)
        worksheet.write_row('A2', lst)

    def close_workbook(self):
        self.workbook.close()
