#coding=utf-8
from cjol.public.basic import *
import os,time

def login(url,username,passwd):
    try:
        driver=open_browser('gc')
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(20)
        click_link_text(driver,"个人登录")
        time.sleep(0.5)
        input_text(driver,"txtUserName",username)
        click_element(driver,'[id="tbxPasswordTip"]')
        input_text(driver,"txtPassword",passwd)
        time.sleep(1)
        click_element(driver,'[id="btnLogin_input"]')
        time.sleep(2)
        return True
    except:
        return False

def page_search(driver,text,element,name):
    click_button(driver,"a_MyResumeCenterAutoSearchResult")
    time.sleep(2)
    try:
        click_id("a_setsearchjobs").click()
        input_text(driver, '[id="txtKeyWord"]', u"自动化测试")
        click_id(driver, "txtRegion")
        time.sleep(0.5)
        click_link_text(driver, "深圳")
        time.sleep(0.5)
        click_xpath(driver, '//*[@id="winLocation_dropdivrdiv_2008"]/div/div[1]/div/p/span')
        time.sleep(0.5)
        click_id(driver, "winLocation_dropdivselected_ok")
        time.sleep(0.5)
        click_button(driver, "btnSaveAndSearch")
    except:
        click_button(driver, "btnSaveAndSearch")
    time.sleep(2)
    click_button(driver, "btnSearch")
    str1 = [u"深圳市华辰软通信息咨询有限公司", u"深圳市鸿程信息技术有限公司", u"深圳市丰泽高科信息技术有限公司", u"深圳市华腾科创信息技术有限公司", u"深圳市文思联合网络技术有限公司",u"深圳凌岳软件有限公司", u"深圳无觅科技有限公司"]
    for i in range(1, 41):
        name = driver.find_element_by_xpath('//*[@id="searchlist"]/ul[' + str(i) + ']/li[3]/a').text
        # print name,type(name)
        if name not in str1:
            driver.find_element_by_xpath('//*[@id="searchlist"]/ul[' + str(i) + ']/li[1]/input').click()
        else:
            continue
    time.sleep(2)

def roll_down(self):
    # 将页面滚动条滑倒页面底部
    js = "var q=document.body.scrollTop=100000"
    driver=self.driver
    driver.execute_script(js)
    time.sleep(2)

def submit_element(self,element):
    driver=self.driver
    driver.find_element_by_css_selector(element).click()

def finish(self,num):
    driver=self.driver
    driver.switch_to.alert.accept()
    time.sleep(num)
    driver.switch_to.alert.accept()
    time.sleep(num)

def kill_process(name):
    os.system("taskkill /f /im "+name+"* >nul 2>nul")