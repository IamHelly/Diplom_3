from selenium.webdriver.common.by import By


class BasePageLocators:
    INPUT_EMAIL = (By.XPATH, './/*[text()="Email"]/following-sibling::input')  # input для ввода почты
    INPUT_PASSWORD = (By.XPATH, './/*[text()="Пароль"]/following-sibling::input')  # input для ввода пароля
    BUTTON_LOGIN = (By.XPATH, './/button[contains(text(), "Войти")]')  # кнопка "Войти"
    LINK_ACCOUNT = (By.XPATH, './/p[contains(text(), "Личный Кабинет")]/parent::a')  # ссылка "Личный кабинет"
    TITLE_CONSTRUCTOR = (By.XPATH, './/h1[contains(text(), "Соберите бургер")]')  # заголовок раздела "Конструктор"
    TITLE_LOGIN = (By.XPATH, './/div[@class="Auth_login__3hAey"]/h2[contains(text(), "Вход")]')  # заголовок "Вход"
    LINK_ORDER_HISTORY = (By.XPATH, './/a[contains(text(), "История заказов")]')  # ссылка "История заказов" в личном кабинете
    TITLE_ORDER_FEED = (By.XPATH, './/h1[contains(text(), "Лента заказов")]')  # заголовок раздела "Лента заказов"
    LINK_CONSTRUCTOR = (By.XPATH, './/p[contains(text(), "Конструктор")]/parent::a')  # ссылка в хедере для перехода в раздел "Конструктор"
    LINK_ORDER_FEED = (By.XPATH, './/p[contains(text(), "Лента Заказов")]/parent::a')  # ссылка в хедере для перехода в раздел "Лента заказов"
    CARD_INGREDIENT = (By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')  # карточка с ингредиентом "Краторная булка N-200i"
    CLOSE_MODAL_WINDOW = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')  # крестик для закрытия модального окна с деталями ингредиента
    BASKET = (By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]')  # корзина заказа бургера
    BUTTON_CREATE_ORDER = (By.XPATH, './/button[contains(text(), "Оформить заказ")]')  # кнопка "Оформить заказ"
