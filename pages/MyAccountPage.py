from .BasePage import BasePage
from locators import MyAccount

class MyAccountPage(BasePage):

    def check_for_existence_button_logout(self):
        self._element_is_presented(MyAccount.logout)