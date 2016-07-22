#-*- coding:utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup
import re
from chardet import detect
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


word = re.compile('\>\S+\<')

s=requests.session()
url = 'http://www.chinahr.com/beijing/jobs/'
text = s.get(url).text.encode('utf-8')
text = BeautifulSoup(open('chinahr'),"html.parser",from_encoding="utf-8")
tex = text.findAll(class_='item-til')
nex = text.findAll(class_='item-con')
count = 0
name_list = []
for item in nex:
    x = item.findAll('h4')
    s = item.findAll('div',class_="ul-con")
    for ite in s:
        buffer = []
        s1 = ite.findAll('a')
        for item in s1:
            buffer.append(item.string)
        name_list.append(buffer)

for item in nex:
    name = word.findall(str(tex[nex.index(item)]))[0].strip('<').split('>')[2]
    x = item.findAll('h4')
    for ite in x:
        print name.encode('utf-8') + '\t',
        print ite.string.encode('utf-8') + '\t',
        for item in name_list[count]:
            if item != name_list[count][len(name_list[count])-1]:
                print item+',',
            else:
                print item
        count +=1
