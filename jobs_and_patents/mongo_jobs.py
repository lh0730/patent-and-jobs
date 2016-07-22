import pymongo

client = pymongo.MongoClient('183.174.228.38')
db = client.Zhaopin
collection = db.ObjJobs
text = collection.find()


count = 0
for item in text:
    if u'JobCategory' in item[u'Json']:
        print str(count) + '\t'+ item[u'Json'][u'JobName'].encode('utf-8') + '\t' + item[u'Json'][u'JobCategory'].encode('utf-8')
    else:
        print str(count) + '\t' + item[u'Json'][u'JobName'].encode('utf-8') + '\t' + 'null'
    count +=1
