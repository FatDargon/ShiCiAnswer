# -*- coding:utf-8 -*-  
'''
Created on 2017年10月18日

@author: Administrator
'''
from functions.ClassfiedQuestion import classfied_question
from functions.InputQuestion import input_question
from functions.SaveQuestion import save_question
from tools.myprint import *
from functions.SearchInternet import search_internt, search_in_baidu


if __name__ == '__main__':
    my_question = input_question()
#     pretty_dict(my_question, ' ')
    question_type = classfied_question(my_question)
    pretty_dict(question_type)
    verse = search_internt(question_type,my_question)
#     pretty_dict(verse)
    save_question(question_type, verse)
#     s = "罗浮山下四时春"
#     search_in_baidu(s)