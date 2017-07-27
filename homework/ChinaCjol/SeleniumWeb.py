#coding=utf-8
from selenium import webdriver
from time import sleep
import os

driver=webdriver.Firefox()
# driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.cjol.com")
driver.implicitly_wait(15)
driver.find_element_by_link_text("个人登录").click()
sleep(1)
driver.find_element_by_id("txtUserName").send_keys("xue10123456@163.com")
driver.find_element_by_id("tbxPasswordTip").click()
driver.find_element_by_id("txtPassword").send_keys("123456789")
driver.find_element_by_id("btnLogin_input").click()
sleep(3)
driver.quit()