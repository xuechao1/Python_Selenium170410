# coding=utf-8
###########################读写################################
# 写（当前目录，脚本在哪里就写在哪里）
# .当前目录   ..上层目录     ../../../
fileobj = open("file.txtb", "w")
# fileobj=open("../fiel.txt","w")   #相对路径
print fileobj, type(fileobj)  # 第一个参数文件名，写的方式打开
fileobj.write("qwe2343432")
str = "sfkjksljflk93209sdf速度风口浪尖"
fileobj.write(str)  # 把字符写入文件里面
fileobj.close()  # 文件操作完成后记得关闭

# 指定绝对路径  （路径要加双斜线）
fileobj = open("C:\\Users\\Administrator\\Desktop\\file.txt", "w")  # 第一个参数文件名，写的方式打开
print fileobj, type(fileobj)
strl = "sflsjfl984832084932\n"
str1 = "sfslkjl329\t9999999999\n"
str2 = "sfslkjl329\n9999999999\n"
str3 = "sfsl\njl329\t9999999999\n"
str4 = "sfslkjl\n9999999999\n"
fileobj.write(strl)  # 把字符写入文件里面
fileobj.write(str1)
fileobj.write(str2)
fileobj.write(str3)
fileobj.write(str4)
fileobj.close()  # 文件操作完成后记得关闭

# 绝对路径前面加 r 用来识别绝对路径的
fileobj = open(r"C:\\Users\\Administrator\\Desktop\\file1.txt", "w")  # 第一个参数文件名，写的方式打开
print fileobj, type(fileobj)
strll = "ksdfjsdkjf的看法绝对是24342\n"
str11 = "ksdfjsdkjf的看\n法绝对是24342"
str12 = "ksdfjsdkjf的看法绝对是2434\n2"
str13 = "ksdfjsdkjf的看法绝对是24342\n"
str14 = "ksdfjsdkjf\n的看法绝对是24342"
str15 = "ksdfjsdkjf的看法绝对是24342\n"
fileobj.write(strll)  # 把字符写入文件里面
fileobj.write(str11)
fileobj.write(str12)
fileobj.write(str13)
fileobj.write(str14)
fileobj.write(str15)
fileobj.close()  # 文件操作完成后记得关闭

#写html
fileobj=open(r"e:\\file3.html","w")
print fileobj,type(fileobj)
strlll="""
<html>
<body>
<input type="text" value="123" id="user">
<br><br><br>
<button id="loginBtn">login</button>
</body>
</html>
"""
fileobj.write(strlll)
fileobj.close()

#写文件
# import os
# path1=u"e:\\测试34\\"
# if not os.path.exists(path1):
#     os.mkdir(path1)
# fileobj=open(path1+"file2.txt","w")
# str21="大家斯洛伐克数据库王9490284dkjflsj"
# fileobj.write(str21)
# fileobj.close()

#写中文目录（处理中文前面加 u unicode编码格式）
import os
path1=u"e:\\测试11\\"
if not os.path.exists(path1):
    os.mkdir(path1)
fileobj=open(path1+"file11.txt","w")
print fileobj,type(fileobj)
stri="skjflsd来看待世界疯狂34324u089\n"
fileobj.write(stri)
fileobj.close()
# #追加  a
fileobj=open(u"e:\\测试11\\file12.txt","a")
print fileobj,type(fileobj)
strGe="隔壁\t老王\n"
fileobj.write(strGe+'\n')
fileobj.close()
#读文件
fileobj=open(r"C:\\Users\\Administrator\\Desktop\\file1.txt","r")
print fileobj
print fileobj.readlines()
for i in fileobj.readlines():
    print i
# #读指定行
import linecache
print linecache.getline(u"e:\\测试\\file12.txt",1)
#win7英文版的汉字乱码问题
# fileobj=open(r"C:\\Users\\Administrator\\Desktop\\file1.txt","r")
# print fileobj
# print fileobj.read().decode("utf-8").encode("gbk")
#读二进制

#读写二进制文件
#http://172.16.3.158/ecshop/data/afficheimg/1462958213922967180.jpg
# import urllib2
# data=urllib2.urlopen("http://172.16.3.158/ecshop/data/afficheimg/1462958213922967180.jpg").read()
# file=open("123.jpg","wb")
# file.write(data)
# file.close()

file=open("C:\\Windows\\notepad.exe","rb")
print file.read()