#coding:utf-8
import requests

def main():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Cookie':'user_trace_token=20171119092250-7c52ac87-873e-477b-9614-a2b913f6b416; __guid=237742470.164011108602126720.1511054570975.4329; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FPython%2F%3FlabelWords%3Dlabel; LGUID=20171119092255-2bb2e39b-ccc8-11e7-981f-525400f775ce; index_location_city=%E6%9D%AD%E5%B7%9E; JSESSIONID=ABAAABAACEBACDG31953364533185D090B2345CF77E4CD7; _gid=GA1.2.1445483945.1511054574; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511054575,1511055179; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511056132; _ga=GA1.2.1949819308.1511054574; LGSID=20171119092255-2bb2e1ba-ccc8-11e7-981f-525400f775ce; LGRID=20171119094852-cbb292aa-cccb-11e7-9823-525400f775ce; SEARCH_ID=0ff5f878f80548ab8fcd19de4c727287; monitor_count=15',
        'Referer':'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%85%A8%E5%9B%BD#filterBox',

    }
    form_date = {
        'first':'true',
        'pn':'1',
        'kd':'Python'
    }

    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=0'
    result = requests.post(url=url,headers=headers,data=form_date)
    print(result.content.decode("utf-8"))

if __name__ == '__main__':
    main()