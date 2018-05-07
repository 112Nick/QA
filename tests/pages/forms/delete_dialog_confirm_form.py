
from base_element import BaseElement

class DeleteDialogConfirmForm(BaseElement):
    CONFIRM_BUTTON = '//input[@id="hook_FormButton_menu_op_confirm_btn"]'
    def get_confirm_button(self):
        return self.driver.find_element_by_xpath(self.CONFIRM_BUTTON)
