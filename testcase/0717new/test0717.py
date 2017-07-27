#coding=gbk
#异常补充
# try:
#     open("asdfasd","r").read()
# except Exception,e:
#     print "error",repr(e),e   #repr打印什么类型的error并且显示错误信息    e显示错误信息
#
###################################################模块########################################################
# import time   #系统自带的模块
# import selenium #第三方的模块
# # time.sleep(2)
# # print time.time()    #1970-1-1到目前的秒数，时间戳
# # print type(time.localtime())
# #导入模块的方式一
# import time,random,selenium  #导入多个模块 逗号隔开
# print random.randint(1,100)  #区间包含100在随机数模块
# print random.randrange(100)  #不包含100
# num=random.randint(1,100)
# while 1:
#     guess=input("请输入数字：")
#     if guess<num:
#         print "你猜的有点小"
#     elif  guess>num:
#         print "你猜的有点大"
#     else:
#         print "你猜对了"
#导入方式二，导致使用的方式也会不一样（资源占用少一些）
from time import sleep
#sleep(2)   #跟time.sleep(2)实现效果是一样的
# import time
# print dir(time)  #查看模块里面的方法
# #print help(time) #查看模块的介绍 使用方法 在cmd里面也可以用
# import math
# print math.sqrt(9)
# import os
# os.system("ping www.baidu.com")
# print os.getcwd()  #current 当前的路径
# print os.name

#####################################python对系统的操作##########################
#创建目录
import os
#判断目录是否存在(os.path.exists 可以判断目录和文件) 再去创建1.if
# if not os.path.exists("e:\\123123"):
#     os.mkdir("e:\\123123")
# #2.try
# try:
#     os.mkdir("e:\\333")
# except Exception,e:
#     print e
# # #删除空目录
# if os.path.exists("e:\\123123"):
#     os.rmdir("e:\\333")
# #删除非空目录
# import shutil
# if os.path.exists("e:\\333"):
#     shutil.rmtree("e:\\333")
# #cmd删除非空目录方法
# os.system("rd /s /q e:\\333")
# #重命名目录
# os.mkdir("e:\\123")
# os.rename("e:\\123","e:\\456")
# #cmd的重命名方法
# os.system("ren   e:\\456   e:\\789")

#创建级联目录
# os.makedirs("e:\\11\\22\\33")
# #cmd模式下
# os.system("md e:\\a\\b\\c")
#删文件
# if os.path.exists("e:\\file.txt"):
#     #os.remove("e:\\file.txt")
#     os.unlink("e:\\file.txt")

#decode解码  encode编码
# c="汉字"
# print repr(c)   #如果是utf-8（'\xe6\xb1\x89\xe5\xad\x97'） 如果是gbk的话（'\xba\xba\xd7\xd6'）
# print c.decode("gbk")
#
# #列出指定目录下的所有文件
# file= os.listdir("d:\\")
# print file
# for i in file:
#     filename=i.decode("gbk")
#     if filename[-4:]==".exe":
#         print filename
# #判断是否为文件 还是目录
# print os.path.isdir("e:\\123123")
# print os.path.isfile("e:\\123123")
#
# #获取文件的创建时间；大小等等
# import stat
# fp = open("d:\\resume0504.7z")
# st = os.fstat(fp.fileno())
# print  st[stat.ST_CTIME],st[stat.ST_SIZE]
#
# import datetime,time
# print datetime.datetime.now()
# print datetime.datetime.strftime(datetime.datetime.now(), '%Y/%m/%d %H:%M:%S')
# #时间戳转换成格式化时间
# print time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(1493880515))

#如果自定义的模块有层级关系，那么导入的时候用from
#在自定义模块目录里面，需要增加一个__init__.py文件（或者用编辑器新建一个package）
#
# from project2017_02.Public.public_base import *
# filename= listTxtInPath("d:\\")
# for i in filename:
#     print i
