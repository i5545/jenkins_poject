import time

from base.base_driver import init_driver
from page.page import Page


class TestMore:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_more_2G(self):
        # 更多-移动网络-首选网络类型-2G
        self.page.setting.click_more()
        self.page.more.click_mobile_button()
        self.page.mobile_web.click_first_network()
        self.page.mobile_web.click_2G()

    def test_more_3G(self):
        # 更多-移动网络-首选网络类型-3G
        self.page.setting.click_more()
        self.page.more.click_mobile_button()
        self.page.mobile_web.click_first_network()
        self.page.mobile_web.click_3G()