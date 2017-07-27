#coding=utf-8
from selenium import  webdriver  #从selenium包导入webdriver模块
import os,time
#os.system("taskkill /f /im chrome* >nul 2>nul")
os.system("taskkill /f /im geck* >nul 2>nul")
os.system("taskkill /f /im firefox* >nul 2>nul")


br=webdriver.Firefox()  #确定测试要使用的浏览器 把浏览器对象赋值给一个变量
br.implicitly_wait(20) #隐性等待 也叫智能等待，最长等待20秒
br.get("http://172.16.3.158/ecshop")  #浏览器打开要测试的网址
br.maximize_window()   #最大化浏览器窗口

#login
br.find_element_by_link_text("请登录").click()  #link_text 点击文本链接  在html里面一般是a标签
br.find_element_by_name("username").send_keys("zhaosi6") #输入框里面输入用户名
br.find_element_by_name("password").send_keys("123123")     #输密码
br.find_element_by_name("submit").click()  #点击登录按钮
time.sleep(1)
br.find_element_by_link_text("用户中心").click()
time.sleep(1)
br.find_element_by_link_text("我的推荐").click()
time.sleep(1)
#二次查找元素
# ele=br.find_element_by_name("province")
# ele.find_element_by_css_selector('option[value="3"]').click()

ele=br.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/table[1]/tbody/tr[contains(.,'4')]")
#contains包含的意思  .当前的元素里面  '4' 需要查找的文本
print ele
print ele.find_element_by_xpath('td[3]').text #从上面的行里面 再去取第三列的数据

ele=br.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/table[1]/tbody/tr[contains(.,'4')]")