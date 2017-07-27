#coding=utf-8
from selenium import webdriver
from time import sleep

def open_browser(brname):
    """open browser"""
    if brname=="ff" or brname=="firefox" or brname=="Firefox":
        driver=webdriver.Firefox()
    elif brname=="Chrome" or brname=="gc" or brname=="googlechrome":
        driver=webdriver.Chrome()
    elif brname in ("ie","iexplore"):
        driver=webdriver.Ie
    else:
        driver=webdriver.Firefox
    return driver

def input_text(driver,element,value):
    """input text"""
    driver.find_element_by_css_selector(element).clear()
    sleep(0.5)
    driver.find_element_by_css_selector(element).send_keys(value)

def click_button(driver,element):
    """click button"""
    driver.find_element_by_css_selector(element).click()

def click_link_text(driver,text):
    """click text"""
    driver.find_element_by_link_text(text).click()

def quit(driver):
    """quit browser"""
    driver.quit()