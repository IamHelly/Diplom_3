from urls import UrlsPage
from pages.recovery_password_page import RecoveryPasswordPage
import allure


class TestRecoveryPasswordPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('Проверка, что при клике на гиперссылку "Восстановить пароль" открывается страница "Восстановление пароля"')
    def test_click_to_recovery_password_page(self, driver):
        password_recovery_page = RecoveryPasswordPage(driver, UrlsPage.BASE_URL + UrlsPage.LOGIN_PAGE)
        password_recovery_page.open_page()
        password_recovery_page.click_to_link_recovery_password()
        password_recovery_page_title = password_recovery_page.get_text_title_recovery_password_page()
        assert password_recovery_page_title == 'Восстановление пароля'

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить"')
    @allure.description('Проверка, что доступен ввод email и кнопка "Восстановить" кликабельна')
    def test_input_email_and_click_to_button_recovery_password(self, driver):
        password_recovery_page = RecoveryPasswordPage(driver, UrlsPage.BASE_URL + UrlsPage.FORGOT_PASSWORD_PAGE)
        password_recovery_page.open_page()
        password_recovery_page.input_email()
        password_recovery_page.click_to_button_recovery_password()
        current_url = password_recovery_page.get_current_url_recovery_password_page()
        assert current_url == UrlsPage.BASE_URL + UrlsPage.RECOVERY_PASSWORD_PAGE

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Проверка, что при клике на копку показать/скрыть пароль у поля изменяется класс, отвечающий за его отображение')
    def test_click_to_active_input_email(self, driver):
        password_recovery_page = RecoveryPasswordPage(driver, UrlsPage.BASE_URL + UrlsPage.FORGOT_PASSWORD_PAGE)
        password_recovery_page.open_page()
        password_recovery_page.input_email()
        password_recovery_page.click_to_button_recovery_password()
        password_recovery_page.wait_title_recovery_password_page()
        password_recovery_page.click_to_button_show_password()
        active_class = password_recovery_page.get_attribute_active_class_input()
        assert 'input_status_active' in active_class
