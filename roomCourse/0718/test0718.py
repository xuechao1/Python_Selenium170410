#coding=utf-8
from selenium import  webdriver
br=webdriver.Chrome()
br.implicitly_wait(30)
br.get("http://172.16.3.158/ecshop")
br.find_element_by_link_text("请登录").click()
#id和name都存在的时候 任选一种方式都可以
# br.find_element_by_name("username").send_keys("admin")
# br.find_element_by_id("username").send_keys("admin")

#css选择器
# br.find_element_by_css_selector('input[size="25"]').clear()  #清空输入框
# #br.find_element_by_css_selector('input[size="25"]').send_keys("duandongbo")
# #同名元素 在css方法的时候 可以加多个属性来查找元素
# #br.find_element_by_css_selector('input[type="text"][class="inputBg"]').send_keys("duandongbo1")
# #如果属性唯一的话 可以不用标签 直接写属性
# br.find_element_by_css_selector('[class="inputBg"]').send_keys("duandongbo1")
# print br.find_element_by_css_selector('[class="inputBg"]')

#同名元素
# ele= br.find_elements_by_css_selector('input[type="text"]')
# ele[0].send_keys("admin")
# ele[1].send_keys("ecshop")

#class
# br.find_element_by_class_name("inputBg").send_keys("admin")

#xpath(杀手锏)
br.find_element_by_xpath("/html/body/div[6]/div[]/form/table/tbody/tr[1]/td[2]/input").send_keys("admin123")

#br.find_element_by_css_selector('a[href="asdf"]')