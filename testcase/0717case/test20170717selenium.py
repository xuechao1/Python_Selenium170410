#coding=utf-8
from selenium import webdriver
from time import *
br=webdriver.Firefox()
br.get("http://172.16.3.158/ecshop")
br.implicitly_wait(30)
br.find_element_by_link_text("请登录").click()
br.find_element_by_name("username").send_keys("duandongbo")
br.find_element_by_name("password").send_keys("123456")
br.find_element_by_name("submit").click()
sleep(3)
br.quit()