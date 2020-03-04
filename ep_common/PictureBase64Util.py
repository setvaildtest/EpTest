# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/26 0026
@File : PictureBase64Util.py
@describe : 图片base64工具

"""

import base64, os

deviceFingerprint = "00:5A:13:15:5F:41"


def pictureBase64(pic0, pic1, pic2):
    file_path = os.path.realpath(__file__)
    # print(os.path.dirname(file_path))
    pic_list = [pic0, pic1, pic2]
    pic_data_list = []
    i = 0
    while i <= 2:
        picture_path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'testResources\\' + 'image\\' + pic_list[i]
        with open(picture_path, 'rb') as f:
            b64_pic = base64.b64encode(f.read())
            b64_pic_dec = str(b64_pic, encoding='utf-8')
            pic_data_list.append(b64_pic_dec)
        i += 1
    data = {
        "datas": [
            {"data": pic_data_list[0]},
            {"data": pic_data_list[1]},
            {"data": pic_data_list[2]}],
        "deviceFingerprint": deviceFingerprint
    }
    # print(data)
    # print(type(data))
    return data


if __name__ == '__main__':
    pictureBase64('z.jpg', 'x.jpg', 'c.jpg')
