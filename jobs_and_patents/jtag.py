import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

f=open('jobs_tag','r').readlines()
fp = open('jobs','r').readlines()
for line in fp:
    content=line.strip().split('\t')
    if len(content) > 2:
        word = content[2].strip().split('/')
        key = content[0]
    if word:
        for item in word:
            for line in f:
                buffer = []
                tag_list = line.strip().split('\t')
                name1 = tag_list[0]
                name2 = tag_list[1]
                tags = tag_list[2].strip().split(',')
                for ite in tags:
                    buffer.append(ite.strip())
                for xkey in buffer:
                    if item.strip() == xkey.strip():
                        print key+ '\t' + name1 + '|' + name2 + '|' + xkey
