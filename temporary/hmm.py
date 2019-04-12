# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 12:22
# @Author  : Mr.Robot
# @Site    : 
# @File    : hmm.py
# @Software: PyCharm
import jieba
import jieba.posseg as pseg
import json
import os


def list_my_dict(dir_path):
    dict_list = os.listdir(dir_path)
    dict_list = [os.path.join(os.path.abspath(dir_path), file_name) for file_name in dict_list]
    return dict_list


for i in list_my_dict("./my_classify"):
    jieba.load_userdict(i)


words = pseg.cut("瞳神干缺")
result = []
for w in words:
    temp = {w.word: w.flag}
    result.append(temp)
result = json.dumps(result, ensure_ascii=False)
print(result)
