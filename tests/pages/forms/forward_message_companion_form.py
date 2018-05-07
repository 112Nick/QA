from base_element import BaseElement

class ForwardMessageCompanionForm(BaseElement):
    COMPANION_BUTTON = '//div[@data-l="t,conv-select"]'
    FORWARD_MESSAGE_BUTTON = '//input[@class="button-pro __small mr-2x js-submit"]'
    
    def get_companion_button(self):
        return self.driver.find_element_by_xpath(self.COMPANION_BUTTON)
   
    def get_forward_message_button(self):
        return self.driver.find_element_by_xpath(self.FORWARD_MESSAGE_BUTTON)