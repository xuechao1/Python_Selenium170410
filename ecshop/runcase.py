#coding=utf-8
from ecshop.public import HTMLTestRunner
from ecshop.public.Sendmail import *
import os,unittest,time


testcase_dir = os.path.join(os.getcwd(),'testcase') #定义自动化用例的目录(join把后面的字符加入到前面的变量)
print testcase_dir
test_report = os.path.join(os.getcwd(), 'Report')   #定义自动化测试报告的目录
print test_report
discover = unittest.defaultTestLoader.discover(testcase_dir,pattern='test*.py') #定义用例集合
print discover

now = time.strftime("%Y-%m-%d-%H:%M:%S")  #定时格式化时间
filename = test_report+'/result_'+now+'.html' #定义报告的名字  为了不要重复
fp = open(filename,'wb')    #写二进制文件
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u"ITLEO自动化测试报告",
                                       description=u'用例执行情况：')
runner.run(discover)
fp.close()
file_new=new_report(test_report)
send_mail(file_new,"xue10123456@itleo.cn")