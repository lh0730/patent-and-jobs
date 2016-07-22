#-*-coding:utf-8-*-
import requests
import pymongo
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

client = pymongo.MongoClient('183.174.xxx.xx')
db = client.patentDBs
collection = db.patents.find()
for item in collection:
    if u"分类号" in item:
        print item[u"申请号"] + '\t' + item[u'标题'] + '\t' + item[u"分类号"]
