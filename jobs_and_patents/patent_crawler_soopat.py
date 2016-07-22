#-*- coding:utf-8 -*-

import requests
import pymongo
import time
#from lxml import etree
import re
import random
from bs4 import BeautifulSoup

word = re.compile('\>\S+\<')
'''client = pymongo.MongoClient('183.174.228.38')
db = client.patentDBs
collection = db.patents
test = collection.find()'''
id = []
f = open('new_data','r').readlines()
for line in f:
    content = line.strip().split('\n')
    id.append(content[0])
head = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
for item in id:
    try:
        s = requests.get('http://www.soopat.com/Home/Result?SearchWord=%s&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'%(item))
        soup = BeautifulSoup(s.text,"html.parser", from_encoding='gb2312')
        head = soup.findAll('span',class_="PatentAuthorBlock")
        if head:
            with open('new_result','a') as f:
                f.write(item + '\t' + word.findall(str(head[0]))[1].strip('>').split('<')[0].split('(')[0] + '\n')
                time.sleep(5)
        else:
            with open('new_result','a') as f:
                f.write(item + '\t' + 'null'+'\n')
                time.sleep(10)
    except Exception:
        with open('new_result','a') as f:
            f.write(item + '\t' + 'null'+'\n')
            time.sleep(100)

