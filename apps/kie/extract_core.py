# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 20:25
# @Author  : Mr.Robot
# @Site    : 
# @File    : extract_core.py
# @Software: PyCharm

import pynlpir
import jieba
import jieba.posseg as pseg
import json
import os
from datetime import date


WORD_MAP_NLPIR = {
    "noun": "n",
        # 人名
        "personal name": "nr",
        "Chinese surname": "nr",
        "Chinese given name": "nr",
        "Japanese personal name": "nr",
        "transcribed personal name": "nr",
        # 地名
        "toponym": "ns",
        "transcribed toponym": "ns",
        # 机构团体名
        'organization/group name': 'nt',
        # 其它专名
        "other proper noun": "nz",
        # 名词性惯用语
        "noun phrase": "nl",
        # 名词性语素
        "noun morpheme": "ng",
    # 时间词
    "time word": "t",
        # 时间词性语素
        "time morpheme": "tg",
    # 处所词
    "locative word": "s",
    # 方位词
    "noun of locality": "f",
    # 动词
    "verb": "v",
        # 动词"有"
        "verb 有": "vyou",
        # 行事动词
        "performative verb": "vx",
        # 名动词
        "noun-verb": "vn",
        # 动词性惯用语
        "verb phrase": "vl",
        # 副动词
        "auxiliary verb": "vd",
        # 趋向动词
        "directional verb": "vf",
        # 不及物动词
        "intransitive verb": "vi",
        # 动词"是"
        "verb 是": "vshi",
        # 动词性语素
        "verb morpheme": "vg",
    # 形容词
    "adjective": "a",
        # 形容词性惯用语
        "adjective phrase": "al",
        # 形容词性语素
        "adjective morpheme": "ag",
        # 名形词
        "noun-adjective": "an",
        # 副形词
        "auxiliary adjective": "ad",
    # 区别词
    "distinguishing word": "b",
        # 区别词性惯用语
        "distinguishing phrase": "bl",
    # 状态词
    "status word": "z",
    # 代词
    "pronoun": "r",
        # 人称代词
        "personal pronoun": "rr",
        # 疑问代词
        "interrogative pronoun": "ry",
        # 指示代词
        "demonstrative pronoun": "rz",
        # 代词性语素
        "pronoun morpheme": "rg",

    # 网址URL
    "URL": "xu",
    # 表情符合
    "emoticon": "xm",
    # Email字符串
    "email address": "xe",
    # 非语素字
    "non-morpheme character": "xx",
    # 微博会话分隔符
    "hashtag": "xs",
    # 字符串
    "string": "x",
    # 副词
    "adverb": "d",
    # 连
    "particle 连": "ulian",
    # 过
    "particle 过": "uguo",
    # 的／底
    "particle 的/底": "ude1",
    # 地
    "particle 地": "ude2",
    # 所
    "particle 所": "usuo",
    # 来讲／来说／而言／说来
    "particle 来讲/来说/而言/说来": "uls",
    # 着
    "particle 着": "uzhe",
    # 等／等等／云云
    "particle 等/等等/云云": "udeng",
    # 的话
    "particle 的话": "udh",
    # 之
    "particle 之": "uzhi",
    # 一样／一般／似的／般
    "particle 一样/一般/似的/般": "uyy",
    # 得
    "particle 得": "ude3",
    # 了／喽
    "particle 了/喽": "ule",
    # 助词
    "particle": "u",

    # 后缀
    "suffix": "k",
    # 左括号
    "left parenthesis/bracket": "wkz",
    # 顿号
    "enumeration comma": "wn",
    # 分号
    "semicolon": "wf",
    # 单位符号
    "unit of measure sign": "wh",
    # 冒号
    "colon": "wm",
    # 省略号
    "ellipsis": "ws",
    # 右引号
    "right quotation mark": "wyy",
    # 句号
    "period": "wj",
    # 问号
    "question mark": "ww",
    # 叹号
    "exclamation mark": "wt",
    # 破折号
    "dash": "wp",
    # 右括号
    "right parenthesis/bracket": "wky",
    # 左引号
    "left quotation mark": "wyz",
    # 百分号千分号
    "percent/per mille sign": "wb",
    # 逗号
    "comma": "wd",
    # 标点符号
    "punctuation mark": "w",

    # 数量词
    "numeral-plus-classifier compound": "mq",
    # 数词
    "numeral": "m",
    # 并列连词
    "coordinating conjunction": "cc",
    # 连词
    "conjunction": "c",
    # 语气词
    "modal particle": "y",
    # 前缀
    "prefix": "h",

    # 时量词
    "temporal classifier": "qt",
    # 动量词
    "verbal classifier": "qv",
    # 量词
    "classifier": "q",
    # 拟声词
    "onomatopoeia": "o",
    # 介词“把”
    "preposition 把": "pba",
    # 介词“被”
    "preposition 被": "pbei",
    # 介词
    "preposition": "p",
    # 叹词
    "interjection": "e",
}


def list_my_dict(dir_path):
    print(os.curdir)
    dict_list = os.listdir(dir_path)
    dict_list = [os.path.join(os.path.abspath(dir_path), file_name) for file_name in dict_list]
    return dict_list


print("{} [jieba]: loading user specified dict...".format(date))
for i in list_my_dict("C:/Users/Mr.Robot/Desktop/workspace/TCM_KIE/apps/kie/my_dict/"):
    jieba.load_userdict(i)
    print("dict {} loaded successfully;".format(os.path.split(i)))
print("{} [jieba]: user specified dict loaded successfully".format(date))


def hmm_extract(text):
    words = pseg.cut(text)
    result = []
    for w in words:
        temp = {w.word: w.flag}
        result.append(temp)
    result = json.dumps(result, ensure_ascii=False)
    return result


def nlpir_extract(text):
    pynlpir.open()
    words = pynlpir.segment(text)
    words_list = []
    for word, word_p in words:
        words_list.append({word: word_p})
    words_list = json.dumps(words_list, ensure_ascii=False)

    key_words = pynlpir.nlpir.GetKeyWords(text)
    print(key_words)

    return words_list


if __name__ == "__main__":
    text_origin = "今年6月咳嗽无痰,胸闷气喘逐渐加重,去住院CT：右肺占位,住院治疗,化疗2疗程,右锁骨上颈部可测见肿大淋巴结,口咽干,恶心呕吐,"
    print(nlpir_extract(text_origin))
