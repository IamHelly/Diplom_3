from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from data_user import DataUser
import allure


class LoginPage(BasePage):
    @allure.step('Заполнение поля "Email" данными зарегистрированного пользователя')
    def send_email(self):
        self.send_data(BasePageLocators.INPUT_EMAIL, DataUser.LOGIN_USER)

    @allure.step('Заполнение поля "Пароль" данными зарегистрированного пользователя')
    def send_password(self):
        self.send_data(BasePageLocators.INPUT_PASSWORD, DataUser.PASSWORD_USER)

    @allure.step('Клик по кнопке "Войти"')
    def click_to_button_login(self):
        self.click_to_element(BasePageLocators.BUTTON_LOGIN)

    @allure.step('Ожидание видимости заголовка раздела "Конструктор"')
    def wait_title_constructor_page(self):
        self.wait_visibility_element(BasePageLocators.TITLE_CONSTRUCTOR)
