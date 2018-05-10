from base_page import BasePage
from forms.dialog_menu_form import DialogMenuForm

class DialogMenuPage(BasePage):


    def delete_dialog(self):
        dialog_menu_form = DialogMenuForm(self.driver)
        dialog_menu_form.get_delete_dialog_button().click()

    def leave_chat(self):

        dialog_menu_form = DialogMenuForm(self.driver)
        dialog_menu_form.get_leave_chat_button().click()

    def hide_chat(self):
        dialog_menu_form = DialogMenuForm(self.driver)
        dialog_menu_form.get_hide_chat_button().click()
