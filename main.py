import requests
import json
import io

baseurl = 'http://www.chamc.com.cn/zctjdata/assetinfopublish/assetpromotion?companyname=&provincename=&buytotalBegin=&buytotalEnd=&capitalBegin=&capitalEnd=&imgdescription=&pledgetype=&guarantystyle=&industry=&arecode=&mortgageline=&bankruptcy=&lawsuitprogress=&seizingstate=&linkmode=&size=100&page={}'

with open('report.txt', 'w', encoding='utf-8') as file:
    file.write('债务人名称|所在地区|担保方式|资产类型|债权总额（元）|结束时间\n')
    for i in range(0, 72):
        url = baseurl.format(i)
        response = requests.get(url)
        jsondata = response.json()
        for item in jsondata['content']:
            file.write('{}|{}|{}|{}|{}|{}\n'.format(
                item['companyname'],
                item['provincename'], 
                item['guarantystyle'],
                item['pledgekind'],
                item['buytotal'],
                item['expirydate']))