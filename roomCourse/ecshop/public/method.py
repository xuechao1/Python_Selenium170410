#coding=utf-8
from ecshop.public.base import *

def login(url,username,password):
    driver=open_browser("gc")
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(15)
    click_link_text(driver,"请登录")
    sleep(0.5)
    input_text(driver,'[name="username"]',username)
    input_text(driver,'[name="password"]',password)
    click_button(driver,'[name="submit"]')
    sleep(1)
    quit(driver)