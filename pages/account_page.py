from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.account_page_locators import AccountLocators
import allure


class AccountPage(BasePage):
    @allure.step('Клик на ссылку "Личный кабинет"')
    def click_to_link_account(self):
        self.click_to_element(BasePageLocators.LINK_ACCOUNT)

    @allure.step('Получение адреса открытой страницы')
    def get_current_url_page(self):
        current_url = self.get_current_url()
        return current_url

    @allure.step('Клик на ссылку "История заказов"')
    def click_to_link_order_history(self):
        self.click_to_element(BasePageLocators.LINK_ORDER_HISTORY)

    @allure.step('Клик на ссылку "Выход"')
    def click_to_button_logout(self):
        self.click_to_element(AccountLocators.BUTTON_LOGOUT)

    @allure.step('Ожидание видимости заголовка "Вход" страницы входа в личный кабинет')
    def wait_title_login_page(self):
        self.wait_visibility_element(BasePageLocators.TITLE_LOGIN)
