# -*- coding:utf-8 -*-  
'''
Created on 2017年10月18日

@author: Administrator
'''
import re

def classfied_question(my_question):
#     print my_question['题目']
    type_of_question_dict = ['上一句','下一句','']
    type_of_question = 0
    #诗句匹配
    t1 = re.compile("“(.{10,35})”")
    m1 = re.match(t1, my_question['题目'])
    if m1:
        shiju = m1.group()
        shiju = re.sub('“|”| ', '', shiju)
    else:
        shiju = ''
    #作品名字匹配
    t2 = re.compile("《.+》")
    m2 = re.match(t2, my_question['题目'])
    if m2:
        zuopin = m2.group()
        zuopin = re.sub('《|》| ', '', zuopin)
    else:
        zuopin = ''
        
    #询问关键字的匹配
    keywords = []
    t3 = re.compile("“(.{4,12}?)”")
    m3 = re.findall(t3, my_question['题目'])
    if m3:
        for item in m3:
            item = re.sub('“|”| ', '', item)
            keywords.append(item)
    else:
        keywords = []
        
    #问题类型匹配
    for i in type_of_question_dict:
        t4 = re.compile('.*'+i+'.*')
        m4 = re.match(t4,my_question['题目'])
        if m4:
            type_of_question= type_of_question_dict.index(i)
            break
    return {
        '作品':zuopin,
        '诗句':shiju,
        '关键字':keywords,
        '问题类型':type_of_question,
        '类型详解':type_of_question_dict[type_of_question]
    }