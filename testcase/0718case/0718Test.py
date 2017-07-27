#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
br= webdriver.Chrome()
#最大化窗口
br.maximize_window()
br.get("http://172.16.3.158/ecshop")
br.implicitly_wait(10)
br.find_element_by_link_text("请登录").click()
#css选择器
# br.find_element_by_css_selector('input[size="25"]').clear()
#同名元素，在css方法时 可以加多个属性来查
# br.find_element_by_css_selector('input[type="text"][size="25"][class="inputBg"]').send_keys("xuechao")
#属性如果唯一的话 可以不用标签直接用属性
#br.find_element_by_css_selector('class="inputBg"').send_keys("xuechao")
#同名元素
# ele=br.find_elements_by_css_selector('input[type="text"]')
# ele[0].send_keys("admin")
# ele[1].send_keys("xuechao")
#class
# br.find_element_by_class_name("inputBg").send_keys("duandongbo")
# #xpath(杀手锏)
# br.find_element_by_xpath("html/body/div[6]/div[1]/form/table/tbody/tr[1]/td[2]/input").send_keys("admin")
#login
br.find_element_by_name("username").send_keys("xuechao")
br.find_element_by_name("password").send_keys("123456")
br.find_element_by_name("submit").click()
try:
    br.find_element_by_css_selector('font[class="f4_b"]').text
    print "登录成功"
except:
    print "登录失败"
# #服装
# br.find_element_by_link_text("服装").click()
# br.find_element_by_css_selector('a[href="goods.php?id=47"]').click()
# # br.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[1]/form/div/div/div[2]/div/div[3]/a").click()
# sleep(1)
# #输入数量
# br.find_element_by_id("number").clear()
# sleep(0.5)
# br.find_element_by_id("number").send_keys("2")
# #购买
# br.find_element_by_css_selector('img[src="themes/default/images/buybtn1.png"]').click()
# #去结算
# br.find_element_by_css_selector('img[src="themes/default/images/checkout.gif"]').click()
# #下拉框
# try :
#     ele=br.find_element_by_id("selProvinces_0")
#     Select(ele).select_by_visible_text("河南省")
#     ele1=br.find_element_by_id("selCities_0")
#     Select(ele1).select_by_visible_text("郑州市")
#     Select(br.find_element_by_id("selDistricts_0")).select_by_visible_text("中原区")
#     br.find_element_by_css_selector('input[class="inputBg"][id="consignee_0"]').send_keys(u"薛超")
#     br.find_element_by_id("address_0").send_keys(u"二七纪念塔")
#     br.find_element_by_id("tel_0").send_keys("14787184016")
#     br.find_element_by_name("Submit").click()
# except :
#     pass
# #配送方式
# br.find_element_by_css_selector('input[value="3"][supportcod="1"]').click()
# #支付方式
# br.find_element_by_css_selector('input[name="payment"][value="2"]').click()
# #祝福贺词
# br.find_element_by_css_selector('textarea[name="card_message"][cols="60"][rows="3"]').send_keys(u"盛开的解放路睡觉\n流口水的积分")
# #订单附言
# br.find_element_by_css_selector('textarea[name="postscript"][cols="80"][rows="3"]').send_keys(u"水电费家里的事会计法\n双方家里看到")
# #提交订单
# br.find_element_by_css_selector('input[src="themes/default/images/bnt_subOrder.gif"]').click()
# sleep(1)
# br.quit()
