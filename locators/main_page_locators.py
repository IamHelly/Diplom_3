from selenium.webdriver.common.by import By


class MainPageLocators:
    MODAL_WINDOW = (By.XPATH, './/div[@class="Modal_modal__container__Wo2l_"]/parent::section')  # модальное окно с деталями ингредиента
    COUNTER = (By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]/p')  # каунтер
    ID_ORDER = (By.XPATH, './/p[contains(text(), "идентификатор заказа")]')  # модальное окно с ID заказа
    TEXT_CREATE_ORDER = (By.XPATH, './/p[@class="undefined text text_type_main-small mb-2"]')  # текст "Ваш заказ начали готовить" в модальном окне заказа
