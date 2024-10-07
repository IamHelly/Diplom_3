from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.account_page_locators import AccountLocators


class AccountPage(BasePage):
    def click_to_link_account(self):
        self.click_to_element(BasePageLocators.LINK_ACCOUNT)

    def get_current_url_page(self):
        current_url = self.get_current_url()
        return current_url

    def click_to_link_order_history(self):
        self.click_to_element(BasePageLocators.LINK_ORDER_HISTORY)

    def click_to_button_logout(self):
        self.click_to_element(AccountLocators.BUTTON_LOGOUT)

    def wait_title_login_page(self):
        self.wait_visibility_element(BasePageLocators.TITLE_LOGIN)
