from base_page import BasePage
from forms.pin_message_confirm_form import PinMessageConfirmForm



class PinMessageConfirmPage(BasePage):
    def confirm(self):
        pin_message_confirm_form = PinMessageConfirmForm(self.driver)
        pin_message_confirm_form.get_confirm_button().click()