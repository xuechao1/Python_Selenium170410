#coding=utf-8

from time import sleep
from selenium import webdriver
import unittest
class testcase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        pass
    def tearDown(self):
        self.driver.quit()
    def testcase1(self):
        """test case1测试用例1"""
        x=1
        self.assertEqual(x,1,"error")

    def testcase2(self):
        """test case2测试用例2"""
        x=2
        self.assertEqual(x,3,"error哈哈")