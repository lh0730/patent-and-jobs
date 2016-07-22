import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

f = open('result','r').readlines()
fp = open('jobs','r').readlines()
for line in fp:
    content = line.strip().split('\t')
    if len(content) > 2:
        key = content[0]
        name = content[1]
        categ = content[2]
        for ll in f:
            cont = ll.strip().split('\t')
            old_key = cont[0]
            if key == old_key:
                print key + '\t' + name + '\t' + categ + '\t' + cont[1]
 
