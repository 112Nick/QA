from selenium.webdriver.support.ui import WebDriverWait

class BaseElement(object):
    def __init__(self, driver):
        self.driver = driver
    
    def wait_until_find_by_xpath(self,xpath):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(xpath)
            )
    def wait_for_presence(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.presence_of_element_located(self.locator)
        )
        return self

    def wait_for_visible(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.4).until(
            EC.visibility_of_element_located(self.locator)
        )
        return self

    def wait_for_alert(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.alert_is_present()
        )
        return self