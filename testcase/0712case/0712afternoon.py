#coding=utf-8
#if 条件循环
#单条件
# name=raw_input("请输入你的名字")
# if name=="王思聪":
#     print "国民老公"
#双条件
# if name=="韩寒":
#     print "国民岳父"
# else:
#     print "一个屌丝而已"
#多条件
# score =raw_input("请输入你的成绩")
# score = int(score)
# # print type(score)
# if score<60:
#     print "不及格"
# elif 60<=score<70:
#     print "及格"
# elif 70<=score<90:
#     print "良好"
# elif 90<=score<=99:
#     print "优秀"
# else:
#     print "满分"
# while 1:
#     year=raw_input("请输入你的年份：")
#     year=int(year)
#     if year%4==0 and year%100!=0 or year%400==0:
#         print year,"闰年"
#     else:
#         print year,"平年"
#
# while 1:
# a=raw_input("请输入数字a: ")
# a=int(a)
# b=raw_input("请输入数字b: ")
# b=int(b)
# c=raw_input("请输入数字c: ")
# c=int(c)
# if a!=0 and b!=0 and c!=0 and a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print "等边三角形"
#     elif a**2+b**2==c**2:
#         print "直角三角形"
#     elif a==b and b!=c:
#         print "等腰三角形"
#     elif a==b and a**2+b**2==c**2:
#         print "等腰直角三角形"
#     else:
#         print "您输入的数字有误,无法构建三角形"
# else:
#     print "你输入的数字有误，无法构建三角形"

#while循环
# i=raw_input("请输入i的值")
# i=int(i)
# while i==10:
#     if i<6:
#         print i
#         if i==5:
#             break

# #for循环
# for i in range(10):
#     print i
# #for循环  区间
# for i in range(1,10):
#     print i
#
# #for步长
# for i in range(4):
#     for j in range(6):
#         for k in range(3):
#             print i,j,k

#打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i):
#         print i,"*",j,"=",i*j,'\t',
#     print "\t"
#
for i in range(1,10):
    for j in range(1,i+1):
        print i,"*",j,"=",i*j,'\t',
    print ''
#
# for i in range(1,10):
#     for j in range(i,10):
#         print i,"*",j,"=",i*j,'\t',
#     print ''

#水仙花数    153=1**3+5**3+3**3
#100-999之间有多少符合这个条件的
# a=int(raw_input("请输入a"))
# for i in range(100,1000):
#     if (i//100)**3+(i//10%10)**3+(i%10)**3==i:
#         print i

#计算1  2  3  4能组成多少个不重复的三位数，并且把三位数打印出来
# for a in range(1,5):
#     for b in  range(1,5):
#         for c in range(1,5):
#             if a!=b and b!=c and c!=a:   #a!=b!=c!=a
#                 print a*100+b*10+c

print len("s")

