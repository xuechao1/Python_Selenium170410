#coding=utf-8
from selenium import webdriver
import time
br=webdriver.Chrome()
br.implicitly_wait(20)
br.get("C:\\Users\\Administrator\\Desktop\\购物流程_ECSHOP演示站 - Powered by ECShop.html")

def shping_choose(name):
    #xpath  开头/html从祖辈元素查找  //匹配后面的元素，不需要从祖辈元素查找
    try:
        # .  代表  当前的这一行的元素去匹配
        ele=br.find_element_by_xpath('//table/tbody/tr[contains(.,"'+name+'")]')
        time.sleep(0.5)
        ele.find_element_by_css_selector('input[type="radio"]').click()
        return True
    except:
        return False
shping_choose("精品包装")

#临时修改cmd窗口大小 mod con cols