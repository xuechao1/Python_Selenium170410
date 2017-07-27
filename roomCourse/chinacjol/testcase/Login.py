# coding=utf-8
import time,os
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
url="http://www.cjol.com/"
driver.get(url)
driver.implicitly_wait(15)
driver.find_element_by_link_text("个人登录").click()
time.sleep(1)
driver.find_element_by_id("txtUserName").send_keys("xue10123456@163.com")
driver.find_element_by_css_selector('input[type="text"][id="tbxPasswordTip"][class="lr_input_ps"]').click()
driver.find_element_by_id("txtPassword").send_keys("123456789")
driver.find_element_by_id("btnLogin_input").click()
time.sleep(2)
driver.find_element_by_id("a_MyResumeCenterAutoSearchResult").click()
time.sleep(0.5)
str1="马上设置！"
# if os.path.exists(str1):
#     driver.find_element_by_id("a_setsearchjobs").click()
# else:
#     pass
driver.find_element_by_id("a_setsearchjobs").click()
driver.find_element_by_id("txtKeyWord").send_keys(u"软件测试工程师")
driver.find_element_by_id("txtRegion").click()
time.sleep(0.5)
driver.find_element_by_link_text("深圳").click()
# driver.find_element_by_css_selector('a[class="common_alist"][href="javascript:;"]').click()
# driver.find_element_by_link_text("深圳"[1]).click()
# driver.find_element_by_css_selector('span[class="checkbox_txt checkbox_txt_hover"][text]').click()
driver.find_element_by_id("winLocation_dropdivselected_ok").click()
driver.find_element_by_id("btnSaveAndSearch").click()

time.sleep(1)

driver.quit()
