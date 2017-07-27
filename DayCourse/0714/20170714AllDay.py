# coding=utf-8
##############################################文件读写###################################################
# 写（当前目录，脚本在哪里就写在哪里）
# .当前目录  ..上层目录
# w模式 就是全新写文件
# fileobj=open("./file.txt","w")   #第一个参数文件名，写的方式打开
# print fileobj,type(fileobj)
# str1="你不是好人"
# fileobj.write(str1)    #吧字符写入文件里面
# fileobj.close()        #文件操作完成后记得关闭
#
# #指定绝对路径  （路径要加双斜线）
# fileobj=open("e:\\file.txt","w")   #第一个参数文件名，写的方式打开
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
# fileobj=open(r"C:\Users\Dongboduan\Desktop\file.txt","r")   #第一个参数文件名，读的方式打开
# print fileobj
# print fileobj.read()
# # print fileobj.readlines()
# # for i in fileobj.readlines():
# #     print i
#
# #读指定行
# import linecache   #导入模块
# print  linecache.getline(u"e:\\测试\\file1.txt",3)
#
# #win7英文版的汉字乱码问题
# fileobj=open(r"C:\Users\Dongboduan\Desktop\file.txt","r")   #第一个参数文件名，读的方式打开
# print fileobj
# print fileobj.read().decode("utf-8").encode('gbk')

# 读写二进制文件
# http://172.16.3.158/ecshop/data/afficheimg/1462958213922967180.jpg
# import urllib2
# data=urllib2.urlopen("http://172.16.3.158/ecshop/data/afficheimg/1462958213922967180.jpg").read()
# file=open("123.jpg","wb")
# file.write(data)
# file.close()

# 读二进制
# file=open("C:\\Windows\\notepad.exe","rb")
# print file.read()

###################################################函数###############################################################
# 一小段程序  实现一个小功能
# 可重用  可被反复的调用
# def  函数名 括号 （形参）：

import os


def kill_process(name):
    """函数的注释，此函数windows专杀进程函数，传入进程名即可"""
    os.system('taskkill  /f  /im  ' + name + '*   >nul   2>nul')


def calc_year(year):
    """计算闰年的函数，闰年返回0 平年返回1"""
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 0
    else:
        return 1


# 函数的入参
def foo2(a=1, b=8, c=5):  # 形参默认值
    return a + b + c


# print foo2(1,2,3)  #实参

# 函数定义的时候 如果形参有默认值；在调用函数的时候，首先按传递的参数进行运算；如果没有传递参数就取默认值运算
# print foo2(1,2)  #没有默认值的时候，就取默认值
# print foo2(b=8,c=3)  #如果你想传递指定的参数，那么就要写上变量名
# print foo2(c=3,a=9)  #写上变量名的时候，参数传递就不要顺序
#
# ##函数的特殊参数传递
# def foo3(a,b,*c):    #*c 接受剩余的参数，返回元组类型
#     return a,b,c
#     for i in c:
#         pass
# foo3(1,2,3,4,5,6)
# #**接收赋值表达式的参数，返回字典类型
# def  foo4(a,b,**c):
#     return  a,b,c
# foo4(1,2,fff=77,kkk=8,UserAgent=999)
# #固定的参数  也有可选   赋值的参数
# def foo5(a,b,*c,**d):
#     return  a,b,c,d
# foo5(1,2,3,4,5,6,jj=9,ll=88)
# #函数调用
# def foo6(x,y):
#     x=x+y
#     return x
# def  foo7(a,b):
#     a=foo6(a,b)
#     return a+b
# print foo7(2,3)
#
# #函数自省
# print kill_process.__doc__

# 变量作用域
# i=10
# def fun1():
#     i=5     #局部变量
#     return i
# print i
# print fun1()
# print i
#
# i=10
# def fun1():
#     global i   #全局变量
#     i=5
#     return i
# print i
# print fun1()
# print i

# 异常1（try里面代码块任何一行代码出错，就到except里面去运行）
# try:
#     file=open("e:\\4561\\file.txt","r")
#     file.read()
#     file.close()
# except:
#     print "文件读取错误"

# 异常2(不管try代码块是否错误   finally都会被执行)
# try:
#     file = open("e:\\4561\\file.txt", "r")
#     file.read()
#     file.close()
# finally:
#     print "error"
# print "123"

# 判断浮点型
# sal=raw_input("input num:")
# try:
#     sal=float(sal)
#     if type(sal) ==float:
#         print sal,"ok"
# except:
#     print "error"

########################################练习###############################################
def reg():
    name = raw_input("请输入名字：")
    passwd = raw_input("请输入密码：")
    passwd2 = raw_input("请输入确认密码")
    reg_data = name + '\t' + passwd + '\n'
    ret = write_file("data.txt", reg_data)
    print ret


def write_file(filename, data):
    try:
        fileobj = open(filename, "a")
        fileobj.write(data)
        fileobj.close()
        return "数据写入文件成功"
    except:
        return "数据写入文件失败"


def read_file(filename):
    try:
        fileobj = open(filename, "r")
        data = fileobj.readlines()
        fileobj.close()
        return data
    except:
        data = []
        return data


def login(username, passwd):
    user_data = read_file('data.txt')
    count = 0
    for user in user_data:
        user = user.replace("\n", "")
        user_list = user.split("\t")
        if username == user_list[0] and passwd == user_list[1]:
            count += 1
    if count != 0:
        return "登录成功"
    else:
        return "登录失败"


while 1:
    choose = raw_input("1.注册  2.登录")
    if choose == '1':
        reg()
    elif choose == '2':
        username = raw_input("请输入用户名：")
        passwd = raw_input("请输入密码：")
        ret = login(username, passwd)
        print ret
    else:
        print "无该选项"


########################################作业#######################
# 在昨天的程序基础上修改
# 增加功能 5.修改（根据id 修改年龄、修改薪水）   6.删除（根据id删除该用户的所有信息）
# 增加的时候 添加一个字段id，在做增加用户的时候做判断，判断id不能重复；
# 整个代码功能都在文件中实现，用户增加 删除  改 查 都是在文件里
