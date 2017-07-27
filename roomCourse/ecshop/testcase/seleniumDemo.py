#coding=utf-8
from selenium import webdriver
from time import sleep
import unittest
from Unittest_demo.Public.ITLEOFramework import ITleoFramework

class ecshopTest():
    def setUp(self):
        self.driver=ITleoFramework("Chrome")
        self.driver.wait(10)
        self.driver.get_url("http://172.16.3.158/ecshop")
    def test_username_pwd(self):
        driver = self.driver
        driver.open(self.base_url)
        driver.click_text("请登录")
        try :
            driver.input_text('css=>input[name="username"]',"xuechao")
            driver.input_text('css=>input[name="password"]',"123456")
        except Exception, e:
            driver.save_windows_img(driver.get_image_path())
            print e
