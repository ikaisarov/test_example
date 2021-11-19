from pages.HeaderPage import HeaderPage
from pages.SearchPage import SearchPage
from helpers.BaseAssert import *
from helpers.Messages import *

def test_correct_search_query(browser):
    query = 'Nike'

    HeaderPage(browser).enter_value_in_search(query)
    is_sub_str(SearchPage(browser).get_text_search_query(), RESULT_SEARCH)
    is_sub_str(SearchPage(browser).get_text_search_query(), query)

    for i in range(10):
        is_sub_str(SearchPage(browser).get_search_product_tile_description(i), query)


def test_incorrect_search_query(browser):
    queries = ['!@', '--', ',./']

    for query in queries:
        HeaderPage(browser).enter_value_in_search(query)
        assert SearchPage(browser).get_text_incorrect_search_query() == SEARCH_INCORRECT.upper()