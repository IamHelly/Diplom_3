from urls import UrlsPage
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from data_user import DataUser
from selenium import webdriver
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
    login = BasePage(driver, UrlsPage.BASE_URL + UrlsPage.LOGIN_PAGE)
    login.open_page()
    login.send_data(BasePageLocators.INPUT_EMAIL, DataUser.LOGIN_USER)
    login.send_data(BasePageLocators.INPUT_PASSWORD, DataUser.PASSWORD_USER)
    login.click_to_element(BasePageLocators.BUTTON_LOGIN)
    login.wait_visibility_element(BasePageLocators.TITLE_CONSTRUCTOR)
