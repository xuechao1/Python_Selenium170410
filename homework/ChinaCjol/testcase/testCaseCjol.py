#coding=utf-8
from ChinaCjol.public.Basic import *

url="http://www.cjol.com"
# ChinarCjolTest.open_browser_ch
testCjol.open_browser_get(url)
testCjol.open_browser_max
testCjol.loginMy("个人登录")
testCjol.login_wait(1)
testCjol.input_text_id("txtUserName","xue10123456@163.com")
testCjol.input_text_idlocate("tbxPasswordTip").click()
testCjol.input_text_id("txtPassword","123456789")
testCjol.login_button_click("btnLogin_input")