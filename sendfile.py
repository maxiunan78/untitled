# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests
import base64
import json

def basefile1(yfile):
	with open(yfile,'rb') as f:
		base64_data = base64.b64encode(f.read())
		print base64_data
	return base64_data

def sendfile():
	url = 'http://123.56.13.177:9090/hjlc-api/apieloan/submitImg'
	f1 = 'C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\User\daikuan\IMG_5849(20191129-144317).PNG'
	f2 = 'C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\User\daikuan\IMG_5858(20191201-210713).PNG'
	fileInfo = [
				{'type':'101',base64Img:basefile(f1),sortNo:'1'},
				{'type':'104',base64Img:basefile(f2),sortNo:'2'}
				]
	result = {
			'requestId':'applyId1531106900044314',
			'tatal':2,
			'files':fileInfo
			}
	data={
        "requestData":json.dumps(result),"skip*!^^fh.h23123k$d":"1",
    	}
    res=requests.post(url,data=data)
    print(res.content)

if __name__ == '__main__':
	f1 = "C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\User\daikuan\IMG_5849(20191129-144317).PNG"
	basefile1(f1)
	sendfile()

