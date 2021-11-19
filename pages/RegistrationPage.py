from .BasePage import BasePage
from locators import Registration


class RegistrationPage(BasePage):

    def fill_registration_form(self, customer):
        self._input(Registration.email, customer._email)
        self._input(Registration.firstname, customer._firstname)
        self._input(Registration.lastname, customer._lastname)
        self._input(Registration.password, customer._password)
        self._select(Registration.birthday, customer._birthday)
        self._select(Registration.birthmonth, customer._birthmonth)
        self._select(Registration.birthyear, customer._birthyear)

    def click_submit_registration(self):
        self._click(Registration.register_button)
        return RegistrationPage(self.driver)

    def get_text_empty_error_registration(self):
        text =  []
        text.append(self._get_element_innerText(Registration.email_error))
        text.append(self._get_element_innerText(Registration.firstname_error))
        text.append(self._get_element_innerText(Registration.lastname_error))
        text.append(self._get_element_innerText(Registration.password_error))
        text.append(self._get_element_innerText(Registration.birthyear_error))

        return text

    def fill_email(self, value):
        self._input(Registration.email, value)
        return RegistrationPage(self.driver)

    def fill_password(self, value):
        self._input(Registration.password, value)
        return RegistrationPage(self.driver)

    def get_email_error_text(self):
        return self._get_element_innerText(Registration.email_error)

    def get_password_error_text(self):
        return self._get_element_innerText(Registration.password_error)