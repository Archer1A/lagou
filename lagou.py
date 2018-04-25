#coding:utf-8
import json

import requests
import time
from xlwt  import *
from lxml import etree
COUNT = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie': 'user_trace_token=20170922185141-04566935-9f84-11e7-a226-525400f775ce; LGUID=20170922185141-04566fdd-9f84-11e7-a226-525400f775ce; _ga=GA1.2.821244537.1506077500; JSESSIONID=ABAAABAACEBACDG0B2A07FB0B86DB2C9058587E9CF40FC3; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524488209; LGSID=20180423205647-c8287626-46f5-11e8-99d3-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DQjrhpv1w1zbf5pebmPs_b2nAp4cDpqcZK3e89VPkUDm%26wd%3D%26eqid%3De0b759ed00087602000000045addd806; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gid=GA1.2.1371465779.1524488210; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; LGRID=20180423205704-d23dd02e-46f5-11e8-99d3-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524488227; SEARCH_ID=b9d50fb70301408aa872c6a7d8401a27',
    'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%85%A8%E5%9B%BD#filterBox',

}
def main():
    global COUNT
    file = Workbook(encoding='utf-8')
    table = file.add_sheet('aaa')


    for i in range(1,31):
        form_date = {
            'first':'true',
            'pn':str(i),
            'kd':"电商推广"
        }

        url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'
        result = requests.post(url=url,headers=headers,data=form_date)
        print(result.text)
        print("正在爬取第%d页"%(i))

        js = json.loads(result.text)
        try:
            positions = js["content"]["positionResult"]["result"]
            for position in positions:
                #print(position)
                table.write(COUNT,0,str(position["positionName"]))
                table.write(COUNT,1,str(position["education"]))
                table.write(COUNT,2,str(position["city"]))
                table.write(COUNT,3,str(position["companyShortName"]))
                table.write(COUNT,4,str(position["salary"]))
                table.write(COUNT,5,str(position["positionAdvantage"]))
                table.write(COUNT,6,str(position["companyLabelList"]))
                table.write(COUNT,7,str(position["companyLabelList"]))
                table.write(COUNT,8,getDetail(position["positionId"]))
                print("==============正在爬取%s的职位描述=============="%(str(position["positionName"])))
                COUNT += 1
        except KeyError:
            print("lllll")
        time.sleep(4)

    file.save("detail.xls")

def  getDetail(id):
    time.sleep(1)
    url = "https://www.lagou.com/jobs/%s.html"%(id)
    res = requests.get(url=url, headers = headers)
    #print(res.text)
    tree = etree.HTML(res.text)
    content=tree.xpath('//*[@id="job_detail"]/dd[2]/div/*/text()')
    return str(content)



if __name__ == '__main__':
    main()
    #getDetail(4451893)