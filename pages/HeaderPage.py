from .BasePage import BasePage
from locators import Header
from .LoginPage import LoginPage
from .RegistrationPage import RegistrationPage

class HeaderPage(BasePage):

    def open_registration_page(self):
        self._click(Header.my_account_dropdown)
        self._wait_for_visible(Header.signup)
        self._click(Header.signup)
        return RegistrationPage(self.driver)

    def open_login_page(self):
        self._click(Header.my_account_dropdown)
        self._wait_for_visible(Header.my_account)
        self._click(Header.my_account)
        return LoginPage(self.driver)

    def enter_value_in_search(self, value):
        self._click(Header.search_input)
        self._input(Header.search_input, value)
        self._click(Header.search_button)