# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/27 10:23

import tesserocr
from PIL import Image


def ocr_image(image_path):
    """
    图片识别
    :param image_path:
    :return:
    """
    image = Image.open(image_path)
    image = image.convert('L')
    threshold = 127
    tb = []
    for i in range(256):
        if i < threshold:
            tb.append(0)
        else:
            tb.append(1)
    image = image.point(tb, '1')
    code = tesserocr.image_to_text(image)
    print(code)
    return code

ocr_image("E:\TestDemo\cypress\screenshots\demo.js\Demo -- Demo.png")

