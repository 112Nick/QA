# -*- coding: utf-8 -*-
from base_element import BaseElement

class MessageForm(BaseElement):
    CREATE_DIALOG_BUTTON = '//span[@id="chats_create_button"]'
    FIND_MESSAGE_INPUT = '//input[@id="ConversationsListSearch_field_query"]'


    def get_create_dialog_button(self):
    #    return self.wait_until_find_by_xpath(self.CREATE_DIALOG_BUTTON)
        return self.driver.find_element_by_xpath(self.CREATE_DIALOG_BUTTON)

    def get_find_message_input(self):
        return self.driver.find_element_by_xpath(self.FIND_MESSAGE_INPUT)