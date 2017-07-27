#coding=utf-8
from prettytable import PrettyTable
import urllib2,ssl,json

date="2017-08-01"
train_num="C6012"
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

def station_num(train_num,start_station_code,end_station_code,date):
    """在12306中查询对应列车的编号"""
    url=""
    data=get_api(url)
    open("station_name.txt","w").write(data)
    f=open("station_name.txt","r")
    data=f.read()
    f.close()
    data=json.loads(data)
    stationlist=data.get("data").get("result")
    for i in stationlist:
        j=i.split("|")
        if j[3]==train_num:
            return j[2]

def get_station(train_num,date,start_station_code,end_station_code):
    """12306中查询对应车次的停靠站点信息"""
    train_num=station_num(train_num,start_station_code,end_station_code,date)
    station_url=""
    try:
        data=get_api(station_url)
        open("station.txt","w").write(data)
        f=open("station.txt","r")
        data=f.read()
        f.close()
        data=json.loads(data)
        station_list=data.get("data").get("data")
        x=PrettyTable(["站台","站点","到站时间","出发时间","停留时间"])
        x.align[u"站序"]=1
        x.padding_width=1
        for i in station_list:
            x.add_row([i.get("station_no"),i.get("station_name"),i.get("arriver_time"),i.get("start_time"),i.get("stopover_time")])
        return x
    except:
        return "无法获取，请重试"
x,y=get_station_code(station_name_url,"深圳","昆明")
get_station(train_num,date,x,y)