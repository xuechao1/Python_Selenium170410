#coding=utf-8
from selenium import  webdriver
from time import  sleep

def open_browser(brname):
    """open browser"""
    if brname=="ff" or brname=='firefox':
        driver=webdriver.Firefox()
    elif brname in ("chrome","gc","googlechrome"):
        driver=webdriver.Chrome()
    elif brname in ("ie","iexplore"):
        driver=webdriver.Ie()
    else:
        driver=webdriver.Firefox()
    return driver

def input_text(driver,element,value):
    """text input """
    driver.find_element_by_css_selector(element).clear()
    sleep(0.5)
    driver.find_element_by_css_selector(element).send_keys(value)

def click_element(driver,element):
    """click element"""
    driver.find_element_by_css_selector(element).click()

def click_link(driver,text):
    """text click"""
    driver.find_element_by_link_text(text).click()

def quit(driver):
    driver.quit()