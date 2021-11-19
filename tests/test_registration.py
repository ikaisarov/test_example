from pages.RegistrationPage import RegistrationPage
from pages.MyAccountPage import MyAccountPage
from pages.HeaderPage import HeaderPage
from helpers.Customer import Customer
from helpers.Messages import *

def test_empty_fields_in_registration(browser):

    HeaderPage(browser) \
        .open_registration_page()\
        .click_submit_registration()

    assert RegistrationPage(browser).get_text_empty_error_registration() == [EMPTY_EMAIL_ERROR, EMPTY_FIRSTNAME_ERROR, EMPTY_LASTNAME_ERROR,
                                                                       EMPTY_PASSWORD_ERROR, EMPTY_BIRTHYEAR_ERROR]

def test_incorrect_data_in_registration(browser):

    HeaderPage(browser) \
        .open_registration_page()\
        .fill_email('qwerty')\
        .fill_password('qwerty')\
        .click_submit_registration()

    assert RegistrationPage(browser).get_email_error_text() == EMAIL_ERROR
    assert RegistrationPage(browser).get_password_error_text() == PASSWORD_ERROR

def test_successful_registration(browser):
    customer = Customer()

    HeaderPage(browser)\
        .open_registration_page()\
        .fill_registration_form(customer)\
        .click_login_form()
    MyAccountPage(browser).check_for_existence_button_logout()