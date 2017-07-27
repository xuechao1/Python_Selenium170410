#coding=utf-8
from cjol.public.method import *

login("http://www.cjol.com","xue10123456@163.com","123456789")
page_search(u"自动化测试",)
roll_down()
submit_element('span[id="btnApplyJob"][class="new_btn_login new_commonbtn_02"]')
finish(2)