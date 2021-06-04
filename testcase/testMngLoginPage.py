# _*_ coding:utf-8 _*_

from selenium import webdriver
import unittest, time
from common import fileOperation

class TestMngLoginPage():

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://test4-h5-pyp-mng.chuxingyouhui.com/#/login?redirect=%2Fdashboard"

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(2)
        driver.find_element_by_xpath("//div[3]/button/span").click()
        time.sleep(1)
        driver.find_element_by_id("tab-login-text").click()
        driver.find_element_by_name("data[username]").click()
        driver.find_element_by_name("data[username]").clear()
        driver.find_element_by_name("data[username]").send_keys("sumeilan")
        driver.find_element_by_name("data[password]").click()
        driver.find_element_by_name("data[password]").clear()
        driver.find_element_by_name("data[password]").send_keys("Sml08240824$")
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def teardown_class(self):
        cookies = self.driver.get_cookies()

        print('cookies',cookies)
        for c in cookies:
            if c['name'] == 'Admin-Token-0':
                print('----------------',c['value'])
                fileOperation.add_write_file({"admin_token": c['value']}, 'params.json')
        time.sleep(1)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
