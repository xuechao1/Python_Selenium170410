#coding=utf-8
#异常补充
# try :
#     open("asdfasd","r").read()
# except Exception,e:
#     print "error",repr(e),e     #repr打印什么类型的error并且显示错误信息  e显示错误信息
#######################模块################
# import time# 系统自带的模块
# import selenium  #第三方模块
# time.sleep(2)
# print time.time()
# print time.localtime()
#
# #导入模块的方式一  导入多个模块
# import time,random,selenium
# print random.randint(1,100)  #区间包含100，在随机数模块
# print random.randrange(100)  #不包含100，在随机数模块
# num=random.randint(1,100)
# while 1:
#     guess=input("请输入数字")
#     if num<guess:
#         print "大了"
#     elif num>guess:
#         print "smaller"
#     else:
#         print "right"
#导入方式二  导致使用的方式也不一样（资源占用少）
# from time import sleep   #sleep里面的数据来源于time模块
# sleep(2)   #跟time.sleep(2)实现效果是一样的
# import time
# print dir(time)    #查看模块里面的方法
# #print help(time)     #查看模块的介绍 使用方法，在cmd里面也可以用
# import math
# print math.sqrt(9)
# import os
# os.system("ping www.baidu.com")
# print os.getcwd()   #current 当前的路径
###########python对系统的操作############
#创建目录
# os.mkdir("e:\\123123")
# os.system("md e:\\456456")
#判断目录是否存在 再去创建  1、if
# if not os.path.exists("e:\\123789"):
#     os.mkdir("e:\\123789")
# #2/ try
# try:
#     os.mkdir("e:\\123789")
# except Exception,e:
#     print e
#删除空目录
# if os.path.exists("e:\\123789"):
#     os.rmdir("e:\\123789")
#删除非空目录
# import shutil
# if os.path.exists("e:\\123789"):
#     shutil.rmtree("e:\\123789")
#重命名目录
# os.mkdir("e:\\123789")
# os.rename("e:\\123789","e:\\123456789")
#cmd重命名的方法
# os.system("ren  e:\\456456   e:\\789789")
# if not os.path.exists("e:\\123456"):
#     os.mkdir("e:\\123456")
#创建级联目录
# os.makedirs("e:\\a\\b\\c")
# #cmd模式下
# os.system("md e:\\a\\b\\c")
# #删文件
# if os.path.exists("e:\\file.txt"):
#     os.unlink("e:\\file.txt")
#列出指定目录下的所有文件
# file=os.listdir("d:\\")
# print file
# for i in file:
#     filename=i.decode("gbk")
#     if filename[-4:]==".exe":
#         print filename
#decode 解码   encode编码
# c="汉字"
# print repr(c)   #如果是utf-8('\xe6\xb1\x89\xe5\xad\x97')如果是gbk
# print c.decode("gbk")
# #判断是否为文件 还是目录
# print os.path.isdir("e:\\123123")
# print os.path.isfile("e:\\123123")
#########################
# import stat
# fp = open("d:\\resume0504.7z")
# st = os.fstat(fp.fileno())
# print st[stat.ST_CTIME]

# import datetime,time
# print datetime.datetime.now()
# print datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m%d %H:%M:%S')
# #时间戳转换格式化时间
# print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(1493880515))

# import os,datetime,time,stat
# localtime=time.localtime(1493880515)
# localtime2 = time.strftime("%Y-%m-%d",localtime)
# print localtime2
# list = os.listdir("e:\\")
# while 1:
#     for i in list:
#         print repr(i)
#         print i.decode("gbk")
#         if os.path.isfile(i)!=file:
#             size1=os.stat(i).st_size
#             size=os.path.getsize(size1)
#             print i,localtime2,size1
#         else:
#             continue
#     print i,localtime2,size1
from Public.public_Basic import *
kill_process()
foo1()
foo2()
foo3()
foo4()
PathRoad()
add()






