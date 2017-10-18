# -*- coding:utf-8 -*-  
'''
Created on 2017年10月18日

@author: Administrator
'''
from functions.ClassfiedQuestion import classfied_question
from functions.InputQuestion import input_question
from functions.SaveQuestion import save_question
from tools.myprint import *


if __name__ == '__main__':
    my_question = input_question()
    pretty_dict(my_question, ' ')