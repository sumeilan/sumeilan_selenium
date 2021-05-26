# _*_ coding:utf-8 _*_


from selenium import webdriver
import unittest, time
from pages.loginPage import LoginPage
from selenium.webdriver.common.keys import Keys


class TestLoginPage():

    def setup_class(self):
        option = webdriver.ChromeOptions()
        mobile_emulation = {"deviceName": "iPhone 6"}
        option.add_experimental_option("mobileEmulation", mobile_emulation)
        option.add_experimental_option('useAutomationExtension', False)
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=option)
        self.base_url = "https://test12-m.black-unique.com/login?refer=%2Fnew%2Findex.html%23%2Fhome"

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)

        login_Page = LoginPage(driver)
        time.sleep(3)

        login_Page.input_phone_text('18825076907')
        login_Page.input_msg_text('123456')
        login_Page.click_login_btn()
        time.sleep(1)

        flag = TestLoginPage.isElementExist(self, "//div[@id='app']/div[5]/div/button")
        if flag:
            driver.find_element_by_xpath("//div[@id='app']/div[5]/div/button").send_keys(Keys.ENTER)

        time.sleep(2)
        result = TestLoginPage.isElementExist(self, "//main[@id='app']/section/div[3]/div/div/ul/a/li/i")
        assert (result, True)

    # 判断元素是否存在
    def isElementExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_xpath(element)
            return flag

        except:
            flag = False
            return flag

    def teardown_class(self):
        print('test')
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()
