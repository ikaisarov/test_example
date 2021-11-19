import allure

from pages.LoginPage import LoginPage
from pages.HeaderPage import HeaderPage
from pages.MyAccountPage import MyAccountPage
from helpers.Customer import Customer
from helpers.Messages import *


@allure.feature('Логин игрока')
@allure.story('Успешный логин')
def test_successful_login(browser):
    customer = Customer('correct_data')

    HeaderPage(browser) \
        .open_login_page() \
        .fill_login_form(customer) \
        .click_login_form()
    MyAccountPage(browser).check_for_existence_button_logout()

@allure.feature('Логин игрока')
@allure.story('Ошибка при неверном логине и пароле')
def test_unsuccessful_login(browser):
    customer = Customer()

    HeaderPage(browser) \
        .open_login_page() \
        .fill_login_form(customer) \
        .click_login_form()
    assert LoginPage(browser).get_login_error_message() == LOGIN_ERROR

@allure.feature('Логин игрока')
@allure.story('Блокировка игрока при трехкратном неверном вводе данных')
def test_locked_account_after_unsuccessful_login(browser):
    customer = Customer()

    HeaderPage(browser).open_login_page()
    for i in range(3):
        LoginPage(browser).fill_login_form(customer) \
            .click_login_form()
    assert LoginPage(browser).get_login_locked_message() == LOCKED_ERROR.upper()
