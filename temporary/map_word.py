# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 18:00
# @Author  : Mr.Robot
# @Site    : 
# @File    : map_word.py
# @Software: PyCharm
from collections import OrderedDict



map = {'s': ('处所词', 'locative word'),
    'f': ('方位词', 'noun of locality'),
    'v': ('动词', 'verb', {
        'vd': ('副动词', 'auxiliary verb'),
        'vn': ('名动词', 'noun-verb'),
        'vshi': ('动词"是"', 'verb 是'),
        'vyou': ('动词"有"', 'verb 有'),
        'vf': ('趋向动词', 'directional verb'),
        'vx': ('行事动词', 'performative verb'),
        'vi': ('不及物动词', 'intransitive verb'),
        'vl': ('动词性惯用语', 'verb phrase'),
        'vg': ('动词性语素', 'verb morpheme'),
    }),
    'a': ('形容词', 'adjective', {
        'ad': ('副形词', 'auxiliary adjective'),
        'an': ('名形词', 'noun-adjective'),
        'ag': ('形容词性语素', 'adjective morpheme'),
        'al': ('形容词性惯用语', 'adjective phrase'),
    }),
    'b': ('区别词', 'distinguishing word', {
        'bl': ('区别词性惯用语', 'distinguishing phrase'),
    }),
    'z': ('状态词', 'status word'),
    'r': ('代词', 'pronoun', {
        'rr': ('人称代词', 'personal pronoun'),
        'rz': ('指示代词', 'demonstrative pronoun', {
            'rzt': ('时间指示代词', 'temporal demonstrative pronoun'),
            'rzs': ('处所指示代词', 'locative demonstrative pronoun'),
            'rzv': ('谓词性指示代词', 'predicate demonstrative pronoun'),
        }),
        'ry': ('疑问代词', 'interrogative pronoun', {
            'ryt': ('时间疑问代词', 'temporal interrogative pronoun'),
            'rys': ('处所疑问代词', 'locative interrogative pronoun'),
            'ryv': ('谓词性疑问代词', 'predicate interrogative pronoun'),
        }),
        'rg': ('代词性语素', 'pronoun morpheme'),
    }),
    'm': ('数词', 'numeral', {
        'mq': ('数量词', 'numeral-plus-classifier compound'),
    }),
    'q': ('量词', 'classifier', {
        'qv': ('动量词', 'verbal classifier'),
        'qt': ('时量词', 'temporal classifier'),
    }),
    'd': ('副词', 'adverb'),
    'p': ('介词', 'preposition', {
        'pba': ('介词“把”', 'preposition 把'),
        'pbei': ('介词“被”', 'preposition 被'),
    }),
    'c': ('连词', 'conjunction', {
        'cc': ('并列连词', 'coordinating conjunction'),
    }),
    'u': ('助词', 'particle', {
        'uzhe': ('着', 'particle 着'),
        'ule': ('了／喽', 'particle 了/喽'),
        'uguo': ('过', 'particle 过'),
        'ude1': ('的／底', 'particle 的/底'),
        'ude2': ('地', 'particle 地'),
        'ude3': ('得', 'particle 得'),
        'usuo': ('所', 'particle 所'),
        'udeng': ('等／等等／云云', 'particle 等/等等/云云'),
        'uyy': ('一样／一般／似的／般', 'particle 一样/一般/似的/般'),
        'udh': ('的话', 'particle 的话'),
        'uls': ('来讲／来说／而言／说来', 'particle 来讲/来说/而言/说来'),
        'uzhi': ('之', 'particle 之'),
        'ulian': ('连', 'particle 连'),
    }),
    'e': ('叹词', 'interjection'),
    'y': ('语气词', 'modal particle'),
    'o': ('拟声词', 'onomatopoeia'),
    'h': ('前缀', 'prefix'),
    'k': ('后缀', 'suffix'),
    'x': ('字符串', 'string', {
        'xe': ('Email字符串', 'email address'),
        'xs': ('微博会话分隔符', 'hashtag'),
        'xm': ('表情符合', 'emoticon'),
        'xu': ('网址URL', 'URL'),
        'xx': ('非语素字', 'non-morpheme character'),
    }),
    'w': ('标点符号', 'punctuation mark', {
        'wkz': ('左括号', 'left parenthesis/bracket'),
        'wky': ('右括号', 'right parenthesis/bracket'),
        'wyz': ('左引号', 'left quotation mark'),
        'wyy': ('右引号', 'right quotation mark'),
        'wj': ('句号', 'period'),
        'ww': ('问号', 'question mark'),
        'wt': ('叹号', 'exclamation mark'),
        'wd': ('逗号', 'comma'),
        'wf': ('分号', 'semicolon'),
        'wn': ('顿号', 'enumeration comma'),
        'wm': ('冒号', 'colon'),
        'ws': ('省略号', 'ellipsis'),
        'wp': ('破折号', 'dash'),
        'wb': ('百分号千分号', 'percent/per mille sign'),
        'wh': ('单位符号', 'unit of measure sign'),
    })
}


if __name__ == "__main__":
    result = ""
    for k, v in map.items():
        if len(v) > 2:
            for k_i, v_i in v[2].items():
                result += "#"
                result += v_i[0]
                result += "\n"
                result += '"'
                result += v_i[1]
                result += '": "'
                result += k_i
                result += '",\n'
        result += "#"
        result += v[0]
        result += "\n"
        result += '"'
        result += v[1]
        result += '": "'
        result += k
        result += '",\n'
    print(result)







