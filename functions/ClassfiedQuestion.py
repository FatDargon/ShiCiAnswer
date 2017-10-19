# -*- coding:utf-8 -*-  
'''
Created on 2017年10月18日

@author: Administrator
'''
import re

def classfied_question(my_question):
#     print my_question['题目']
    type_of_question_dict = ['无诗句','无作品','上一句','下一句','']
    type_of_question = 0
    t1 = re.compile("“.+”")
    m1 = re.match(t1, my_question['题目'])
    if m1:
        shiju = m1.group()
        shiju = re.sub('“|”| ', '', shiju)
    else:
        shiju = ''
        type_of_question = 0
    t2 = re.compile("《.+》")
    m2 = re.match(t2, my_question['题目'])
    if m2:
        zuopin = m2.group()
        zuopin = re.sub('《|》| ', '', zuopin)
    else:
        zuopin = ''
        type_of_question = 1
    for i in type_of_question_dict[2:]:
        print i
        t3 = re.compile(i)
        m3 = re.match(t3, my_question['题目'])
        if m3:
            type_of_question= type_of_question_dict.index(i)-1
            break
    return {
        '作品':zuopin,
        '诗句':shiju,
        '关键字':'',
        '问题类型':type_of_question,
        '类型详解':type_of_question_dict[type_of_question]
    }