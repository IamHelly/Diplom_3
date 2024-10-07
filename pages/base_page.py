from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_visibility_element(self, locator):
        return WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_to_element(self, locator):
        return WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        return WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(locator)).text

    def get_current_url(self):
        return self.driver.current_url

    def send_data(self, locator, value):
        return WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(locator)).send_keys(value)

    def get_attribute_by_class(self, locator):
        return self.driver.find_element(*locator).get_attribute('class')

    def get_all_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_to_clickable_element(self, locator):
        return WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(locator))

    def check_open(self, value1, value2):
        if value1 in value2:
            return True
        else:
            return False

    def drag_and_drop_element(self, element_from, element_to):
        from_element = self.wait_to_clickable_element(element_from)
        to_element = self.wait_to_clickable_element(element_to)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()

    def wait_until_text_is_not(self, locator, text):
        return WebDriverWait(self.driver, 4).until(lambda driver: self.driver.find_element(*locator).text != text)

    def wait_until_locator_is_not(self, locator):
        return WebDriverWait(self.driver, 4).until(lambda driver: self.driver.find_element(*locator) is not None)
