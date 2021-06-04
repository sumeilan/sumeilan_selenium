# _*_ coding:utf-8 _*_

import sys

# pages基类
class Page(object):
    """
        Page基类，所有page都应该继承该类
    """
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.find_element(*loc).click()

    def send_keys(self, loc, key):
        self.find_element(*loc).send_keys(key)

    def get_title(self):
        return self.driver.title

    def isElementExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_xpath(element)
            return flag

        except:
            flag = False
            return flag

