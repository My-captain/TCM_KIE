# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 9:51
# @Author  : Mr.Robot
# @Site    : 
# @File    : segment.py
# @Software: PyCharm
import pynlpir
pynlpir.open(encoding='gbk')

print(pynlpir.nlpir.ImportUserDict('coal_dict.txt'.encode("utf-8")))

# num = pynlpir.nlpir.AddUserWord("八角茴香油  key_nr".encode("gbk"))
print(pynlpir.segment("表寒里热证"))
