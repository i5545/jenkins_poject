import time
from appium import webdriver
from base.base_driver import init_driver
from page.page import Page


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_display(self):
        # 显示-搜索-输入hello-返回
        self.page.setting.click_display()
        self.page.display.click_search()
        self.page.search.input_text("hello")
        self.page.search.click_back()

