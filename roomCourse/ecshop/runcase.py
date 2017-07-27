#coding=utf-8
from ecshop.public import HTMLTestRunner
import os,time,unittest
from ecshop.public.Sendmail import *

#定义自动化用例目录
testcase_dir = os.path.join(os.getcwd(),'testcase')
print testcase_dir
#定义自动化用例测试报告目录
test_report = os.path.join(os.getcwd(),'Report')
print test_report
#定义用例集合
discover = unittest.defaultTestLoader.discover(testcase_dir,pattern='test*.py')#discover搜索test开头的py文件
print discover

# now  当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S")  #定义格式化时间
#
filename = test_report+'/result_'+now+'.html'  #定义报告的名字 为了不要重复
fp = open(filename,'wb')  #写二进制文件
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u"ITLEO自动化测试报告",
                                       description=u"用例执行情况：")
runner.run(discover)
fp.close()
file_new=new_report(test_report)
send_mail(file_new,"623858143@qq.com")
