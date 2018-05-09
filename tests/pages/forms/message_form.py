# -*- coding: utf-8 -*-
from base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MessageForm(BaseElement):
    CREATE_DIALOG_BUTTON = '//span[@id="chats_create_button"]'
    FIND_MESSAGE_INPUT = '//input[@id="ConversationsListSearch_field_query"]'


    def get_create_dialog_button(self):
    #    return self.driver.find_element_by_xpath(self.CREATE_DIALOG_BUTTON)
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_DIALOG_BUTTON)))

        

    def get_find_message_input(self):
        return self.driver.find_element_by_xpath(self.FIND_MESSAGE_INPUT)


        