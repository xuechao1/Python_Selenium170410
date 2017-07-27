#coding=utf-8
##############################################文件读写###################################################
#写（当前目录，脚本在哪里就写在哪里）
#.当前目录  ..上层目录
#w模式 就是全新写文件
# fileobj=open("./file.txt","w")   #第一个参数文件名，写的方式打开
# print fileobj,type(fileobj)
# str1="你不是好人"
# fileobj.write(str1)    #吧字符写入文件里面
# fileobj.close()        #文件操作完成后记得关闭

# #指定绝对路径  （路径要加双斜线）
# fileobj=open("e:\\file.txt","w")   #第一个参数文件名，写的方式打开
# fileobj=open("e:\\file.txt","w")

# print fileobj,type(fileobj)
# str1="asdf12345"
# fileobj.write(str1)    #吧字符写入文件里面
# fileobj.close()        #文件操作完成后记得关
#
# #绝对前面加 r 用来识别绝对路径的
# fileobj=open(r"e:\file1.txt","w")   #第一个参数文件名，写的方式打开
# print fileobj,type(fileobj)
# str1="你不是好人111"
# fileobj.write(str1)    #吧字符写入文件里面
# fileobj.close()        #文件操作完成后记得关闭
#
# #写网页
# fileobj=open(r"e:\file1.html","w")   #第一个参数文件名，写的方式打开
# print fileobj,type(fileobj)
# str1="""
# <html>
# <body>
# <input  type="text" value="123" id="user">
# <br><br>
# <button id="loginbtn">login</button>
# </body>
# </html>
# """
# fileobj.write(str1)    #吧字符写入文件里面
# fileobj.close()        #文件操作完成后记得关闭
#
# #写文件夹
# import os
# path1="e:\\123\\"
# if not os.path.exists(path1):
#     os.mkdir(path1)
# fileobj=open(path1+"file1.txt","w")   #第一个参数文件名，写的方式打开
# print fileobj,type(fileobj)
# str1="qweqweqwe"
# fileobj.write(str1)    #吧字符写入文件里面
# fileobj.close()        #文件操作完成后记得关闭
#
# #写中文目录（处理中文前面加u unicode编码格式）
# fileobj=open(u"e:\\测试\\file1.txt","w")   #第一个参数文件名，写的方式打开
# print fileobj,type(fileobj)
# str1="隔壁老王"
# fileobj.write(str1)    #吧字符写入文件里面
# fileobj.close()        #文件操作完成后记得关闭

# #追加  a
# #写中文目录（处理中文前面加u unicode编码格式）
# fileobj=open(u"e:\\测试\\file1.txt","a")   #第一个参数文件名，写的方式打开
# print fileobj,type(fileobj)
# str1="隔壁\t老王"
# fileobj.write(str1+'\n')    #吧字符写入文件里面
# fileobj.close()        #文件操作完成后记得关闭
#
# #读文件
# fileobj=open(r"C:\Users\Administrator\Desktop\file.txt","r")   #第一个参数文件名，读的方式打开
# print fileobj
# print fileobj.read()
# print fileobj.readlines()
# for i in fileobj.readlines():
#     print i
#
# #读指定行
# import linecache   #导入模块
# print  linecache.getline(u"e:\\测试\\file1.txt",3)
#
# #win7英文版的汉字乱码问题
# fileobj=open(r"C:\Users\Dongboduan\Desktop\file.txt","r")   #第一个参数文件名，读的方式打开
# print fileobj
# print fileobj.read().decode("utf-8").encode('gbk')

#读写二进制文件
#http://172.16.3.158/ecshop/data/afficheimg/1462958213922967180.jpg
# import urllib2
# data=urllib2.urlopen("http://172.16.3.158/ecshop/data/afficheimg/1462958213922967180.jpg").read()
# file=open("123.jpg","wb")
# file.write(data)
# file.close()

#读二进制
# file=open("C:\\Windows\\notepad.exe","rb")
# print file.read()

