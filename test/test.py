# -*- coding:utf-8 -*-  
'''
Created on 2017年10月18日

@author: Administrator
'''
from functions.ClassfiedQuestion import classfied_question
from functions.InputQuestion import input_question
from functions.SaveQuestion import save_question
from tools.myprint import *
from functions.SearchInternet import search_internt


if __name__ == '__main__':
    my_question = input_question()
#返回结构性问题，作为问题本体
#{
#       '题目':'“咬定青山不放松 ,立根原在破岩中。千磨万 击还坚劲 ，任尔东西南北 风。”描写的是哪种植物? ',
#       '选项':'3',
#       'A':'松树',
#       'B':'梅花',
#       'C':'竹子',
#       'D':'', 
#       } 
    print '问题整理'
    print '*'*30
    pretty_dict(my_question, ' ')
    question_type = classfied_question(my_question)
#详细分类问题
#{
#  "类型详解": "下一句",
#  "诗句": "罗浮山下四时春",
#  "关键字": ['\xe5\xbf\xab\xe4\xb9\x90', '\xe4\xbb\x80\xe4\xb9\x88'],
#  "问题类型": 1,
#  "作品": ""
# }
    print '问题分类'
    print '*'*30
    pretty_dict(question_type)
    pretty_little_list(question_type['关键字'])
    verse = search_internt(question_type,my_question)
    print '搜索全诗'
    print '*'*30
    pretty_dict(verse)
#     {
#  "题目": "黄鹤楼送孟浩然之广陵",
#  "关键字": "唐诗三百首，小学古诗，写景，写水，长江，地名，离别，友情，送别",
#  "朝代": "唐代",
#  "作者": "李白",
#  "材料": "译文老朋友向我频频挥手，告再现来▲",
#  "诗文": "故人西辞黄鹤楼，烟花三月下扬州。孤帆远影碧空尽，唯见长江天际流。 (唯 通：惟)",
#  "作者详情": "李白李白（701年－762年，被后人誉为“诗仙”。祖籍陇西有纪念馆。"
# }
    print "问题答案"
    print '*'*30
    answer = save_question(question_type, verse,my_question)
    pretty_little_list(answer)
#     s = "罗浮山下四时春"
#     search_in_baidu(s)