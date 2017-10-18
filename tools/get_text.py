# -*- coding:utf-8 -*-  
'''
Created on 2017年9月17日

@author: Administrator
'''
def read_file(my_file_path = '../data/source.txt'):
    return_list = []
    tmp_dict = {'source_name':'', 'source_url':''}
    my_file_path = my_file_path
    with open(my_file_path, 'r') as f:
        for line in f.readlines():
            tmp_list = line.split('：')
            tmp_dict['source_name'] = tmp_list[0]
            tmp_dict['source_url'] = tmp_list[1]
            return_list.append(tmp_dict)
            tmp_dict = {'source_name':'', 'source_url':''}
    return return_list
        
