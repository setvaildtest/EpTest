# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/27 0027
@File : VoiceBase64Util.py
@describe : 声纹base64工具

"""

import base64, os

deviceFingerprint = "00:5A:13:15:5F:41"


def voiceBase64(vic0, vic1, vic2):
    file_path = os.path.realpath(__file__)
    vic_list = [vic0, vic1, vic2]
    vic_data_list = []
    i = 0
    while i <= 2:
        voice_path = os.path.dirname(os.path.dirname(file_path)) + '\\' + 'testResources\\' + 'voice\\' + vic_list[i]
        with open(voice_path, 'rb') as f:
            b64_vic = base64.b64encode(f.read())
            b64_vic_dec = str(b64_vic, encoding='utf-8')
            vic_data_list.append(b64_vic_dec)
        i += 1
    data = {
        "datas": [
            {"data": vic_data_list[0], "content": ""},
            {"data": vic_data_list[1], "content": ""},
            {"data": vic_data_list[2], "content": ""}],
        "deviceFingerprint": deviceFingerprint
    }
    # print(data)
    # print(type(data))
    return data


if __name__ == '__main__':
    voiceBase64('voice1.wav', 'voice2.wav', 'voice3.wav')
