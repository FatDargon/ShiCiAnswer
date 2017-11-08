# -*- coding:utf-8 -*-  
'''
Created on 2017年10月19日

@author: Administrator
'''
import re
import jieba

def test1():
    s = '“罗浮山下四 时春”的下一句是什么? '
    
    t3 = re.compile("“(.{4,12}?)”")
    m3 = t3.findall('“罗浮山下四 时春”的“下一句”是“什么”?')
    print m3
def test2():
# t = re.compile("“.+”", 0)
# # print re.match(t, s).group()
# jieba.load_userdict("../dict/userdict.txt")
# fragment = jieba.cut(s)
# print '/'.join(fragment)
# type_of_question_dict = ['无诗句','无作品','上一句','下一句','']
# for i in type_of_question_dict[2:]:
#     print i
# 
#     if m3:
#         type_of_question= type_of_question_dict.index(i)-1
#         break
    pass
def test3():
    s = 'dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfg《下dddddddddddddd一句》'
    t2 = re.compile(r"《(.*?)》")
    m2 = re.search(t2, s)
    if m2:
        zuopin = m2.group()
        zuopin = re.sub('《|》| ', '', zuopin)
    else:
        zuopin = 'sdddddddd'
    print zuopin
    
    
if __name__ == '__main__':
    test3()