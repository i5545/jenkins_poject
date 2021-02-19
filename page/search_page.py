from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):

    search_text = By.ID,"android:id/search_src_text"

    back_button = By.CLASS_NAME,"android.widget.ImageButton"

    #输入hello
    def input_text(self,value):
        self.base_input(self.search_text,value)
    #点击返回
    def click_back(self):
        self.base_click(self.back_button)
