from urls import UrlsPage
from pages.account_page import AccountPage
import allure


class TestPersonalAccountPage:
    @allure.title('Проверка перехода по клику на "Личный кабинет"')
    @allure.description('Проверка, что при клике на ссылку "Личный кабинет" открывается страница профиля')
    def test_switch_to_account(self, driver, login):
        account_page = AccountPage(driver, UrlsPage.BASE_URL)
        account_page.open_page()
        account_page.click_to_link_account()
        current_url = account_page.get_current_url_page()
        assert current_url == UrlsPage.BASE_URL + UrlsPage.PROFILE_PAGE

    @allure.title('Проверка перехода в раздел "История заказов"')
    @allure.description('Проверка, что при клике на ссылку "История заказов" в личном кабинете открывается раздел "История заказов"')
    def test_switch_to_chapter_order_history_in_account(self, driver, login):
        account_page = AccountPage(driver, UrlsPage.BASE_URL)
        account_page.open_page()
        account_page.click_to_link_account()
        account_page.click_to_link_order_history()
        current_url = account_page.get_current_url_page()
        assert current_url == UrlsPage.BASE_URL + UrlsPage.ORDER_HISTORY_PAGE

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверка, что при клике на ссылку "Выход" идет переход в неавторизованную зону - на страницу входа в личный кабинет')
    def test_account_logout(self, driver, login):
        account_page = AccountPage(driver, UrlsPage.BASE_URL)
        account_page.open_page()
        account_page.click_to_link_account()
        account_page.click_to_button_logout()
        account_page.wait_title_login_page()
        current_url = account_page.get_current_url_page()
        assert current_url == UrlsPage.BASE_URL + UrlsPage.LOGIN_PAGE
