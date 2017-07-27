#coding=utf-8
from prettytable import PrettyTable
import urllib2,ssl,json

date="2017-08-01"
departureCity="深圳"
arrivalCity='上海'
fly_url="https://flight.qunar.com/twell/flight/OneWayFlight_Info.jsp?departureCity=%E6%B7%B1%E5%9C%B3&arrivalCity=%E6%98%86%E6%98%8E&departureDate=2017-07-29&returnDate=2017-07-31"

def get_api(url):
    context = ssl._create_unverified_context()  # 解决请求https的时候，需要验证证书；第一种方式就是创建一个未验证的证书
    req = urllib2.Request(url)  # 定义一个请求信息
    res = urllib2.urlopen(req, context=context)  # 打开这个请求信息，并接收返回的数据
    return res.read()  # 从内存读取服务器返回的数据

def get_station_code(url,departureCity_name,arrivalCity_name):
    data=get_api(url)
    open("e:\\station_name.txt","w").write(data)
    f=open("e:\\station_name.txt","r")
    data=f.read()
    f.close()
    for i in data.split("@"):
        if i.find("|")!=-1:
            if departureCity_name==i.split("|")[1]:
                departureCity_code=i.split("|")[2]
            if arrivalCity_name==i.split("|")[1]:
                arrivalCity_code=i.split("|")[2]
    return departureCity_code,arrivalCity_code

def get_ticket(date, code1, code2):
    ticket_url="https://flight.qunar.com/twell/flight/OneWayFlight_Info.jsp?departureCity=%s&arrivalCity=%s&departureDate=%s&returnDate=2017-08-20"%(code1,code2,date)
    data=get_api(ticket_url)
    data=json.loads(data)
    ticklist=data.get("carrierInfo").get("CZ")
    x=PrettyTable(["zh","full","maxvendors","key"])
    x.align["zh"]=1
    x.padding_width=1
    for i in ticklist:
        j=i.split("|")
        x.add_row([j[5],j[6],j[7],j[8]])
    print x

x,y=get_station_code(fly_url,"深圳","厦门")
get_ticket(date,x,y)
