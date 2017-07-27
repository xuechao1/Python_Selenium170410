#coding=utf-8
import os, time, stat

def listTxtInPath(path):
    """获取目录下所有的文件的创建日期、大小、文件名；
    入参传入目录路径，后面需跟上双斜线；例如d:\\
    返回list"""
    resultlist = []
    if os.path.isdir(path) and os.path.exists(path):
        listFile = os.listdir(path)
        for fileName in  listFile:
            if os.path.isfile(path+"\\"+fileName):
                ctime=os.stat(path+"\\"+fileName)[stat.ST_CTIME]
                fsize=os.stat(path+"\\"+fileName)[stat.ST_SIZE]
                resultlist.append ("%s\t%8dkb\t%s"%(time.strftime("%Y-%m-%d",time.localtime(ctime)),fsize/1024,fileName.decode("gbk")))
        return resultlist
    else:
        return resultlist

def kill_process(name):
    """windows专杀进程函数，入参进程名字即可"""
    os.system("taskkill /f /im "+name+"* >nul 2>nul")

def cacl_year(year):
    """计算闰年的方法 入参必须是整型的数据；闰年返回0  平年返回1 其他错误返回2"""
    try:
        year=int(year)
        if year%4==0 and year%100!=0 or year%400==0:
            return 0
        else:
            return 1
    except:
        return 2

def foo1(x,y):
    return x**y

def foo2():
    pass

def foo3():
    pass

def foo4():
    pass