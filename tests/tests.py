# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from pages.auth import AuthPage
from pages.main import MainPage
from pages.message import MessagePage
from pages.dialog import DialogPage
from pages.dialog_menu import DialogMenuPage
from pages.delete_dialog_confirm import ConfirmPage
from pages.delete_message_confirm import DeleteMessageConfirmPage
from pages.pin_message_confirm import PinMessageConfirmPage


from time import sleep

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Tests(unittest.TestCase):    

    CREATED_DIALOG_URL = ''

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        print 'setUp'        
        auth_page = AuthPage(self.driver)
        auth_page.sign_in("technopark2","testQA1")
        main_page = MainPage(self.driver)
        main_page.open_messages() # Open chat's window

    def tearDown(self):
        print 'tearDown'      
        self.driver.get(self.CREATED_DIALOG_URL) 
        if(self.CREATED_DIALOG_URL[23] == 'c'):
            self.leave_group_chat()
        else:       
            # if(dialog_page.no_messages_text_exists() == False):
            self.delete_dialog()
        self.driver.quit()

    def create_dialog(self):
        print 'create_dialog'                
        message_page = MessagePage(self.driver)
        message_page.create_dialog() # Create new dialog
        message_page.choose_companion() # Choosing person to start dialog with
        return message_page

    def delete_dialog(self):
        print 'delete_dialog'                
        dialog_page = DialogPage(self.driver)
        dialog_page.open_menu() # Opening dialog menu in the right top corner
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.delete_dialog()
        delete_dialog_confirm_page = ConfirmPage(self.driver)
        delete_dialog_confirm_page.confirm()
    
    def leave_group_chat(self):
        print 'leave_group_chat'                        
        dialog_page = DialogPage(self.driver)  
        dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.leave_chat()
        leave_chat_confirm_page = ConfirmPage(self.driver)
        leave_chat_confirm_page.confirm()


    def test_send_message(self):
        print 'test_send_message'        
        MESSAGE_TEXT = 'TestNumber1'  
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        self.CREATED_DIALOG_URL = self.driver.current_url
        # self.assertEquals(dialog_page.no_messages_text_exists(), False)
        
    def test_edit_message(self):
        print 'test_edit_message'                
        MESSAGE_TEXT = 'TestNumber1'  
        MESSAGE_EDITED_TEXT = ' IS_EDITED'      
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        dialog_page.edit_and_send_message(MESSAGE_EDITED_TEXT) 
        self.CREATED_DIALOG_URL = self.driver.current_url
    
    def test_delete_message(self):
        print 'test_delete_message'                
        MESSAGE_TEXT = 'TestNumber1'          
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        self.CREATED_DIALOG_URL = self.driver.current_url
        dialog_page.delete_message()
        delete_message_confirm_page = DeleteMessageConfirmPage(self.driver)
        delete_message_confirm_page.delete_message()
        self.driver.refresh()
        self.assertEquals(dialog_page.no_messages_text_exists(), True)

    def test_answer_message(self):
        print 'test_answer_message'                
        MESSAGE_TEXT = 'TestNumber1'  
        MESSAGE_ANSWERED_TEXT = ' IS_ANSWERED'  
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        dialog_page.answer_message(MESSAGE_ANSWERED_TEXT)
        self.CREATED_DIALOG_URL = self.driver.current_url

    def test_forward_message(self):
        print 'test_forward_message'                
        MESSAGE_TEXT = 'TestNumber1'      
        message_page = self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        self.CREATED_DIALOG_URL = self.driver.current_url
        dialog_page.forward_message()
        message_page.choose_companion_forward_message()
    
    def test_find_message(self):
        print 'test_find_message'                
        MESSAGE_TEXT = 'TestNumber1'  
        message_page = self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        self.CREATED_DIALOG_URL = self.driver.current_url
        message_page.find_message(MESSAGE_TEXT)
        # self.assertEquals(dialog_page.no_messages_text_exists(), False)
        
    def test_add_user_to_group_chat(self):
        print 'test add user to group chat'
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.add_user_to_chat()
        self.CREATED_DIALOG_URL = self.driver.current_url

    def test_delete_user_from_group_chat(self):
        print 'test delete user from group chat'
        MESSAGE_TEXT = 'TestNumber1'          
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.add_user_to_chat()
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        dialog_page.delete_user_from_chat()
        self.CREATED_DIALOG_URL = self.driver.current_url

    def test_pin_message(self):
        print 'test_pin_message'
        MESSAGE_TEXT = 'TestNumber1'  
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.add_user_to_chat()
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        self.CREATED_DIALOG_URL = self.driver.current_url        
        dialog_page.pin_message()
        pin_message_confirm_page = PinMessageConfirmPage(self.driver)
        pin_message_confirm_page.confirm()
        # sleep(5)
       
    def test_unpin_message(self):
        print 'test_unpin_message'
        MESSAGE_TEXT = 'TestNumber1'  
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.add_user_to_chat()
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        self.CREATED_DIALOG_URL = self.driver.current_url        
        dialog_page.pin_message()
        pin_message_confirm_page = PinMessageConfirmPage(self.driver)
        pin_message_confirm_page.confirm()
        sleep(5)
        dialog_page.unpin_message()
        pin_message_confirm_page.confirm()

    def test_hide_group_chat(self):
        print 'test_unpin_message'
        MESSAGE_TEXT = 'TestNumber1'  
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        dialog_page.add_user_to_chat()
        dialog_page.write_and_send_message(MESSAGE_TEXT)
        self.CREATED_DIALOG_URL = self.driver.current_url
        dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.hide_chat()
        hide_chat_confirm_page = ConfirmPage(self.driver)
        hide_chat_confirm_page.confirm()

   


       
