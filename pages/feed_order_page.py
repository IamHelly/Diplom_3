from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.feed_order_page_locators import FeedOrderPageLocators


class FeedOrderPage(BasePage):
    def wait_title_order_feed_page(self):
        self.wait_visibility_element(BasePageLocators.TITLE_ORDER_FEED)

    def click_to_card_order(self):
        self.click_to_element(FeedOrderPageLocators.CARD_ORDER)

    def get_attribute_by_class_opening_modal_window(self):
        class_open = self.get_attribute_by_class(FeedOrderPageLocators.SECTION_MODAL_WINDOW_ORDER)
        check_open = self.check_open('Modal_modal_opened__3ISw4', class_open)
        return check_open

    def drag_and_drop_ingredient_into_basket(self):
        self.drag_and_drop_element(BasePageLocators.CARD_INGREDIENT, BasePageLocators.BASKET)

    def click_to_create_order_button(self):
        self.click_to_element(BasePageLocators.BUTTON_CREATE_ORDER)

    def wait_id_completed_order(self):
        self.wait_until_text_is_not(FeedOrderPageLocators.NUMBER_ORDER, '9999')

    def click_to_close_opened_window_completed_order(self):
        self.click_to_element(BasePageLocators.CLOSE_MODAL_WINDOW)

    def click_to_link_account(self):
        self.click_to_element(BasePageLocators.LINK_ACCOUNT)

    def click_to_link_order_history(self):
        self.click_to_element(BasePageLocators.LINK_ORDER_HISTORY)

    def get_expected_number_order_in_history(self):
        number = self.get_text(FeedOrderPageLocators.NUMBER_ORDER_IN_HISTORY)
        return number

    def click_to_link_feed_orders_page(self):
        self.click_to_element(BasePageLocators.LINK_ORDER_FEED)

    def get_all_number_of_orders(self):
        orders = []
        numbers = self.get_all_elements(FeedOrderPageLocators.NUMBERS_ORDER)
        for value in numbers:
            orders.append(value.text)
        return orders

    def check_number_of_order_on_feed_page(self, orders, number):
        for item in orders:
            if item == number:
                return True
            else:
                break

    def get_expected_number_order(self):
        expected_number = self.get_text(FeedOrderPageLocators.NUMBER_ORDER)
        return expected_number

    def wait_until_locator_is_not_none(self):
        self.wait_until_locator_is_not(FeedOrderPageLocators.LI_NUMBER_ORDERS)

    def get_actual_number_order(self):
        actual_number = self.get_text(FeedOrderPageLocators.LI_NUMBER_ORDERS)
        return actual_number

    def click_to_link_constructor_page(self):
        self.click_to_element(BasePageLocators.LINK_CONSTRUCTOR)

    def get_old_value_of_number_completed_orders_for_today(self):
        old = self.get_text(FeedOrderPageLocators.COMPLETE_TODAY)
        int(old)
        return old

    def get_new_value_number_completed_orders_for_today(self):
        new = self.get_text(FeedOrderPageLocators.COMPLETE_TODAY)
        int(new)
        return new

    def get_old_value_of_number_completed_orders_for_all_time(self):
        old = self.get_text(FeedOrderPageLocators.COMPLETE_ALL_TIME)
        return old

    def get_new_value_of_number_completed_orders_for_all_time(self):
        new = self.get_text(FeedOrderPageLocators.COMPLETE_ALL_TIME)
        return new
