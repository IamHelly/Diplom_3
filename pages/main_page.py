from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_to_link_burger_constructor_page(self):
        self.click_to_element(BasePageLocators.LINK_CONSTRUCTOR)

    def get_title_burger_constructor_page(self):
        title_burger_constructor = self.get_text(BasePageLocators.TITLE_CONSTRUCTOR)
        return title_burger_constructor

    def click_to_link_order_feed_page(self):
        self.click_to_element(BasePageLocators.LINK_ORDER_FEED)

    def get_title_order_feed_page(self):
        title_order_feed = self.get_text(BasePageLocators.TITLE_ORDER_FEED)
        return title_order_feed

    def wait_title_page(self):
        self.wait_visibility_element(BasePageLocators.TITLE_CONSTRUCTOR)

    def click_to_card_ingredient(self):
        self.click_to_element(BasePageLocators.CARD_INGREDIENT)

    def get_attribute_by_class_opening_modal_window(self):
        class_open = self.get_attribute_by_class(MainPageLocators.MODAL_WINDOW)
        check_open = self.check_open('Modal_modal_opened__3ISw4', class_open)
        return check_open

    def close_modal_window_to_card_ingredient(self):
        self.click_to_element(BasePageLocators.CLOSE_MODAL_WINDOW)

    def drag_and_drop_ingredient_into_basket(self):
        self.drag_and_drop_element(BasePageLocators.CARD_INGREDIENT, BasePageLocators.BASKET)

    def get_counter_after_adding_ingredient(self):
        counter = self.get_text(MainPageLocators.COUNTER)
        return counter

    def click_to_create_order_button(self):
        self.click_to_element(BasePageLocators.BUTTON_CREATE_ORDER)

    def wait_modal_window_created_order(self):
        self.wait_visibility_element(MainPageLocators.ID_ORDER)

    def get_text_modal_window_created_order(self):
        created_order_text = self.get_text(MainPageLocators.TEXT_CREATE_ORDER)
        return created_order_text
