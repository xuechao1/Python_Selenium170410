#coding=utf-8
#######################################函数###############################
import os
def kill_process(name):
    """函数的注释：此函数windows专杀进程函数，传入进程名即可"""
    os.system('taskkill /f /im '+name+'* >nul 2>nul')

kill_process('firefox')
kill_process('chrome')

def calc_roundTi(a,b,c):
    """计算长方体的体积"""
    a=int(a)
    b=int(b)
    c=int(c)
    if a!=0 and b!=0 and c!=0:
        return a*b*c
    else:
        "您输入的有误请重新输入"
def foo1(a=3,b=4,c=5):
    return a*b*c
print foo1()
print foo1(6,6,7)
print foo1(a=9,c=6)
print foo1(b=6)

##求闰年计算公式
def calc_year(year):
    year=int(year)
    if year%4==0 and year%4!=0 or year%400==0:
        return 0
    else:
        return 1
#函数的入参
def foo2(a=1,b=8,c=5):
    return a+b+c

print foo2(1,2,3)    #实参
#函数定义的时候，如果形参有默认值：在调用函数的时候
#首先按传递的参数进行运算，如果没有传递参数，就取默认值运算
print foo2(1,2)     #没有默认值的时候，就取默认值
print foo2(b=8,c=3)     #如果想传递指定的参数，那么就要写上指定的变量名
print foo2(c=3,a=9)     #写上变量名的时候，参数传递就不要顺序

#函数的特殊参数传递
def foo3(a,b,*c):      #*c接受剩余的参数，返回元组类型
    return a,b,c
    for i in c:
        pass
print foo3(1,2,3,4,5,6)
foo3(1,2,3,4,5,6)
#**接收赋值表达式的参数，返回字典类型
def foo4(a,b,**c):
    return a,b,c
print foo4(1,2,fff=77,kkk=8,userAgent=999)
foo4(1,2,fff=77,kkk=8,userAgent=999)
# #固定的参数  也有可选  赋值的参数
def foo5(a,b,*c,**d):
    return a,b,c,d
print foo5(1,2,3,4,5,6,jj=9,ll=88)
foo5(1,2,3,4,5,6,jj=9,ll=88)
# #函数调用
def foo6(x,y):
    x=x+y
    return x
def foo7(a,b):
    a=foo6(a,b)
    return a+b
print foo7(3,6)
#函数自省
print kill_process.__doc__

#变量作用域
i=10
def fun1(i):
    i=5     #局部变量
    return i
print i
#
def fun2():
    global i  #全局变量
    i=5
    return i
print i
print fun2()
print i
#
# #异常1（try里面代码任何一行代码出错，就到except里面去执行）
# try:
#     file=open("e:\\4561\\file.txt","r")
#     file.read()
#     file.close()
# except:
#     print "文件读取错误"
#
# #异常2（不管try代码块是否错误  finally都会被执行）
# try:
#     file=open("e:\\4561\\file.txt","r")
#     file.read()
#     file.close()
# finally:
#     print "error"
# print "123"
#
# #判断浮点型
# sal=raw_input("input num:")
# try:
#     sal=float(sal)
#     if type(sal)==float:
#         print "正确"
#         break
# except:
#     print "输入异常，请重新输入"
#
