# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/22 18:27


from sktest.common.utility import Excel, element_format


class Elements:

    def __init__(self):
        pass

    def get_elements(self, elements_file):
        e = Excel(elements_file)
        self.elements = element_format(e.read('elements'))

    def have(self, page, element):
        ele = page + '-' + element
        if self.elements.get(ele, ''):
            return ele
        else:
            """元素查不到"""
            return ''

    def get(self, element):
        el_ = self.elements.get(element)
        if el_:
            value = el_.get('value', '')
            # value = el_['value']
            return el_, value
        return element, element

    """ 
    根据用例的页面查找元素
    {页面名+元素名：{元素名：元素}}
    """


el = Elements()
