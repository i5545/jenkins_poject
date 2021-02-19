from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self,dirver):
        self.driver = dirver

    # 查找单个元素方法
    def find_element(self,feature,timeout = 5,poll = 1):
        feature_by, feature_value = feature
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(feature_by,feature_value))

    # 查找多个元素方法
    def find_elements(self, feature, timeout=5, poll=1):
        feature_by, feature_value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))

    #点击方法
    def base_click(self,feature):
        self.find_element(feature).click()


    #输入方法
    def base_input(self,feature,value):
        self.find_element(feature).send_keys(value)

    def base_clear(self, feature):
        self.find_element(feature).clear()

