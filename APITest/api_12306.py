#coding=utf-8
from prettytable import PrettyTable
import urllib2,ssl,json

date="2017-08-01"
start_station="深圳北"
end_station='长沙南'
station_name_url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9019"

def get_api(url):
    context = ssl._create_unverified_context()  # 解决请求https的时候，需要验证证书；第一种方式就是创建一个未验证的证书
    req = urllib2.Request(url)  # 定义一个请求信息
    res = urllib2.urlopen(req, context=context)  # 打开这个请求信息，并接收返回的数据
    return res.read()  # 从内存读取服务器返回的数据

def get_station_code(url,start_station_name,end_station_name):
    data=get_api(url)
    open("e:\\station_name.txt","w").write(data)
    f=open("e:\\station_name.txt","r")
    data=f.read()
    f.close()
    for i in data.split("@"):
        if i.find("|")!=-1:
            if start_station_name==i.split("|")[1]:
                start_station_code=i.split("|")[2]
            if end_station_name==i.split("|")[1]:
                end_station_code=i.split("|")[2]
    return start_station_code,end_station_code

def get_ticket(date, code1, code2):
    ticket_url="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT"%(date,code1,code2)
    data=get_api(ticket_url)
    data=json.loads(data)
    ticklist=data.get("data").get("result")
    x=PrettyTable(["车次","商务座","一等座","二等座"])
    x.align[u"车次"]=1
    x.padding_width=1
    for i in ticklist:
        j=i.split("|")
        x.add_row([j[3],j[32],j[31],j[30]])
    print x

# 31一等座 30二等座 32商务座 26无座  23硬座   29软卧  28硬卧
x,y=get_station_code(station_name_url,"深圳","厦门")
get_ticket(date,x,y)
