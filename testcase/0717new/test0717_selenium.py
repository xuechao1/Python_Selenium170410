#coding=utf-8
#1.安装selenium   如果有网络的pip install selenium
#2.没有网络 离线安装  解压selenium.tar.gz   在cmd里面输入python setup.py install
#3.安装完成后检查是否安装成功 在cmd里面先敲python 再敲import selenium 如果没报错就安装成功了

#X:\Python27\Lib\site-packages  这个是所有的第三方 模块安装的目录
from selenium import  webdriver
from time import  sleep
br=webdriver.Chrome()
br.get("http://172.16.3.158/ecshop")
try:
    br.implicitly_wait(30)
    br.find_element_by_link_text("请登录").click()
    br.find_element_by_name("username").send_keys("duandongbo")
    br.find_element_by_name("password").send_keys("123456")
    br.find_element_by_name("submit").click()
    sleep(5)
    br.quit()
except Exception,e:
    print e
    br.quit()

#作业：一键自动注册10个用户