#coding=utf-8
############################元组tuple###########################
#定义 小括号，元素之间逗号分开
# tuple1=(1,2,3,4,)
#存储任意类型  任意长度
#元组不能增加  不能修改  不能删除
#遍历的速度比list要快很多
#存储数据比list安全
#
# #切片运算
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
# tuple2[3][1]=44       #元组里面嵌套的列表可以操作
# print tuple2
#
# del tuple2[3][0]
# del tuple2[3][0]
# del tuple2[3][0]
# print tuple2
############################字典dict####################
#定义{} 大括号，字典映射关系一一对应
dict1={}
#key:value  一对一组  每一组之间逗号隔开
dict1={"name":"zhang","age":23,"sex":"男"}
dict2={"name":"xuechao","borthyear":1992,"favorite":"game"}
# #key键 只能是数字或者是字符串 ；value值 可以是任意数据
#字典是无序，没有顺序
print dict1
print "dict2:",dict2
#查找
print dict1["sex"]
# #增加（如果key存在，那就是修改功能，如果key不存在，那就是增加功能）
dict1["name"]="shenzhen"
print dict1
# #删除
# # del dict1["name"]
# # print dict1
# #字典遍历所有的key
for i in dict1:
    print i
    if i=="name":
        print dict1["name"]
#遍历key
for i in dict1.keys():
    print i
# #遍历值
for j in dict1.values():
    print j
#遍历项目
for i in dict1.items():
    print "\n"      #打印一共有几行
for i,j in dict1.items():
    print i,":",j
# #变量赋值  交换 简写方式
x,y,z=4,5,6
y,z=z,y
print y,z
#格式化输出  %d代表整型  %s字符串  %f浮点型
for i in range(1,10):
    for j in range(1,i+1):
        print "%d*%d=%d"%(i,j,i*j),
    print ''
# for i in range(1,100):
#     print "%s%d次运行脚本"%("第",i)
#     print "第"+str(i)+"次运行脚本"
print "%s%d次运行脚本"%("第",23)
print "第"+str(23)+"次运行脚本"



