#coding=utf-8
from selenium import webdriver
import os,time

# br=webdriver.Chrome()
br=webdriver.Firefox()
path=os.getcwd()
# br.get("D:\\xuechao\\form.html")  #chrome
# br.get("file:///d:/xuechao/form.html")  #friefox
#消息弹窗
# br.find_element_by_id("alert").click()
# time.sleep(1)
# br.switch_to.alert.accept()
# time.sleep(1)
# br.quit()
# br.switch_to_alert().accept()
#提示弹窗
# br.find_element_by_id("prompt").click()
# time.sleep(1)
# print br.switch_to.alert.text  #获取提示窗口标题
# br.switch_to.alert.send_keys("admin")
# time.sleep(0.5)
# br.switch_to.alert.dismiss()
# time.sleep(1)
# br.quit()
#确认弹窗
# br.find_element_by_id("confirm").click()
# time.sleep(1)
# # br.switch_to.alert.accept()
# br.switch_to.alert.dismiss()
# time.sleep(1)
# br.quit()
#多窗口切换
# br.find_element_by_id("opennew").click()
# time.sleep(1)
# all_window=br.window_handles#获取当前所有浏览器的句柄值
# print br.current_window_handle
# br.switch_to.window(all_window[1])
# br.find_element_by_id("name").send_keys("xuechao")
# time.sleep(1)
# br.switch_to.window(all_window[0])
# br.find_element_by_id("name").send_keys("xuechao11111")
# time.sleep(1)
# br.quit()

#多窗口切换(判断)
# current_window=br.current_window_handle  #获取当前窗口句柄值
# br.find_element_by_id("opennew").click()
# time.sleep(1)
# all_window=br.window_handles  #获取当前所有窗口句柄值
# for i in all_window:   #遍历所有句柄值
#     if i!=current_window: #如果句柄值不等于当前窗口，那就是新窗口
#         br.switch_to.window(i)   #切换到新窗口
#         br.find_element_by_id("name").send_keys("xuechao12")
#         time.sleep(0.5)
#         br.close()
#         break
# br.switch_to.window(current_window)  #切换到原始窗口，就是第一次打开的窗口
# br.find_element_by_id("name").send_keys("xuechao123")
# time.sleep(1)
# br.quit()
#框架切换
# br.get("file:///d:/xuechao/iframe_test.html")
# time.sleep(3)
# # br.switch_to.default_content()
# # time.sleep(1)
# # br.switch_to.frame()  #只能传入frame
# ele = br.find_element_by_xpath('//*[@id="ls_username"]')
# print ele
# br.switch_to.frame(ele)
# br.find_element_by_id("ls_username").send_keys("admin")
# time.sleep(1)
# br.switch_to.default_content()  #切换到默认内容（切换到默认的网页，不是框架）
# br.find_element_by_id("name").send_keys("123123123")

#键盘操作
# from selenium.webdriver.common.keys import Keys
# br.get("file:///d:/xuechao/form.html")
# br.implicitly_wait(20)
# br.find_element_by_id("self_intr").send_keys(Keys.CONTROL+'a')
# time.sleep(1)
# br.find_element_by_id("self_intr").send_keys(Keys.CONTROL+'x')
# time.sleep(1)
# br.find_element_by_id("self_intr").send_keys(u'隔壁家的小棍')
# time.sleep(1)
# br.quit()
#模拟鼠标
from selenium.webdriver.common.action_chains import ActionChains
br.get("file://172.16.3.158/ecshop")
br.implicitly_wait(20)
ele=br.find_element_by_xpath('//*[@id="category_tree"]/div[1]')
ele=br.find_elements_by_link_text("家用电器")
ActionChains(br).move_to_element(ele[1]).perform()
time.sleep(3)
ele=br.find_elements_by_link_text("大家电")
ActionChains()
time.sleep(1)
br.quit()






