from pages.base_page import BasePage
from data_user import DataUser
from locators.base_page_locators import BasePageLocators
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators


class RecoveryPasswordPage(BasePage):
    def click_to_link_recovery_password(self):
        self.wait_visibility_element(BasePageLocators.TITLE_LOGIN)
        self.click_to_element(RecoveryPasswordPageLocators.LINK_FORGOT_PASSWORD)

    def get_text_title_recovery_password_page(self):
        title_recovery_password_page = self.get_text(RecoveryPasswordPageLocators.TITLE_RECOVERY_PASSWORD)
        return title_recovery_password_page

    def input_email(self):
        self.send_data(BasePageLocators.INPUT_EMAIL, DataUser.LOGIN_USER)

    def click_to_button_recovery_password(self):
        self.click_to_element(RecoveryPasswordPageLocators.BUTTON_RECOVERY_PASSWORD)

    def get_current_url_recovery_password_page(self):
        self.wait_visibility_element(RecoveryPasswordPageLocators.BUTTON_SHOW_PASSWORD)
        current_url = self.get_current_url()
        return current_url

    def wait_title_recovery_password_page(self):
        self.wait_visibility_element(RecoveryPasswordPageLocators.TITLE_RECOVERY_PASSWORD)

    def click_to_button_show_password(self):
        self.click_to_element(RecoveryPasswordPageLocators.BUTTON_SHOW_PASSWORD)

    def get_attribute_active_class_input(self):
        active_class_input = self.get_attribute_by_class(RecoveryPasswordPageLocators.INPUT_NEW_PASSWORD)
        return active_class_input
