#coding=utf-8
from ecshop.public.base import *

def login(url,username,passwd):
    driver=open_browser('gc')
    driver.get(url)
    driver.implicitly_wait(20)
    click_link(driver,"请登录")
    input_text(driver,'[name="username"]',username)
    input_text(driver,'[name="password"]',passwd)
    click_element(driver,'[name="submit"]')
    quit(driver)