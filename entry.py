# -*-coding:utf-8 -*-

import requests,json
for i in range(1):
    url='http://123.56.13.177:9090/hjlc-api/api/eloan/submit'
    result={
    "applyId":"applyId1531106900044312",
    "sourceId":"FL",
	"borrowerInfo": {
		"age": "99",
		"corpName": "阿道夫",
		"corpPhone": "028-88888888",
		"corpPlaceAddr": "����·42��",
		"corpPlaceCity": "�ɶ���",
		"corpPlaceCounty": "��ţ��",
		"corpPlacePovice": "�Ĵ�ʡ",
		"corpPost": "����",
		"corpType": "����",
		"education": "����",
		"gender": "��",
		"idNo": "230805198901039999",
		"industry": "����",
		"marital": "δ��",
		"mateIdNo": "230805198901038888",
		"mobile": "17099999999",
		"name": "auto5825",
		"name1": "auto15825",
		"name2": "auto25825",
		"nation": "��",
		"permanentAddressCity": "̨����",
		"permanentAddressCounty": "̨̨��",
		"permanentAddressDetail": "��·42��",
		"permanentAddressPovice": "̨��ʡ",
		"personalIncome": "0-3000",
		"phoneNum1": "17099999998",
		"phoneNum2": "17099999997",
		"receiverAddressCity": "�ɶ���",
		"receiverAddressCounty": "ۯ����",
		"receiverAddressDetail": "����·556��",
		"receiverAddressPovice": "�Ĵ�ʡ",
		"relation1": "����",
		"relation2": "ĸ��",
		"sourceOfRepayment": "��������",
		"termOfValidity": "2020-01-01",
		"workingLife": "5��"
	},
	"creditInfo": {
		"creditAccount": "zhanghao3821",
		"creditPasswd": "pwd3821",
		"debtAmount": 0.00,
		"historyOverdueNum": 0,
		"insuranceAccount": "baodan3821",
		"insurancePassWord": "bdpwd3821",
		"insuranceType": "����",
		"isExceed": "0",
		"isOverdue": "0",
		"settleAccountNum": 0,
		"threeMonthInquiries": 3,
		"vCode": "code3821"
	},
	"loanInfo": {
		"applyLoanAmount": 200000.00,  #�ͻ�������
		"category": "100",
		"channel": "1003",
		"channelLoanAmount": 100000.00, #���������Ŷ�� ,
		"firstLoanAmount": 1000000.00,
		"firstLoanBalance": 50000.00,
		"guaranteeType": "����",
		"initialValue": 1200000.00,
		"loanUse": "����",
		"mortgageStatus": "1",
		"rateCode": "482",
	},
	"mortgageInfo": {
		"coOwners": [{
			"ownerCorpAddressCity": "��ľ˹��",
			"ownerCorpAddressCounty": "������",
			"ownerCorpAddressDetail": "������100��",
			"ownerCorpAddressPovice": "������ʡ",
			"ownerCorpName": "��ݼ��ŵ�",
			"ownerCorpPost": "����",
			"ownerIdNo": "230805198901038888",
			"ownerMobile": "17088889999",
			"ownerName": "owner8532"
		}, {
			"ownerCorpAddressCity": "��ľ˹��",
			"ownerCorpAddressCounty": "������",
			"ownerCorpAddressDetail": "������100��",
			"ownerCorpAddressPovice": "������ʡ",
			"ownerCorpName": "��ݼ��ŵ�",
			"ownerCorpPost": "����",
			"ownerIdNo": "230805198901038888",
			"ownerMobile": "17088889999",
			"ownerName": "owner4219"
		}],
		"estateAreaCity": "�ɶ���",
		"estateAreaCounty": "ۯ����",
		"estateAreaDetail": "����·900��",
		"estateAreaPovice": "�Ĵ�ʡ",
		"floor": 5,
		"mortgageType": "1",
		"totalFloor": 20,
		"useStatus": "��ס",
		"warrants": "chanquan7386"
	}
}
    data={
        "requestData":json.dumps(result),"skip*!^^fh.h23123k$d":"1",
    }
    res=requests.post(url,data=data)
    print(res.content)
