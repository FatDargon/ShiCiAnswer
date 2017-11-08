# -*- coding:utf-8 -*-  
'''
Created on 2017年10月18日

@author: Administrator
'''
from tools.GetSoup import Soup
from urllib import quote
def search_in_baidu(words):
    base_url = "https://www.baidu.com/s?ie=utf-8&wd="
    url = base_url + quote(words)
    print url
    soup = Soup(url).get_soup()
    hanyu = soup.find('div',class_='result-op c-container')
    print hanyu
        
def search_internt(question_type,my_question):
    '''
    question_type :
        '作品':zuopin,
        '诗句':shiju,
        '关键字':keywords,
        '问题类型':type_of_question,
        '类型详解':type_of_question_dict[type_of_question]
        
    my_question : 
        '题目':'“罗浮山下四 时春”的《下一句》杀对方“快乐”撒大家发是“什么”? ',
        '选项':'0',
        'A':'',
        'B':'',
        'C':'',
        'D':'', 
    '''
    name = question_type['作品']
    shiju = question_type['诗句']
    keywords = question_type['关键字']
    question =my_question
    if name != '':
        search_in_baidu(name)
    pass
        