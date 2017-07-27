#coding=utf-8
from cjol.public import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import unittest
import time
import re
# import HTMLTestRunner
class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url="http://www.baidu.com"
        self.verficationErrors=[]
        self.accept_next_alert=True
    def test_search(self):
        driver = self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id("kw").clear()
        time.sleep(1)
        driver.find_element_by_id("kw").send_keys(u"自动化测试")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.find_element_by_id("su").submit()
        time.sleep(3)
        title=driver.title
        print ("title is %s"%title)
        time.sleep(5)
        driver.close()
    def test_link(self):
        driver=self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_link_text("贴吧").click()
        time.sleep(5)
        driver.close()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors)
if __name__=="__main__":
    unittest.main()