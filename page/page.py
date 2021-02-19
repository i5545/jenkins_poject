from page.display_page import DisplayPage
from page.mobile_web_page import MobileWebPage
from page.more_page import MorePage
from page.search_page import SearchPage
from page.setting_page import SettingPage


class Page:

    def __init__(self,driver):
        self.driver = driver

    # @property装饰器会将方法转换为相同名称的只读属性
    # 将方法变成像属性一样调用
    # 在test页面中  调用可以直接  page.setting.click_more()
    #  不加也可以 调用 page.setting().click_more()
    #  加了方便阅读
    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def search(self):
        return SearchPage(self.driver)

    @property
    def more(self):
        return MorePage(self.driver)

    @property
    def mobile_web(self):
        return MobileWebPage(self.driver)

    @property
    def display(self):
        return DisplayPage(self.driver)