# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 9:29
# @Author  : Mr.Robot
# @Site    : 
# @File    : secl2txt.py
# @Software: PyCharm
import struct
import os

# 拼音表偏移，
startPy = 0x1540;

# 汉语词组表偏移
startChinese = 0x2628;

# 全局拼音表
GPy_Table = {}

# 解析结果
# 元组(词频,拼音,中文词组)的列表
GTable = []


# 原始字节码转为字符串
def byte2str(data):
    pos = 0
    string = ''
    while pos < len(data):
        c = chr(struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0])
        if c != chr(0):
            string += c
        pos += 2
    return string


# 获取拼音表
def getPyTable(data):
    data = data[4:]
    pos = 0
    while pos < len(data):
        index = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]
        pos += 2
        lenPy = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]
        pos += 2
        py = byte2str(data[pos:pos + lenPy])
        GPy_Table[index] = py
        pos += lenPy


# 获取一个词组的拼音
def getWordPy(data):
    pos = 0
    ret = ''
    while pos < len(data):
        index = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]
        ret += GPy_Table[index]
        pos += 2
    return ret


# 读取中文表
def getChinese(data):
    pos = 0
    while pos < len(data):
        # 同音词数量
        same = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]

        # 拼音索引表长度
        pos += 2
        py_table_len = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]

        # 拼音索引表
        pos += 2
        py = getWordPy(data[pos: pos + py_table_len])

        # 中文词组
        pos += py_table_len
        for i in range(same):
            # 中文词组长度
            c_len = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]
            # 中文词组
            pos += 2
            word = byte2str(data[pos: pos + c_len])
            # 扩展数据长度
            pos += c_len
            ext_len = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]
            # 词频
            pos += 2
            count = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]

            # 保存
            GTable.append((count, py, word))

            # 到下个词的偏移位置
            pos += ext_len


def scel2txt(file_name):
    # 分隔符
    print('-' * 60)
    # 读取文件
    with open(file_name, 'rb') as scel_f:
        data = scel_f.read()

    print("词库名：", byte2str(data[0x130:0x338]))  # .encode('GB18030')
    print("词库类型：", byte2str(data[0x338:0x540]))
    print("描述信息：", byte2str(data[0x540:0xd40]))
    print("词库示例：", byte2str(data[0xd40:startPy]))

    getPyTable(data[startPy:startChinese])
    getChinese(data[startChinese:])


if __name__ == '__main__':

    # scel所在文件夹路径
    in_path = "./sogouDict/"
    out_path = "./transDict/"

    fin = [fname for fname in os.listdir(in_path) if fname[-5:] == ".scel"]
    for src_f in fin:
        src_f_path = os.path.join(in_path, src_f)
        scel2txt(src_f_path)

        dest_f_path = out_path + src_f[:-5] + ".txt"
        dest_f = open(dest_f_path, 'w', encoding='UTF8')
        for count, py, word in GTable:
            dest_f.write(word + '\n')
        dest_f.close()
        GTable.clear()
