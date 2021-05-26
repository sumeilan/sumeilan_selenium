from selenium.webdriver.common.by import By
from pages.basePage import Page


class LoginPage(Page):
    # 手机输入框
    phone_input = (By.XPATH, "(//input[@name='name'])[2]")
    # 验证码输入框
    msg_input = (By.NAME, "msgNum")
    # 登录按钮
    login_button = (By.XPATH, "//div[@id='app']/button")

    def __init__(self, driver):
        Page.__init__(self, driver)

    def input_phone_text(self, text):
        self.input_text(self.phone_input, text)

    def input_msg_text(self, text):
        self.input_text(self.msg_input, text)

    def click_login_btn(self):
        self.click(self.login_button)
