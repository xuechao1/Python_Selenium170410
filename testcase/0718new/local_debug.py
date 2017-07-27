#coding=utf-8
from selenium import  webdriver
import time
br=webdriver.Chrome()
br.implicitly_wait(20)
br.get("C:\\Users\\Dongboduan\\Desktop\\购物流程_ECSHOP演示站 - Powered by ECShop.htm")

def shping_choose(name):
    #xpath   开头/html从祖辈元素查找   //匹配后面的元素，不需要从祖辈元组查找
    try:
        ele=br.find_element_by_xpath('//table/tbody/tr[contains(.,"'+name+'")]')
        time.sleep(0.5)
        #ele.find_element_by_css_selector('input[type="radio"]').click() #css方式
        ele.find_element_by_xpath("td/input").click()
        return True
    except:
        return False

shping_choose("邮局")
shping_choose("货到付款")
shping_choose("货到付款")

#临时修改cmd窗口大小mode con cols=100 lines=20
#临时修改cmd窗口颜色 color fc
