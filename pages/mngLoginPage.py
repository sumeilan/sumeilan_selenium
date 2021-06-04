from selenium.webdriver.common.by import By
from pages.basePage import Page
from selenium.webdriver.common.keys import Keys

class LoginPage(Page):
    # 手机输入框
    phone_input = (By.XPATH, "(//input[@name='name'])[2]")
    # 验证码输入框
    msg_input = (By.NAME, "msgNum")
    # 登录按钮
    login_button = (By.XPATH, "//div[@id='app']/button")
    # 弹窗确认按钮
    confirm_ele = "//div[@id='app']/div[5]/div/button"
    confirm_btn = (By.XPATH,confirm_ele)
    # 活动弹窗
    alter_ele = "//div[@id='viewpage']/div[8]/div/div[2]/div/div[2]"
    activity_alter = (By.XPATH,alter_ele)

    def input_phone_text(self, text):
        self.input_text(self.phone_input, text)

    def input_msg_text(self, text):
        self.input_text(self.msg_input, text)

    def click_login_btn(self):
        self.click(self.login_button)

    def enter_confirm_btn(self):
        flag = self.isElementExist(self.confirm_ele)
        if flag:
            self.send_keys(self.confirm_btn,Keys.ENTER)

    def close_activity_alter(self):
        act_alter = self.isElementExist(self.alter_ele)
        if act_alter:
            self.click(self.activity_alter)