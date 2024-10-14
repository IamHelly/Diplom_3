from urls import UrlsPage
from pages.feed_order_page import FeedOrderPage
import allure


class TestFeedOrderPage:
    @allure.title('Проверка, что откроется всплывающее окно с деталями, если кликнуть на заказ')
    @allure.description('Проверка, что при клике по карточке заказа открывается всплывающее окно с деталями заказа')
    def test_open_modal_window_details_of_order(self, driver):
        feed_orders_page = FeedOrderPage(driver, UrlsPage.BASE_URL + UrlsPage.FEED_PAGE)
        feed_orders_page.open_page()
        feed_orders_page.wait_title_order_feed_page()
        feed_orders_page.click_to_card_order()
        check_for_modal_window = feed_orders_page.confirmation_modal_window_opening()
        assert check_for_modal_window is True

    @allure.title('Проверка отображения заказов залогиненного пользователя на странице "Лента заказов"')
    @allure.description('Проверка, что заказы пользователя из раздела "История заказов" в личном кабинете отображаются на странице "Лента заказов"')
    def test_feed_of_orders_page_has_order_user(self, driver, login):
        feed_orders_page = FeedOrderPage(driver, UrlsPage.BASE_URL)
        feed_orders_page.open_page()
        feed_orders_page.drag_and_drop_ingredient_into_basket()
        feed_orders_page.click_to_create_order_button()
        feed_orders_page.wait_id_completed_order()
        feed_orders_page.click_to_close_opened_window_completed_order()
        feed_orders_page.click_to_link_account()
        feed_orders_page.click_to_link_order_history()
        number_of_order = feed_orders_page.get_expected_number_order_in_history()
        feed_orders_page.click_to_link_feed_orders_page()
        feed_orders_page.wait_title_order_feed_page()
        number_of_orders = feed_orders_page.get_all_number_of_orders()
        result = feed_orders_page.check_number_of_order_on_feed_page(number_of_orders, number_of_order)
        assert result is True

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Проверка, что при оформлении заказа увеличивается счетчик "Выполнено за всё время" на странице "Лента заказов"')
    def test_check_number_of_completed_orders_of_all_time(self, driver, login):
        feed_orders_page = FeedOrderPage(driver, UrlsPage.BASE_URL)
        feed_orders_page.open_page()
        feed_orders_page.click_to_link_feed_orders_page()
        feed_orders_page.wait_title_order_feed_page()
        old = feed_orders_page.get_old_value_of_number_completed_orders_for_all_time()
        feed_orders_page.click_to_link_constructor_page()
        feed_orders_page.drag_and_drop_ingredient_into_basket()
        feed_orders_page.click_to_create_order_button()
        feed_orders_page.wait_id_completed_order()
        feed_orders_page.click_to_close_opened_window_completed_order()
        feed_orders_page.click_to_link_feed_orders_page()
        new = feed_orders_page.get_new_value_of_number_completed_orders_for_all_time()
        assert old < new

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Проверка, что при создании заказа увеличивается счетчик "Выполнено за сегодня" на странице "Лента заказов"')
    def test_check_number_of_completed_orders_for_today(self, driver, login):
        feed_orders_page = FeedOrderPage(driver, UrlsPage.BASE_URL)
        feed_orders_page.open_page()
        feed_orders_page.click_to_link_feed_orders_page()
        feed_orders_page.wait_title_order_feed_page()
        old = feed_orders_page.get_old_value_of_number_completed_orders_for_today()
        feed_orders_page.click_to_link_constructor_page()
        feed_orders_page.drag_and_drop_ingredient_into_basket()
        feed_orders_page.click_to_create_order_button()
        feed_orders_page.wait_id_completed_order()
        feed_orders_page.click_to_close_opened_window_completed_order()
        feed_orders_page.click_to_link_feed_orders_page()
        new = feed_orders_page.get_new_value_number_completed_orders_for_today()
        assert old < new

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    @allure.description('Проверка, что после оформления заказа его номер отображается в разделе "В работе" на странице "Лента заказов"')
    def test_check_number_order_in_work_order_list(self, driver, login):
        feed_orders_page = FeedOrderPage(driver, UrlsPage.BASE_URL)
        feed_orders_page.open_page()
        feed_orders_page.drag_and_drop_ingredient_into_basket()
        feed_orders_page.click_to_create_order_button()
        feed_orders_page.wait_id_completed_order()
        expected_number = feed_orders_page.get_expected_number_order()
        feed_orders_page.click_to_close_opened_window_completed_order()
        feed_orders_page.click_to_link_feed_orders_page()
        feed_orders_page.wait_until_locator_is_not_none()
        actual_number = feed_orders_page.get_actual_number_order()
        assert f'0{expected_number}' == actual_number
