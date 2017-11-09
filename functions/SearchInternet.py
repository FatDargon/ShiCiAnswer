# -*- coding:utf-8 -*-  
'''
Created on 2017年10月18日

@author: Administrator
'''
from urllib import quote
from tools.GetSoup import Soup
from tools.myprint import pretty_list, pretty_little_list
import re
def search_in_gushici(query_str):
    base_url ="http://so.gushiwen.org/search.aspx?value="+quote(query_str)
    print base_url
    soup1 = Soup(url = base_url,encoding='',host ="so.gushiwen.org").get_soup()
#     print soup
    new_url = ''
    try:
        new_url = soup1.find("div",class_="sons").find("a",href=re.compile("view"))['href']
        new_url = "http://so.gushiwen.org"+new_url
    except:
        print "error in search gushici"
    soup2 = Soup(url = new_url,encoding='',host ="so.gushiwen.org").get_soup()
    
    data = {"题目":"",
     "作者":"",
     "作者详情":"",
     "朝代":"",
     "诗文":"",
     "材料":"",
     "关键字":"",
    }
    title = soup2.find('h1').get_text().strip()
#     print title
    tmp1 = soup2.find("p",class_="source").find_all("a")
    chaodai = tmp1[0].get_text().strip()
    zuozhe  = tmp1[1].get_text().strip()
#     print chaodai
#     print zuozhe
    tmp3 = soup2.find_all('div',class_='contyishang')

    cailiao =''
    for t in tmp3:
        t.h2.extract()
        text=t.get_text().strip()
        text =re.sub('\s','',text)   
        cailiao+=text
#     print yiwen
#     print beijing
#     print shangxi  
    zuozhexiangqing =''
    tmp4 =soup2.find('div',class_="sonspic").find_all('p')
    for t in tmp4:
        zuozhexiangqing+=t.get_text().strip()    
#     print zuozhexiangqing
    tags = soup2.find('div',class_='tag').get_text().strip() 
    tags = re.sub('\s','',tags)   
#     print tags
    tmp5 = soup2.find('div',class_='contson').get_text().strip()   
    
    data['题目']=title.encode('utf-8')
    data['作者']=zuozhe.encode('utf-8')
    data['作者详情']=zuozhexiangqing.encode('utf-8')
    data['朝代']=chaodai.encode('utf-8')
    data['诗文']=tmp5.encode('utf-8')
    data['关键字']=tags.encode('utf-8')
    data['材料']=cailiao.encode('utf-8')
    return data

    
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
    type_of_question = question_type['问题类型']
    key_of_type = question_type['类型详解']
    question =my_question
    
    key_for_whole_verse = name+shiju
    verse = search_in_gushici(shiju)
    return verse