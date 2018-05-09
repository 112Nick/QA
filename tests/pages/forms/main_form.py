
from base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainForm(BaseElement):
    MESSAGE_BUTTON = '//div[@id="msg_toolbar_button"]'

    # def get_message_button(self):
    #     return self.driver.find_element_by_id(self.MESSAGE_BUTTON)

    def get_message_button(self):
        return  WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.MESSAGE_BUTTON)))



    # def get_message_button(self):
    #     return WebDriverWait(self.driver, 10, 0.1).until(
    #             lambda d: d.find_element_by_xpath(self.MESSAGE_BUTTON).text
    #         )