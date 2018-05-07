
from base_element import BaseElement

class MainForm(BaseElement):
    MESSAGE_BUTTON = 'msg_toolbar_button'

    def get_message_button(self):
        return self.driver.find_element_by_id(self.MESSAGE_BUTTON)
