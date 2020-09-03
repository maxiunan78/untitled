#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
def c():
    filepath = os.path.realpath(__file__)
    print os.path.realpath(__file__)
    print os.path.split(filepath)[0]
    filepath1 = os.path.split(filepath)[0]
    filepath2 = os.path.join(os.path.split(filepath)[0],"text.txt")
    f = open(filepath2,'r')
    # content1 = f.read()
    # print content1
    content = []
    inputfile = f.readlines()
    f.close()
    for line in inputfile:
        # print line
        content.append(line)
    print content
    print content[-1]
    content[-1] = content[-1] + '\n'
    print 'a'.join('b')
    print content
    print (set(content))
    newcontect =  ''.join(set(content))
    print newcontect
    # print list(content)
    f = open(os.path.join(os.path.split(filepath)[0],"text1.txt"),'w')
    f.write(newcontect)
    f.close()
if __name__ == '__main__':
    c()
