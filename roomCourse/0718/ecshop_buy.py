#coding=utf-8
from selenium import  webdriver  #从selenium包导入webdriver模块
from selenium.webdriver.support.ui import Select  #导入select方法
# from selenium.webdriver.common.action_chains import ActionChains
import time #导入时间模块
br=webdriver.Firefox()  #确定测试要使用的浏览器 把浏览器对象赋值给一个变量
br.implicitly_wait(20) #隐性等待 也叫智能等待，最长等待20秒
br.get("http://172.16.3.158/ecshop")  #浏览器打开要测试的网址
br.maximize_window()   #最大化浏览器窗口

#login
br.find_element_by_link_text("请登录").click()  #link_text 点击文本链接  在html里面一般是a标签
br.find_element_by_name("username").send_keys("zhaosi6") #输入框里面输入用户名
br.find_element_by_name("password").send_keys("123123")     #输密码
br.find_element_by_name("submit").click()  #点击登录按钮
try:
    br.find_element_by_css_selector('font[class="f4_b"]')
    print "登录成功"
except:
    print "登录失败"

#shoping
br.find_element_by_link_text("服装").click()  #点击菜单的服装 文本链接
br.find_element_by_css_selector('a[href="goods.php?id=44"]').click()  #点击第二件衣服的 购买按钮
#选择数量
br.find_element_by_id("number").clear()  #清除文本框原有的数据
time.sleep(0.5)
br.find_element_by_id("number").send_keys("3") #在文本框里面输入我们自定义的数据
#结算
br.find_element_by_css_selector('img[src="themes/default/images/buybtn1.png"]').click() #点击图片按钮
br.find_element_by_css_selector('img[src="themes/default/images/checkout.gif"]').click() #点击图片按钮
#填写收货人信息（下拉框选择）
try:
    Select(br.find_element_by_name("country")).select_by_visible_text("中国") #选择下拉框的国家
    Select(br.find_element_by_name("province")).select_by_visible_text("广东省") #
    Select(br.find_element_by_name("city")).select_by_visible_text("深圳市")
    Select(br.find_element_by_name("district")).select_by_visible_text("南山区")
    Select(br.find_element_by_name("country")).select_by_visible_text("中国")
    br.find_element_by_name("consignee").send_keys(u"段")  #输入收件人名字（中文要编码成unicode）
    br.find_element_by_name("address").send_keys(u"虚拟大学园W1-A") #输入地址
    br.find_element_by_name("tel").send_keys("13412234124")  #输入手机号码
    br.find_element_by_name("Submit").click()  #点击配置到这个地址按钮
except:
    pass
#选择配送方式和支付方式
br.find_element_by_css_selector('input[name="shipping"][value="6"]').click()
br.find_element_by_css_selector('input[name="payment"][value="2"]').click()
#贺卡
br.find_element_by_css_selector('input[name="card"][value="1"]').click()
br.find_element_by_name("card_message").send_keys(u"生日快乐888888q")
#提交订单
br.find_element_by_css_selector('input[src="themes/default/images/bnt_subOrder.gif"]').click() #点击图片按钮
time.sleep(3)  #休息3秒钟
br.quit()  #浏览器结束运行


