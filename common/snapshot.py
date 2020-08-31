# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/27 10:35

def snapshot(element, img_file=''):
    """
    截取指定元素的图片
    :param element:
    :param img_file:
    :return: bool
    """
    result = element.screenshot('snapshot/'+str(img_file))
    return result
