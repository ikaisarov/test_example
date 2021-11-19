from pages.MainPage import MainPage
from helpers.BaseAssert import *
from helpers.Images import *
from helpers.Messages import *


def test_main_page_content(browser):
    assert MainPage(browser).get_src_main_banner() == MAIN_BANNER_IMG
    assert MainPage(browser).get_innerText_main_sections_site(0) == WOMEN.upper()
    assert MainPage(browser).get_innerText_main_sections_site(1) == MEN.upper()
    is_sub_str(MainPage(browser).get_href_main_sections_site(0), 'women')
    is_sub_str(MainPage(browser).get_href_main_sections_site(1), 'men')
