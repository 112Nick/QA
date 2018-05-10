# -*- coding: utf-8 -*-
from base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DialogForm(BaseElement):
    MENU_BUTTON = '//div[@data-additional-button="js-open-menu"]'
    ADD_USER_BUTTON = '//span[@class="inlineBlock ic ic_add-user"]'
    CONTROLE_USERS_BUTTON = '//span[@class="inlineBlock ic ic_ffriend"]'
    UNPIN_MESSAGE_BUTTON = "//a[@class='ic ic_close-g chat_pinned_close']"

    COMPANION_BUTTON = "//div[@data-l='t,participant-add']" 
    DELETE_COMPANION_BUTTON = "//span[@data-l='t,participant-remove']"
    ADD_USER_CONFIRM_BUTTON = "//input[@value='Добавить']" 

    SEND_MESSAGE_BUTTON = '//button[@title="Отправить"]'
    MESSAGE_INPUT = "//div[@name='st.txt']"
    
    DELETE_MESSAGE_BUTTON =  "//a[@data-l='t,deleteMsg']"
    PIN_MESSAGE_BUTTON =  "//a[@data-l='t,pinMsg']"
    EDIT_MESSAGE_BUTTON = "//a[@data-l='t,editMsg']"
    ANSWER_MESSAGE_BUTTON = "//span[@data-l='t,replyToMsg']"
    FORWARD_MESSAGE = "//span[@data-l='t,forward']"

    NO_MESSAGES_TEXT = '//div[@class="stub-empty_t"]'



    def get_menu_button(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.MENU_BUTTON)))
        # return self.driver.find_element_by_xpath(self.MENU_BUTTON)

    def get_add_user_button(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_USER_BUTTON)))
    
    def get_controle_users_button(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.CONTROLE_USERS_BUTTON)))

    def get_delete_companion_button(self):
        return self.driver.find_elements_by_xpath(self.DELETE_COMPANION_BUTTON)
   
    def get_send_message_button(self):
        return self.driver.find_element_by_xpath(self.SEND_MESSAGE_BUTTON)

    def get_delete_message_button(self):
        return self.driver.find_element_by_xpath(self.DELETE_MESSAGE_BUTTON)

    def get_pin_message_button(self):
        return self.driver.find_element_by_xpath(self.PIN_MESSAGE_BUTTON)

    def get_edit_message_button(self):
        return self.driver.find_element_by_xpath(self.EDIT_MESSAGE_BUTTON)
   
    def get_answer_message_button(self):
        return self.driver.find_element_by_xpath(self.ANSWER_MESSAGE_BUTTON)

    def get_unpin_button(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.UNPIN_MESSAGE_BUTTON)))

    def get_message_input(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.MESSAGE_INPUT)))

    def get_forward_message(self):
        return self.driver.find_element_by_xpath(self.FORWARD_MESSAGE)

    def get_no_messages_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.NO_MESSAGES_TEXT)))
        # return self.driver.find_element_by_xpath(self.NO_MESSAGES_TEXT)

    def get_companion_button(self):
        return self.driver.find_elements_by_xpath(self.COMPANION_BUTTON)

    def get_add_user_confirm_button(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_USER_CONFIRM_BUTTON)))