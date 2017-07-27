#coding=utf-8
import unittest
from time import sleep

import self as self
from selenium import webdriver

driver=webdriver.Chrome()

class testCjol(unittest.TestCase):

    def __init__(self,url):
        self.open_browser_ch=webdriver.Chrome()
        self.open_browser_ff = webdriver.Firefox()
        self.open_browser_ie = webdriver.Ie()
        self.open_browser_get=driver.get(url)
        self.open_browser_max=driver.maximize_window()

    def login_person(self,keywords):
        self.loginMy=driver.find_element_by_link_text(keywords).click()

    def input_text(self,text,input):
        self.input_text_id=driver.find_element_by_id(text).send_keys(input)
        self.input_text_xpath=driver.find_element_by_xpath(text).send_keys(input)
        self.input_text_css=driver.find_element_by_css_selector(text).send_keys(input)
        self.input_text_name=driver.find_element_by_name(text).send_keys(input)
        self.input_text_idlocate=driver.find_element_by_id(text).click()

    def login_button_click(self,input):
        self.login_button_click=driver.find_element_by_id(input).click()

    def login_wait(self,num):
        self.login_wait=sleep(num)

    def login_input(self,inputkey):
        pass





