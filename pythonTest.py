# coding=utf-8
# print "HelloWorld";print "robot"
# raw_input("\n\nPress the enter key to exit")
# import sys
# x="robot"
# sys.stdout.write(x+'\n')
# x="aaaaa"
# y="bbbb"
# print x,
# print y,
# a=b=c=1
# print a,b,c
# a,b,c =1,0.356,"hello"
# print a,b,c,
# var1=1
# var2=10
# del var1
# print var2
# a=8
# b=0.35
# print complex(a,b)
# s="iloveyou"
# print s[:-1]
# print s[:-2]
# print s[-3:-1]
# print s[1:5]
# print s[0:4]
# 列表
# list=['hello',1,2,0.035,"robot"]
# list1=['my',1234]
# list2=list+list1
# print list+list1
# print list[0]
# print list2[5][1]
# print list2[5],list2[6]
# 元祖
# tuple=('hello',1,2,0.035,"robot")
# tuple1=("my",1234)
# tuple2=tuple+tuple1
# print tuple+tuple1
# print tuple2[5][1]
# tuple=("hello",1,2,0.035,"robot")
# list=["hello",1,2,0.035,"robot"]
# tuple[2]=1000     #元祖只能读取不能定义修改
# list[2]=1000      #列表可以定义也可以修改
# 字典
# dict={}
# dict['one']="this is one"
# dict[2]="this is two"
# tinydict={'name':"xuechao",'age':25,'sex':"man"}
# print dict['one']
# print tinydict
# print dict[2]
# print tinydict.values()
# print tinydict.keys()
# a = 10
# b = 20
# if (a and b):
#     print "1 - 变量 a 和 b 都为 true"
# else:
#     print "1 - 变量 a 和 b 有一个不为 true"
#
# if (a or b):
#     print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
# else:
#     print "2 - 变量 a 和 b 都不为 true"
# num=8
# if (num>=5 and num <=10) or (num>10 and num<15):
#     print "hello"
# else:
#     print "error"
# a=0
# b=1
# if ( a > 0 ) and ( b / a > 2 ):
#     print "yes"
# else :
#     print "no"
#
# def my_print(args):
#     print args
#
# def move(n, a, b, c):
#     my_print ((a, '-->', c)) if n==1 else (move(n-1,a,c,b) or move(1,a,b,c) or move(n-1,b,a,c))
#
# move (3, 'a', 'b', 'c')
# var = 1
# while var == 1:  # 该条件永远为true，循环将无限执行下去
#     num = raw_input("Enter a number  :")
#     print "You entered: ", num
#
# print "Good bye!"
# flag = 1
# while (flag): print 'Given flag is really true!'
# print "Good bye!"
# while 1:
#     print "Given flag is really true!"
# print "good bye"
# for letter in 'python':
#     print letter
#
# fruits=['banana','apple','orange']
# # for i in fruits:
# #     print i
# for index in range(len(fruits)):
#     print fruits[index]
# for num in range(10, 20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num / i
#             print '%d 等于 %d * %d' % (num, i, j)
#             break
#     else:
#         print num, '是一个质数'
# for num in range(10, 20):  # 迭代 10 到 20 之间的数字
#     for i in range(2, num):  # 根据因子迭代
#         if num % i == 0:  # 确定第一个因子
#             j = num / i  # 计算第二个因子
#             print '%d 等于 %d * %d' % (num, i, j)
#             break  # 跳出当前循环
#     else:  # 循环的 else 部分
#         print num, '是一个质数'
# sequence=[12,13,45,787,44,7897,45]
# for index,item in enumerate(sequence):
#     print index,item
# 输出2-100的质数
# list=[]
# for num in range(2,100):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         list.append(num)
# print list
# 打印空心等边三角形
# rows = int(raw_input('输入行数：'))
# for i in range(0, rows):
#     for k in range(0, 2 * rows - 1):
#         if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
#             print " * ",
#         elif i == rows - 1:
#             if k % 2 == 0:
#                 print " * ",
#             else:
#                 print "   ",
#         else:
#             print "   ",
#     print "\n"
# 打印1-9三角形阵列:
# for i in range(1,11):
#     for k in range(1,i):
#         print k,
#         k +=1
#     i +=1
#     print "\n"
# *字塔
# i=1
# #j=1
# while i<=9:
#    if i<=5:i
#       print ("*"*i)
#
#    elif i<=9 :
#       j=i-2*(i-5)
#       print("*"*j)
#    i+=1
# else :
#    print("")
# for i in 'python':
#     if i=='h':
#         break
#     print i
#
# for i in 'python':
#     if i =='h':
#         pass
#         print "这是pass块"
#     print "这个字母是：",i
# for i in range(1,5):    # 代表从1到5(不包含5)
#     print i
# for i in range(1, 5, 2): # 代表从1到5，间隔2(不包含5)
#     print i
# for i in range(5):  # 代表从0到5(不包含5)
#     print i
# print r'\n'
# print R'\n'
# hi="""hi
# there
# hello
# my friends"""
# print hi
# dit={'name':'xuechao','age':25,'sex':'man'}
# print "name is :"+dit['name']
# dit['age']=24
# dit["school"]="dragon"
# print dit
# del dit['name']; # 删除键是'Name'的条目
# dit.clear();     # 清空词典所有条目
# del dit ;        # 删除词典
# 获取当前日期
# import time
# localtime=time.localtime(time.time())
# print 'localtime: ',localtime
# # #格式化日期
# # localtime1=time.asctime(localtime)
# # print localtime1
# #格式化2016-03-20  11：45：36形式
# print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())##2017-07-16 10:24:49
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
# #将格式字符串转换为时间戳
# a=time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# #获取某年某月的日历
# import calendar
# cal=calendar.month(2017,7)
# print "下面是打印好的日历：\n",cal
# 定义函数
def printme(str):
    "打印传入的字符串到标准显示设备上"
    print str
    return


printme(str="my school")
# 调用函数
# printme("我要调用用户自定义函数")
# def ChangeInt(a):
#     a=10
# b=2
# ChangeInt(b)
# print b
# 可写函数说明
# def printinfo(name,age):
#     "请输入任何传入的字符"
#     print "Name：",name
#     print "Age：",age
#     return
# printinfo(name="tigerscott",age=50)
# Lamda函数 lambda 来创建匿名函数。
# sum=lambda arg1,arg2:arg1+arg2
# print "相加后的函数：",sum(10,20)
# print "相加后的值：",sum(35,75)
# total = 0;  # 这是一个全局变量
# 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2;  # total在这里是局部变量.
#     print "函数内是局部变量 : ", total
#     return total;
# # 调用sum函数
# sum(10, 20);
# print "函数外是全局变量 : ", total
# Money = 2000
# def AddMoney():
#     # 想改正代码就取消以下注释:
#     global Money
#     Money = Money + 1
# print Money
# AddMoney()
# print Money
import os

# os.mkdir("text1.txt")
# os.rename("text1.txt","text2.txt")
# os.remove("text2.txt")
# 创建目录test
# os.mkdir("test")
# os.chdir("/home/newdir")
# 给出当前路径
print os.getcwd()

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()

