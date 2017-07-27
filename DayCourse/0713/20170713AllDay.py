# coding=utf-8
#########################str  list   tuple  dict#########################################
# 字符串  引号之间
#  \续行符
# ss="asd"
# #切片运算
# str1="hello python.txt"
# print  str1[0]    #从前往后计算   下标，索引、index 从0开始计数
# print  str1[6:9]  #取范围
# print  str1[6:]   #取下标之后所有的字符，包含该下标
# print  str1[:6]   #取下标之前的所有字符，但是不包含该下标
# ss="￥123.80"
# print  ss[3:]
# print  str1[-1]    #从后往前   下标从-1开始
# print  str1[-6:-3] #小数放前面 大数放后面
# print  str1[-3:]
# print  str1[:-3]
# print  str1[::-1]  #反序
###提示输入一串字符串，然后反序输出######
# str=raw_input("请输入一串字符：")
# result=""
# for i in range(len(str)):
#     result+=str[-(i+1)]
# print("倒序为:"+result)
#
# strmm=raw_input("请输入一串字符：：")
# strs=""
# for i in range(1,len(strmm)+1):
#     #print strmm[-i],
#     strs=strs+strmm[-i]
# print strs
str1 = "hello python.txt"
# #遍历
# for i in str1:
#     print i
#     if i=='t':
#         break
# #计数
# print str1.count("t")
# #转换大小写
# print str1.upper()
# print str1.lower()
# #查找 判断
# if 'ppp' in str1:
#     print "ok"
# else:
#     print "error"
# #查找
# print str1.find("uu")  #如果找到了就返回它的下标  如果没找到就返回-1
# if str1.find("u")!=-1:
#     print "ok"
# else:
#     print "error"
# #替换
# print str1.replace("o","kkkkk")
# #切割
# str3="a|b|c|d,f,g,h"
# print str3.split("|")      #按照一定规律去切开，然后返回list

# 去空格
# str3="1234567 "
# print str3.strip()   #去掉两边的空格
# print str3.lstrip()  #去掉左边的空格
# print str3.rstrip()  #去右边的空格
# #判断全部为数字
# print str3.isdigit()
# #复制
# str4=str3*3  #赋值是一种行为 一种动作
# print str4
##################################################列表list#########################################
# 定义 中括号[],以逗号区分每个元素
list1 = []  # 空的列表
# 可以存储任意长度  任意类型的数据
# list1=[99,2.3,4444.999,22,2222,33,4444,"Abc","abc"]
# #支持增、删、改、查的操作
# #增加
# list1.append(7777)    #追加 ，一次只能增加一个对象
# print list1
# #快速生成列表
# # for i in range(50):
# #     list1.append(i)
# # print list1
# #插入
# list1.insert(0,"jjjjj")  #第一个参数是下标，第二个是值
# print list1
# #切片运算
# #参考字符串一模一样
# print list1[:3]
# #根据下标删除
# del  list1[2]
# print list1
# #根据值删除
# list1.remove(99)
# print list1
# #修改
# list1[2]="python"
# print list1
# #查询判断
# if  "python"  in  list1:
#     print "ok"
# #遍历
# for i in list1:
#     print i,type(i)
# #排序
# list1.sort()
# print list1
# print ord("A")  #计算ascii码十进制的值
# #倒序排
# list1.sort(reverse=True)
# print list1

# 嵌套
# list3=[1,2,3,4,5]
# list3.append([11,22,33,44])
# print list3[5][2]
# #复制
# print list3*20   #把自己复制20次，生成一个新的列表数据
# #相加
# list4=["a","b","c"]
# list5=list3+list4
# #计算某个值的下标
# print list4.index("b")
###############################################课堂练习##############################################
str1 = "@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1@" \
       "bji|北京|BJP|beijing|bj|2@bjn|北京南|VNP|beijingnan|bjn|3@bjx|北京西|" \
       "BXP|beijingxi|bjx|4@gzn|广州南|IZQ|guangzhounan|gzn|5@cqb|重庆北|CUW|" \
       "chongqingbei|cqb|6@cqi|重庆|CQW|chongqing|cq|7@cqn|重庆南|CRW|chongqingnan" \
       "|cqn|8@gzd|广州东|GGQ|guangzhoudong|gzd|9"
# while 1:
#     station_name=raw_input("input：")
#     list =str.split("@")
#     for i in list:
#         if i.find("|") !=-1:
#             if i.split("|")[1]==station_name:
#                 print i.split("|")[2]

# station_name=raw_input("input：")
# list=str.split("|")
# print list[list.index(station_name)+1]

#########################################元组tuple##################################################
# 定义 小括号,元素之间逗号分开
tuple1 = (1, 2, 3, 4,)
# 存储任意类型  任意长度
# 元组不能增加  不能修改  不能删除
# 遍历的速度比list要快很多
# 存储数据比list安全
# 切片运算
# print tuple1[2]
# #其他的方法参考字符串的运算就行
# #遍历
# for i in tuple1:
#     print i
# #嵌套
# tuple2=(1,2,3,(4,5,6))
# print tuple2[3][1]
#
# tuple2=(1,2,3,[4,5,6],7,8)
# tuple2[3][1]=44  #元组里面嵌套的列表可以操作
# print tuple2
#
# del tuple2[3]
# print tuple2
#######################################字典 dict################################################
# 定义{} 大括号 ，字典映射关系 一一对应
dict1 = {}
# key:value   一对一组 每一组之间逗号隔开
dict1 = {"name": "zhang", "age": 23, "sex": "男"}
# key键 只能是数字或者是字符串  ；value值 可以是任意数据
# 字典是无序 ，没有顺序
print dict1
# 查找
print dict1["sex"]
# 增加 (如果key存在那就是修改功能，如果key不存在那就是增加功能)
# dict1["address"]="shenzhen"
# print dict1
# #删除
# # del dict1["name"]
# # print dict1
# #字典遍历所有的key
# for i in dict1:
#     print i
#     if i=="name":
#         print dict1["name"]
# #遍历key
# for i in dict1.keys():
#     print i
# #遍历值
# for i in dict1.values():
#     print i
# #遍历项目
# for i in dict1.items():
#     print i,type(i)
#     print i[0],i[1]
# #遍历项目(简写)
# print "\n"
# for i,j in dict1.items():
#     print i,j
# #变量赋值 交换 简写方式
# x,y,z=4,5,6
# y,z=z,y
# print y,z
# #格式化输出  %d代表整型  %s字符串 %f浮点型
# for i in range(1,10):
#     for j in range(1,i+1):
#         print "%d*%d=%d"%(i,j,i*j),
#     print ""
# print "%s次运行脚本%f"%("第",23.9)
# print "第"+str(23)+"次运行脚本"

############################################作业################################################
"""
1.存储员工信息
2.查询员工信息(查询三种方式name，age，sal)
3.所有员工信息（格式化输出，对齐）
4.退出程序
"""
