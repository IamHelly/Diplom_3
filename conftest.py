from urls import UrlsPage
from pages.login_page import LoginPage
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
    login = LoginPage(driver, UrlsPage.BASE_URL + UrlsPage.LOGIN_PAGE)
    login.open_page()
    login.send_email()
    login.send_password()
    login.click_to_button_login()
    login.wait_title_constructor_page()
