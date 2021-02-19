from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MobileWebPage(BaseAction):

    first_network_button = By.XPATH,"//*[@text='首选网络类型']"

    network_2G_button = By.XPATH,"//*[@text='2G']"

    network_3G_button = By.XPATH, "//*[@text='3G']"

    def click_first_network(self):
        self.base_click(self.first_network_button)

    def click_2G(self):
        self.base_click(self.network_2G_button)

    def click_3G(self):
        self.base_click(self.network_3G_button)