from .BasePage import BasePage
from locators import Login

class LoginPage(BasePage):

    def fill_login_form(self, customer):
        self._input(Login.email, customer._email)
        self._input(Login.password, customer._password)
        return self

    def click_login_form(self):
        self._click(Login.sign_in)

    def get_login_error_message(self):
        return self._get_element_innerText(Login.login_error_message)

    def get_login_locked_message(self):
        return self._get_element_innerText(Login.account_locked_title_message)