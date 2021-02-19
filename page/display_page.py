from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DisplayPage(BaseAction):

    search_button = By.ID,"com.android.settings:id/search"
    #点击搜索按钮
    def click_search(self):
        self.base_click(self.search_button)