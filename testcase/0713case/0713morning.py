#coding=utf-8
#字符串  引号之间
#  \续行符
# ss="as" \
#    "ddf"
#
# #切片运算
str="hello python.txt"
# print str[0]       #从前往后计算  下标，索引、index从0开始计数
# print str[6:9]      #取范围 6,7,8
# print str[6:]       #取下标之后所有字符，包含该下标
# print str[:6]       #取下标之前的所有字符，但不包含该下标
# sss="￥1235.78"
# print sss[3:]        #￥是中文字符，占据三个，
# print str[-1]       #从后往前  下标从-1开始
# print str[-6:-3]    #小数放前面，大数放后面
# print str[-3:]      #范围 从右开始取值，从0开始取值到-2   例如0，-1，-2
# print str[:-3]      #取范围  从左开始的所有值，一直到-3位
print str[::-1]     #取反序

#####提示输入一串字符串，然后反序输出#######
# str=raw_input("请输入一个字符串\n")
# result=""
# for i in range(len(str)):
#     print i
#     result+=str[-(i+1)]  #此处减号代表 负号，表示负数的意思，相反方向的意思
#     print result
# print ("倒序为： "+result)
# 重点
# aaa=raw_input("请输入一个字符串：：")
# aab=""
# for i in range(1,len(aaa)+1):
#     print i
#     aab=aab+aaa[-i]
# print aab
#遍历
# strl="hello python.txt"
# for i in strl:
# #     print i,
# # #计数
# strl="hello python.txt"
# print strl.count("t")
# #转换大小写
# print strl.upper()
# print strl.lower()
# #查找 判断
# if 'ppp' in strl:
#     print "ok"
# else:
#     print "error"
# #查找
# print strl.find("o")  #如果找到了就返回它的下标，如果没有找到就返回-1
# if strl.find("u")!=-1:
#     print "ok"
# else:
#     print "error"
# #替换
# print strl.replace("o","xxxxxx")
# #切割
# str2="a|b|c|d,f,g,h,j"
# print str2.split("|")
#去空格
# str3="      hello  python    "
# print str3.strip()   #去掉两边的空格
# print str3.lstrip()  #去掉左边的空格
# print str3.rstrip()  #去掉右边空格
#判断全部为数字
# str4="243432423d43"
# print str4.isdigit()
# #复制
# str5=str4*30   #赋值是一种行为  一种动作
# print str5
###########################列表list##################
#定义 中括号【】
# list1=[]    #空的列表
# #可以存储任意长度  任意类型的数据
# list1.append(6666)   #追加，一次只能增加一个对象
# print list1
# # #快速生成列表
# for i in range(1,50):
#     list1.append(i)
# print list1
# #插入
# list1.insert(-1,"jjjj")     #第一个参数是下标，第二个参数是值
# print list1
# # #切片运算
# # #参考字符串一模一样
# # print list1[0]
# #根据下标删除
# del list1[2]
# print list1
# #根据值删除
# list1.remove(6666)
# print list1
#修改
# list2=[99,44.23,"Abc","jjjj","python"]
# list2[2]="python1"
# #查询判断
# if "python" in list2:
#     print "ok"
# #遍历
# for i in list2:
#     print i,type(i)
# #排序
# list2.sort()
# print list2
# #计算ascII码十进制的值
# print ord("A")
# print ord("a")
# #倒序排
# list2.sort(reverse=True)
# print list2
# 嵌套  复制 相加
###########################作业###################################
str1="'@bjb|北京北|VAP|beijingbei|bjb|" \
    "0@bjd|北京东|BOP|beijingdong|bjd|" \
    "1@bji|北京|BJP|beijing|bj|" \
    "2@bjn|北京南|VNP|beijingnan|bjn|" \
    "3@bjx|北京西|BXP|beijingxi|bjx|" \
    "4@gzn|广州南|IZQ|guangzhounan|gzn|" \
    "5@cqb|重庆北|CUW|chongqingbei|cqb|" \
    "6@cqi|重庆|CQW|chongqing|cq|" \
    "7@cqn|重庆南|CRW|chongqingnan|cqn|" \
    "8@gzd|广州东|GGQ|guangzhoudong|gzd|9"
# while 1:
#     station_name=raw_input("\n请输入站台名称\n")
#     print "station_name",station_name
#     list=str1.split("@")
#     print "list列表：\n",list
#     for i in list:
#         print "i1:",i
#         if i.find("|")!=-1:
#             print "i2:",i
#             if i.split("|")[1]==station_name:
#                 print "i3:",i
#                 print i.split("|")[2]
#                 print "i4:",i

station_name=raw_input("\n请输入站台名称\n")
list=str1.split("|")
print list
print list.index(station_name)+1
print list[list.index(station_name)+1]