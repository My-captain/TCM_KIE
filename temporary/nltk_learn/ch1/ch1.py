# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 19:22
# @Author  : Mr.Robot
# @Site    : 
# @File    : ch1.py
# @Software: PyCharm

from nltk.book import *

# 显示单词的上下文
print(text1.concordance("monstrous"))
print(text2.concordance("affection"))
print(text3.concordance("living"))

# 查找与当前单词具有相同上下文的单词
print(text1.similar("monstrous"))

# common_contexts 检索 由多个单词共享的上下文
print(text2.common_contexts(["monstrous", "very"]))

# dispersion_plot 用于生成单词在某text中的分布色散图
text4.dispersion_plot(["citizens", "democracy"])

# 统计smote出现次数
print(text3.count("smote"))
print(text5.count("lol") / len(text5))

# 统计文中每个word以及word出现的频次
fdist1 = FreqDist(text1)
print(fdist1.most_common(50))
# 统计text1中只出现了一次的单词
print(fdist1.hapaxes())

