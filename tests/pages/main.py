from base_page import BasePage
from forms.main_form import MainForm

class MainPage(BasePage):
    
    def open_messages(self):
        BEFORE = self.driver.current_url
        AFTER = self.driver.current_url
        main_form = MainForm(self.driver)
        while (BEFORE == AFTER):
            print 'open messages'
            
            main_form.get_message_button().click()
            AFTER = self.driver.current_url