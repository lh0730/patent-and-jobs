#-*- coding:utf-8 -*-

import requests
import pymongo
import time
from lxml import etree
import re
import random

word = re.compile('分类号\：\S+')
'''client = pymongo.MongoClient('183.174.228.38')
db = client.patentDBs
collection = db.patents
test = collection.find()'''
id = []
f = open('data','r').readlines()
for line in f:
    content = line.strip().split('\n')
    id.append(content[0])
head = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
html = "http://epub.sipo.gov.cn/patentoutline.action"
cookies = dict(cookies_are='working')
s=requests.session()
count = 0
for item in id:
    try:
        key = 'AN,DPR,IAN+=\''+item+'%\' or ABH=\''+item+'\''
        s.get(html)
        data = {'showType':'1','strWhere':str(key),'numSortMethod':'4','pageSize':'3','pageNow':'1'}
        result = s.post(html,data=data,cookies=cookies).content
        with open('result','a') as f:
            if word.findall(result):
                f.write(str(item) + '\t')
                f.write(word.findall(result)[0].split(';')[0].split('：')[1].split('(')[0].strip('&nbsp')+'\n')
            else:
                time.sleep(50)
    except Exception:
        with open('result','a') as f:
            f.write(str(item) + '\t' + 'null' + '\n')
        time.sleep(100)
    count = count + 1
        
