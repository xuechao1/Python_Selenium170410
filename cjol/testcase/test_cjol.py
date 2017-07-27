#coding=utf-8
from selenium import webdriver
import unittest,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class Cjol(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.send_url="http://www.cjol.com"
        self.driver.implicitly_wait(4)

    def login(self):
        driver=self.driver
        driver.get(self.send_url)
        driver.find_element_by_link_text("个人登录").click()
        time.sleep(1)
        driver.find_element_by_id("txtUserName").clear()
        driver.find_element_by_id("txtUserName").send_keys("xue10123456@163.com")
        driver.find_element_by_css_selector('input[type="text"][id="tbxPasswordTip"][class="lr_input_ps"]').click()
        driver.find_element_by_id("txtPassword").send_keys("123456789")
        driver.find_element_by_css_selector('[id="btnLogin_input"][value="登 录"]').click()
        time.sleep(2)
        driver.find_element_by_css_selector('a[id="a_MyResumeCenterAutoSearchResult"]').click()
        time.sleep(1)
        try:
            driver.find_element_by_id("a_setsearchjobs").click()
            driver.find_element_by_id("txtKeyWord").send_keys(u"软件测试")
            driver.find_element_by_id("txtRegion").click()
            time.sleep(0.5)
            driver.find_element_by_link_text("深圳").click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="winLocation_dropdivrdiv_2008"]/div/div[1]/div/p/span').click()
            time.sleep(0.5)
            driver.find_element_by_id("winLocation_dropdivselected_ok").click()
            time.sleep(0.5)
            driver.find_element_by_id("btnSaveAndSearch").click()
        except:
            driver.find_element_by_id("btnSaveAndSearch").click()
        time.sleep(2)
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1.5)
        driver.find_element_by_id("foldbutton").click()
        str1 = ["深圳市华辰软通信息咨询有限公司", "深圳市鸿程信息技术有限公司", "深圳市华腾科创信息技术有限公司", "深圳市丰泽高科信息技术有限公司", "深圳市文思联合网络技术有限公司",
                "深圳凌岳软件有限公司", "深圳无觅科技有限公司"]
        ele=driver.find_elements_by_class_name("results_list_box")
        print len(ele)
        for i in ele:
            name=i.find_element_by_class_name("list_type_second").text
            if name.encode("utf-8") not in str1:
                try:
                    i.find_element_by_css_selector('input[type="checkbox"]').click()
                    js = "var q=document.body.scrollTop=2600"
                    driver.execute_script(js)
                except:
                    pass
        driver.find_element_by_link_text(str(2)).click()
        time.sleep(2)
        ele = driver.find_elements_by_class_name("results_list_box")
        for i in ele:
            name=i.find_element_by_class_name("list_type_second").text
            if name.encode("utf-8") not in str1:
                try:
                    i.find_element_by_css_selector('input[type="checkbox"]').click()
                    js = "var q=document.body.scrollTop=2600"
                    driver.execute_script(js)
                except:
                    pass

        time.sleep(1)
        driver.find_element_by_id("btnApplyJob").click()
        time.sleep(1.5)
        driver.switch_to.frame("appjob_iframe")
        driver.find_element_by_id("btnApply").click()
        time.sleep(1.5)
        driver.find_element_by_id("finish").click()
        time.sleep(1)


    def isPresent(self):
        driver=self.driver
        try:
            driver.find_element_by_xpath('//*[@id="btnApplyJob"]')
        except Exception,e:
            return False
        return True

    def driver_wait(self):
        driver=self.driver
        wait=WebDriverWait(driver,5)
        ele=wait.until(lambda x:x.find_element_by_xpath('//*[@id="btnApplyJob"]'))
        ele.click()

    def choose_page2(self,num):
        driver=self.driver
        for i in range(1,num+1):
            if i!=1:
                driver.find_element_by_link_text(str(i)).click()
            try:
                custom_choose()
                apply()
            except:
                pass

    def custom_select_job(self):
        # 自定义工作的选择，设定工作循环投递几页
        driver=self.driver
        for select_job_num in range(1, job_page_num):
            if select_job_num != 1:
                driver.find_element_by_link_text(str(select_job_num)).click()
            try:
                select_job()
                finish_job()
                logger.info("starting  " + str(select_job_num) + "  page....")
            except:
                pass


    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main