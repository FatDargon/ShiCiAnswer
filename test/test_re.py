# -*- coding:utf-8 -*-  
'''
Created on 2017年10月19日

@author: Administrator
'''
import re
import jieba
s = '“罗浮山下四 时春”的下一句是什么? '
# t = re.compile("“.+”", 0)
# print re.match(t, s).group()
jieba.load_userdict("../dict/userdict.txt")
fragment = jieba.cut(s)
print '/'.join(fragment)