# -*- coding: UTF-8 -*-
import requests
import xlwt
headers = {      #头部分用来模拟浏览器，包括'User-Agent'，浏览器信息，'Referer'来源，'Cookie' 缓存信息
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Cookie':'user_trace_token=20170926134508-daf8d2e1-a27d-11e7-ac91-525400f775ce; LGUID=20170926134508-daf8d7b1-a27d-11e7-ac91-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGGABCB0B1EC33C40CD9ED0ACD99A669777BD37; TG-TRACK-CODE=search_code; _gat=1; _gid=GA1.2.1406285458.1506404713; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1506404708,1506479284,1506479293; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1506481150; _ga=GA1.2.583885505.1506404708; LGSID=20170927102811-81f3f0f9-a32b-11e7-aefd-525400f775ce; LGRID=20170927105908-d4f5f541-a32f-11e7-92ef-5254005c3644; SEARCH_ID=2c80705036554d82a34a71475dfae529'

}
def getJobList(page):
    data={
        'first': 'false',
        'pn': page,
        'kd':'python'
    }
    #post请求的三个变量 url，data信息，headers信息
    res = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0',data=data,headers=headers)
    result=res.json()
    jobs = result['content']['positionResult']['result']  #结合浏览器查看网页的结构
    return jobs
    # print(res.text)

#创建excel表
excel1 = xlwt.Workbook()
sheet1 = excel1.add_sheet('la',cell_overwrite_ok=True) #设置单元格属性


#需要爬取的关键字，设置excel表头
sheet1.write(0, 0, 'companyFullName')
sheet1.write(0, 1, 'firstType')
sheet1.write(0, 2, 'positionName')
sheet1.write(0, 3, 'education')
sheet1.write(0, 4, 'financeStage')
sheet1.write(0, 5, 'city')
sheet1.write(0, 6, 'district')
sheet1.write(0, 7, 'industryField')

#循环遍历翻页
n = 1
for page in range(1,10):
        print (page)  #打印页码
        for job in getJobList(page):
            # print (page)  #打印每页的内容
            print(job)
            #将想要获取的内容写入到excel
            sheet1.write(n, 0, job['companyFullName'])
            sheet1.write(n, 1, job['firstType'])
            sheet1.write(n, 2, job['positionName'])
            sheet1.write(n, 3, job['education'])
            sheet1.write(n, 4, job['financeStage'])
            sheet1.write(n, 5, job['city'])
            sheet1.write(n, 6, job['district'])
            sheet1.write(n, 7, job['industryField'])
            n+=1
        import time
        # time.sleep(2)
    #print (job['companyFullName'])
#将excel表保存到桌面
excel1.save('lagou.xls')