# -*- coding:utf-8 -*-  
'''
Created on 2017年10月18日

@author: Administrator
'''
from functions.ClassfiedQuestion import classfied_question
from functions.InputQuestion import input_question
from functions.SaveQuestion import save_question


if __name__ == '__main__':
    my_question = input_question()
    question_type = classfied_question(my_question)
    my_answer,my_analysis = save_question(question_type,my_question)
