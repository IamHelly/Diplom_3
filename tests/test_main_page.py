from urls import UrlsPage
from pages.main_page import MainPage
import allure


class TestMainPage:
    @allure.title('Проверка перехода по клику на "Конструктор"')
    @allure.description('Проверка, что при клике на ссылку "Конструктор" открывается страница "Соберите бургер"')
    def test_click_to_burger_constructor(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL + UrlsPage.FEED_PAGE)
        main_page.open_page()
        main_page.click_to_link_burger_constructor_page()
        main_page_title = main_page.get_title_burger_constructor_page()
        assert main_page_title == 'Соберите бургер'

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    @allure.description('Проверка, что при клике на ссылку "Лента заказов" открывается страница "Лента заказов"')
    def test_click_to_section_ribbon_of_orders(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.click_to_link_order_feed_page()
        main_page_title = main_page.get_title_order_feed_page()
        assert main_page_title == 'Лента заказов'

    @allure.title('Проверка появления всплывающего окна с деталями, если кликнуть на ингредиент')
    @allure.description('Проверка, что в конструкторе при клике на ингредиент открывается всплывающее окно с деталями ингредиента')
    def test_open_modal_window_card_ingredient(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.wait_title_page()
        main_page.click_to_card_ingredient()
        check_for_modal_window = main_page.get_attribute_by_class_opening_modal_window()
        assert check_for_modal_window is True

    @allure.title('Проверка, что всплывающее окно закрывается кликом по крестику')
    @allure.description('Проверка, что при клике на иконку крестика закрывается окно с информацией')
    def test_close_modal_window_card_ingredient_by_click_on_cross_button(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.wait_title_page()
        main_page.click_to_card_ingredient()
        main_page.close_modal_window_to_card_ingredient()
        check_for_modal_window = main_page.get_attribute_by_class_opening_modal_window()
        assert check_for_modal_window is False

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении его в заказ')
    @allure.description('Проверка, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_increase_counter_when_add_ingredient_in_order(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.wait_title_page()
        main_page.drag_and_drop_ingredient_into_basket()
        counter = main_page.get_counter_after_adding_ingredient()
        assert counter != '0'

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    @allure.description('Проверка, что пользователь может авторизоваться и оформить заказ')
    def test_create_order_by_authorized_user(self, driver, login):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.drag_and_drop_ingredient_into_basket()
        main_page.click_to_create_order_button()
        main_page.wait_modal_window_created_order()
        modal_window_created_order_text = main_page.get_text_modal_window_created_order()
        assert modal_window_created_order_text == 'Ваш заказ начали готовить'
