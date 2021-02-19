from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MorePage(BaseAction):

    mobile_web_button = By.XPATH,"//*[@text='移动网络']"

    #点击移动网络
    def click_mobile_button(self):
        self.base_click(self.mobile_web_button)

