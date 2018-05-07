
from base_element import BaseElement

class DialogMenuForm(BaseElement):
    DELETE_DIALOG_BUTTON = '//i[@class="tico_img ic ic_remove"]'
    def get_delete_dialog_button(self):
        return self.driver.find_element_by_xpath(self.DELETE_DIALOG_BUTTON)