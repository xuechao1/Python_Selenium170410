#coding=utf-8
from roomCourse.Public.ITLEOFramework import ITleoFramework
from time import sleep
import unittest,time

class baiduTest(unittest.TestCase):

    def setUp(self):
        self.driver = ITleoFramework("chrome")
        self.driver.wait(10)
        self.base_url = "http://172.16.3.158/ecshop"

    def test_case(self):
        driver = self.driver
        driver.open(self.base_url)
        driver.click_text("请登录")
        try:
            driver.input_text('css=>input[name="username"]',"duandongbo")
            driver.input_text('css=>[id="username222"]', "duandongbo")
        except Exception ,e:
            driver.save_windows_img(driver.get_image_path())
            print e

        sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()