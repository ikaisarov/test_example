from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.driver = browser

    def __element(self, selector: dict):
        by = None
        if 'id' in selector.keys():
            selector = selector['id']
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_element(by, selector)

    def __elements(self, selector: dict, index: int):
        by = None
        if 'id' in selector.keys():
            selector = selector['id']
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)[index]

    def __get_element(self, selector, index=None):
        return self.__elements(selector, index) if (index is not None) else self.__element(selector)

    def _element_is_presented(self, selector, index=None):
        element = self.__get_element(selector, index)
        element.is_displayed() and element.is_enabled()

    def _click(self, selector, index=None):
        element = self.__get_element(selector, index)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def _input(self, selector, value, index=None):
        element = self.__get_element(selector, index)
        element.clear()
        element.send_keys(value)

    def _select(self, selector, value, index=None):
        element = self.__get_element(selector, index)
        Select(element).select_by_value(value)

    def _select_by_index(self, selector, value, index=None):
        element = self.__get_element(selector, index)
        Select(element).select_by_index(value)

    def _wait_for_visible(self, selector, index=None, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__get_element(selector, index)))

    def _get_element_innerText(self, selector, index=None):
        return self.__get_element(selector, index).get_attribute('innerText')

    def _get_element_text(self, selector, index=None):
        return self.__get_element(selector, index).text

    def _get_element_src(self, selector, index=None):
        return self.__get_element(selector, index).get_attribute("src")

    def _get_element_href(self, selector, index=None):
        return self.__get_element(selector, index).get_attribute("href")
