from selenium.webdriver.common.by import By


class FeedOrderPageLocators:
    NUMBERS_ORDER = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"]//p[@class="text text_type_digits-default"]')  # номера заказов в ленте
    CARD_ORDER = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"]/child::a')  # карточка заказа из списка
    SECTION_MODAL_WINDOW_ORDER = (By.XPATH, './/section[2]')  # модальное окно заказа
    NUMBER_ORDER = (By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]/h2')  # номер заказа в модальном окне заказа
    LI_NUMBER_ORDERS = (By.XPATH, './/li[@class="text text_type_digits-default mb-2"]')  # номер заказа в списке готовых
    NUMBER_ORDER_IN_HISTORY = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"][last()]//p[@class="text text_type_digits-default"]')  # номер заказа в "Истории заказов"
    COMPLETE_TODAY = (By.XPATH, './/p[contains(text(), "Выполнено за сегодня")]/following-sibling::p')  # количество заказов, выполненных за сегодня
    COMPLETE_ALL_TIME = (By.XPATH, './/p[contains(text(), "Выполнено за все время")]/following-sibling::p')  # количество заказов, выполненных за все время
