from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step('Клик на ссылку "Конструктор"')
    def click_to_link_burger_constructor_page(self):
        self.click_to_element(BasePageLocators.LINK_CONSTRUCTOR)

    @allure.step('Получение заголовка раздела "Конструктор"')
    def get_title_burger_constructor_page(self):
        title_burger_constructor = self.get_text(BasePageLocators.TITLE_CONSTRUCTOR)
        return title_burger_constructor

    @allure.step('Клик по ссылке "Лента заказов"')
    def click_to_link_order_feed_page(self):
        self.click_to_element(BasePageLocators.LINK_ORDER_FEED)

    @allure.step('Получение заголовка раздела "Лента заказов"')
    def get_title_order_feed_page(self):
        title_order_feed = self.get_text(BasePageLocators.TITLE_ORDER_FEED)
        return title_order_feed

    @allure.step('Ожидание видимости заголовка раздела "Конструктор"')
    def wait_title_page(self):
        self.wait_visibility_element(BasePageLocators.TITLE_CONSTRUCTOR)

    @allure.step('Клик на ингредиент в списке ингредиентов')
    def click_to_card_ingredient(self):
        self.click_to_element(BasePageLocators.CARD_INGREDIENT)

    @allure.step('Получение подтверждения, что модальное окно открыто')
    def confirmation_modal_window_opening(self):
        class_open = self.get_attribute_by_class(MainPageLocators.MODAL_WINDOW)
        check_open = self.check_open('Modal_modal_opened__3ISw4', class_open)
        return check_open

    @allure.step('Клик в модальном окне по крестику закрытия окна')
    def close_modal_window_to_card_ingredient(self):
        self.click_to_element(BasePageLocators.CLOSE_MODAL_WINDOW)

    @allure.step('Перетаскивание ингредиента в корзину')
    def drag_and_drop_ingredient_into_basket(self):
        self.drag_and_drop_element(BasePageLocators.CARD_INGREDIENT, BasePageLocators.BASKET)

    @allure.step('Получение значения в счетчике ингредиента')
    def get_counter_after_adding_ingredient(self):
        counter = self.get_text(MainPageLocators.COUNTER)
        return counter

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_to_create_order_button(self):
        self.click_to_element(BasePageLocators.BUTTON_CREATE_ORDER)

    @allure.step('Ожидание видимости модального окна с номером заказа')
    def wait_modal_window_created_order(self):
        self.wait_visibility_element(MainPageLocators.ID_ORDER)

    @allure.step('Получение текста "Ваш заказ начали готовить" в модальном окне заказа')
    def get_text_modal_window_created_order(self):
        created_order_text = self.get_text(MainPageLocators.TEXT_CREATE_ORDER)
        return created_order_text
