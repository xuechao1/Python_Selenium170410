#coding=gbk
#�쳣����
# try:
#     open("asdfasd","r").read()
# except Exception,e:
#     print "error",repr(e),e   #repr��ӡʲô���͵�error������ʾ������Ϣ    e��ʾ������Ϣ
#
###################################################ģ��########################################################
# import time   #ϵͳ�Դ���ģ��
# import selenium #��������ģ��
# # time.sleep(2)
# # print time.time()    #1970-1-1��Ŀǰ��������ʱ���
# # print type(time.localtime())
# #����ģ��ķ�ʽһ
# import time,random,selenium  #������ģ�� ���Ÿ���
# print random.randint(1,100)  #�������100�������ģ��
# print random.randrange(100)  #������100
# num=random.randint(1,100)
# while 1:
#     guess=input("���������֣�")
#     if guess<num:
#         print "��µ��е�С"
#     elif  guess>num:
#         print "��µ��е��"
#     else:
#         print "��¶���"
#���뷽ʽ��������ʹ�õķ�ʽҲ�᲻һ������Դռ����һЩ��
from time import sleep
#sleep(2)   #��time.sleep(2)ʵ��Ч����һ����
# import time
# print dir(time)  #�鿴ģ������ķ���
# #print help(time) #�鿴ģ��Ľ��� ʹ�÷��� ��cmd����Ҳ������
# import math
# print math.sqrt(9)
# import os
# os.system("ping www.baidu.com")
# print os.getcwd()  #current ��ǰ��·��
# print os.name

#####################################python��ϵͳ�Ĳ���##########################
#����Ŀ¼
import os
#�ж�Ŀ¼�Ƿ����(os.path.exists �����ж�Ŀ¼���ļ�) ��ȥ����1.if
# if not os.path.exists("e:\\123123"):
#     os.mkdir("e:\\123123")
# #2.try
# try:
#     os.mkdir("e:\\333")
# except Exception,e:
#     print e
# # #ɾ����Ŀ¼
# if os.path.exists("e:\\123123"):
#     os.rmdir("e:\\333")
# #ɾ���ǿ�Ŀ¼
# import shutil
# if os.path.exists("e:\\333"):
#     shutil.rmtree("e:\\333")
# #cmdɾ���ǿ�Ŀ¼����
# os.system("rd /s /q e:\\333")
# #������Ŀ¼
# os.mkdir("e:\\123")
# os.rename("e:\\123","e:\\456")
# #cmd������������
# os.system("ren   e:\\456   e:\\789")

#��������Ŀ¼
# os.makedirs("e:\\11\\22\\33")
# #cmdģʽ��
# os.system("md e:\\a\\b\\c")
#ɾ�ļ�
# if os.path.exists("e:\\file.txt"):
#     #os.remove("e:\\file.txt")
#     os.unlink("e:\\file.txt")

#decode����  encode����
# c="����"
# print repr(c)   #�����utf-8��'\xe6\xb1\x89\xe5\xad\x97'�� �����gbk�Ļ���'\xba\xba\xd7\xd6'��
# print c.decode("gbk")
#
# #�г�ָ��Ŀ¼�µ������ļ�
# file= os.listdir("d:\\")
# print file
# for i in file:
#     filename=i.decode("gbk")
#     if filename[-4:]==".exe":
#         print filename
# #�ж��Ƿ�Ϊ�ļ� ����Ŀ¼
# print os.path.isdir("e:\\123123")
# print os.path.isfile("e:\\123123")
#
# #��ȡ�ļ��Ĵ���ʱ�䣻��С�ȵ�
# import stat
# fp = open("d:\\resume0504.7z")
# st = os.fstat(fp.fileno())
# print  st[stat.ST_CTIME],st[stat.ST_SIZE]
#
# import datetime,time
# print datetime.datetime.now()
# print datetime.datetime.strftime(datetime.datetime.now(), '%Y/%m/%d %H:%M:%S')
# #ʱ���ת���ɸ�ʽ��ʱ��
# print time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(1493880515))

#����Զ����ģ���в㼶��ϵ����ô�����ʱ����from
#���Զ���ģ��Ŀ¼���棬��Ҫ����һ��__init__.py�ļ��������ñ༭���½�һ��package��
#
# from project2017_02.Public.public_base import *
# filename= listTxtInPath("d:\\")
# for i in filename:
#     print i
