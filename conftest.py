from urls import UrlsPage
from locators.base_page_locators import BasePageLocators
from data_user import DataUser
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(UrlsPage.BASE_URL + UrlsPage.LOGIN_PAGE)
    driver.find_element(*BasePageLocators.INPUT_EMAIL).send_keys(DataUser.LOGIN_USER)
    driver.find_element(*BasePageLocators.INPUT_PASSWORD).send_keys(DataUser.PASSWORD_USER)
    driver.find_element(*BasePageLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located(BasePageLocators.TITLE_CONSTRUCTOR))
