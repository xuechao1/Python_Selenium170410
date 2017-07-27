#coding=utf-8
from selenium import webdriver
from time import sleep

def open_browser(brname):
    """open browser"""
    if brname=="ff" or brname=='firefox':
        driver=webdriver.Firefox()
    elif brname in ("chrome","gc","googlechrome"):
        driver=webdriver.Chrome()
    elif brname in ("ie","iexplore"):
        driver=webdriver.Ie()
    else:
        driver=webdriver.Chrome()
    return driver

def click_link_text(driver,text):
    """link text"""
    driver.find_element_by_link_text(text).click()

def locate_element(driver,element):
    driver.find_element_by_link_text(element)

def input_text(driver,text,value):
    """input link"""
    # driver.find_element_by_id(text).clear()
    # sleep(0.5)
    driver.find_element_by_id(text).send_keys(value)

def click_element(driver,element):
    driver.find_element_by_css_selector(element).click()

def click_id(driver,id):
    driver.find_element_by_id(id).click()

def click_xpath(driver,text):
    driver.find_element_by_xpath(text)

def click_button(driver,text):
    driver.find_element_by_id(text).click()


def get_titile(driver,name):
    pass

def quit(driver):
    driver.quit()
