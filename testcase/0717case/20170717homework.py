#coding=utf-8
from selenium import webdriver
from time import *
from random import *
br= webdriver.Firefox()
br.get("http://172.16.3.158/ecshop")
br.implicitly_wait(30)
for i in range(1,11):
    num=str(i)+random.randint(1,1000)
    br.find_element_by_link_text("免费注册").click()
    br.find_element_by_id("username").send_keys("xuechao"+num)
    br.find_element_by_id("email").send_keys(num+"@qq.com")
    br.find_element_by_id("password1").send_keys("123123")
    #确认密码
    br.find_element_by_id("conform_password").send_keys("123123")
    #手机
    # br.find_element_by_name("extend_field5").click()
    br.find_element_by_name("extend_field5").send_keys("123123")
    #注册
    br.find_element_by_name("Submit").click()
    sleep(2)
    br.find_element_by_link_text("退出").click()
br.quit()



