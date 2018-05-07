# -*- coding: utf-8 -*-
from base_element import BaseElement

class DialogForm(BaseElement):
    MENU_BUTTON = '//div[@class="ic inlineBlock ic_info-menu"]'

    SEND_MESSAGE_BUTTON = '//button[@title="Отправить"]'
    MESSAGE_INPUT = "//div[@name='st.txt']"
    
    DELETE_MESSAGE_BUTTON =  "//a[@data-l='t,deleteMsg']"
    EDIT_MESSAGE_BUTTON = "//a[@data-l='t,editMsg']"
    ANSWER_MESSAGE_BUTTON = "//span[@data-l='t,replyToMsg']"
    FORWARD_MESSAGE = "//span[@data-l='t,forward']"
    

    def get_menu_button(self):
        return self.driver.find_element_by_xpath(self.MENU_BUTTON)
   
    def get_send_message_button(self):
        return self.driver.find_element_by_xpath(self.SEND_MESSAGE_BUTTON)

    def get_delete_message_button(self):
        return self.driver.find_element_by_xpath(self.DELETE_MESSAGE_BUTTON)

    def get_edit_message_button(self):
        return self.driver.find_element_by_xpath(self.EDIT_MESSAGE_BUTTON)
   
    def get_answer_message_button(self):
        return self.driver.find_element_by_xpath(self.ANSWER_MESSAGE_BUTTON)

    def get_message_input(self):
        return self.driver.find_element_by_xpath(self.MESSAGE_INPUT)

    def get_forward_message(self):
        return self.driver.find_element_by_xpath(self.FORWARD_MESSAGE)