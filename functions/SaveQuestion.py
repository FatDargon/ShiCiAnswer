# -*- coding:utf-8 -*-  
'''
Created on 2017年10月18日

@author: Administrator
'''
from functions.SearchInternet import search_internt, search_in_baike
from tools.GetSoup import Soup
from urllib import quote
from tools.Html_Tools import *
from tools.TextProcess import *
from tools.myprint import pretty_little_list
def kwquery(query):
    #分词 去停用词 抽取关键词
    keywords = []
    answer = []
    text = ''
    # 找到答案就置1
    flag = 0
    # 抓取百度前10条的摘要
    soup_baidu = get_html_baidu('https://www.baidu.com/s?wd='+quote(query))

    for i in range(1,10):
        if soup_baidu == None:
            break
        results = soup_baidu.find(id=i)

        if results == None:
            print "百度摘要找不到答案"
            break
        # print '============='
        # print results.attrs
        # print type(results.attrs)
        # print results['class']
        #判断是否有mu,如果第一个是百度知识图谱的 就直接命中答案
        if results.attrs.has_key('mu') and i == 1:
            # print results.attrs["mu"]
            r = results.find(class_='op_exactqa_s_answer')
            if r == None:
                print "百度知识图谱找不到答案"
            else:
                # print r.get_text()
                print "百度知识图谱找到答案"
                answer.append(r.get_text().strip())
                flag = 1
                break


        #古诗词判断
        if results.attrs.has_key('mu') and i == 1:
            r = results.find(class_="op_exactqa_detail_s_answer")
            if r == None:
                print "百度诗词找不到答案"
            else:
                # print r.get_text()
                print "百度诗词找到答案"
                answer.append(r.get_text().strip())
                flag = 1
                break


        # 百度知道答案
        if results.attrs.has_key('mu') and i == 1:
            r = results.find(class_='op_best_answer_question_link')
            if r == None:
                print "百度知道图谱找不到答案"
            else:
                print "百度知道图谱找到答案"
                url = r['href']
                zhidao_soup = get_html_zhidao(url)
                r = zhidao_soup.find(class_='bd answer').find('pre')
                answer.append(r.get_text())
                flag = 1
                break

        if results.find("h3") != None:
            # 百度知道
            if results.find("h3").find("a").get_text().__contains__(u"百度知道") and (i == 1 or i ==2):
                url = results.find("h3").find("a")['href']
                if url == None:
                    print "百度知道图谱找不到答案"
                    continue
                else:
                    print "百度知道图谱找到答案"
                    zhidao_soup = get_html_zhidao(url)

                    r = zhidao_soup.find(class_='bd answer')
                    if r == None:
                        continue
                    else:
                        r = r.find('pre')
                    answer.append(r.get_text().strip())
                    flag = 1
                    break

            # 百度百科
            if results.find("h3").find("a").get_text().__contains__(u"百度百科") and (i == 1 or i ==2):
                url = results.find("h3").find("a")['href']
                if url == None:
                    print "百度百科找不到答案"
                    continue
                else:
                    print "百度百科找到答案"
                    baike_soup = get_html_baike(url)

                    r = baike_soup.find(class_='lemma-summary')
                    if r == None:
                        continue
                    else:
                        r = r.get_text().replace("\n","").strip()
                    answer.append(r)
                    flag = 1
                    break
        text += results.get_text()

    if flag == 1:
        return answer

    #获取bing的摘要
    soup_bing = get_html_bing('https://www.bing.com/search?q='+quote(query))
    # 判断是否在Bing的知识图谱中
    # bingbaike = soup_bing.find(class_="b_xlText b_emphText")
    bingbaike = soup_bing.find(class_="bm_box")

    if bingbaike != None:
        if bingbaike.find_all(class_="b_vList")[1] != None:
            if bingbaike.find_all(class_="b_vList")[1].find("li") != None:
                print "Bing知识图谱找到答案"
                flag = 1
                answer.append(bingbaike.get_text())
                # print "====="
                # print answer
                # print "====="
                return answer
    else:
        print "Bing知识图谱找不到答案"
        results = soup_bing.find(id="b_results")
        bing_list = results.find_all('li')
        for bl in bing_list:
            temp =  bl.get_text()
            if temp.__contains__(u" - 必应网典"):
                print "查找Bing网典"
                url = bl.find("h2").find("a")['href']
                if url == None:
                    print "Bing网典找不到答案"
                    continue
                else:
                    print "Bing网典找到答案"
                    bingwd_soup = get_html_bingwd(url)

                    r = bingwd_soup.find(class_='bk_card_desc').find("p")
                    if r == None:
                        continue
                    else:
                        r = r.get_text().replace("\n","").strip()
                    answer.append(r)
                    flag = 1
                    break

        if flag == 1:
            return answer

        text += results.get_text()

    # print text


    # 如果再两家搜索引擎的知识图谱中都没找到答案，那么就分析摘要
    if flag == 0:
        #分句
        cutlist = [u"。",u"?",u".", u"_", u"-",u":",u"！",u"？"]
        temp = ''
        sentences = []
        for i in range(0,len(text)):
            if text[i] in cutlist:
                if temp == '':
                    continue
                else:
                    # print temp
                    sentences.append(temp)
                temp = ''
            else:
                temp += text[i]

        # 找到含有关键词的句子,去除无关的句子
        key_sentences = {}
        for s in sentences:
            for k in keywords:
                if k in s:
                    key_sentences[s]=1


        # 根据问题制定规则

        # 识别人名
        target_list = {}
        for ks in key_sentences:
            # print ks
            words = postag(ks)
            for w in words:
                # print "====="
                # print w.word
                if w.flag == ("nr"):
                    if target_list.has_key(w.word):
                        target_list[w.word] += 1
                    else:
                        target_list[w.word] = 1

        # 找出最大词频
        sorted_lists = sorted(target_list.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
        # print len(target_list)
        #去除问句中的关键词
        sorted_lists2 = []
        # 候选队列
        for i, st in enumerate(sorted_lists):
            # print st[0]
            if st[0] in keywords:
                continue
            else:
                sorted_lists2.append(st)

        print "返回前n个词频"
        answer = []
        for i,st in enumerate(sorted_lists2):
            # print st[0]
            # print st[1]
            if i< 3:
                # print st[0]
                # print st[1]
                answer.append(st[0])
        # print answer

    return answer
def get_relation(item,verse):
    content_item = search_in_baike(item)
    content_verse = str(verse)
def XiangGuanXing(verse,my_question):
    list_option=[]
    list_option.append(my_question['A'])
    list_option.append(my_question['B'])
    list_option.append(my_question['C'])
    list_option.append(my_question['D'])
    list_score=[]
    list_abc = ['A','B','C','D']
    for item in list_option:           
        if item != '':
            list_score.append(get_relation(item,verse))
    return my_question[list_abc[list_score.index(max(list_score))]]
def save_question(question_type,verse,my_question):
    
    name = question_type['作品']
    shiju = question_type['诗句']
    keywords = question_type['关键字']
    type_of_question = question_type['问题类型']
    key_of_type = question_type['类型详解']
    question =my_question
    
    key_for_whole_verse = shiju+key_of_type
    if question_type['问题类型']==0 or question_type['问题类型']==1:
        return kwquery(key_for_whole_verse)
    elif question_type['问题类型']==2:
        print '相关性问题'
        return XiangGuanXing(verse,my_question)
    elif question_type['问题类型']==3:
        pass
    elif question_type['问题类型']==4:
        pass
    elif question_type['问题类型']==6:
        pass