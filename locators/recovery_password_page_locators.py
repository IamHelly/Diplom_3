from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:
    LINK_FORGOT_PASSWORD = (By.XPATH, './/a[contains(text(), "Восстановить пароль")]')  # ссылка перехода на страницу восстановление пароля
    TITLE_RECOVERY_PASSWORD = (By.XPATH, './/h2[contains(text(), "Восстановление пароля")]')  # заголовок страницы "Восстановление пароля"
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, './/button[contains(text(), "Восстановить")]') # кнопка для перехода на страницу создания нового пароля
    BUTTON_SHOW_PASSWORD = (By.XPATH, './/div[@class="input__icon input__icon-action"]/*')  # кнопка показать/скрыть пароля
    INPUT_NEW_PASSWORD = (By.XPATH, './/label[contains(text(), "Пароль")]/parent::div')  # input для ввода нового пароля
