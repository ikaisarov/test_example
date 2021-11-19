from .BasePage import BasePage
from locators.Search import Search

class SearchPage(BasePage):

    def get_text_search_query(self):
        return self._get_element_innerText(Search.search_term, 0) + ' ' + self._get_element_innerText(Search.search_term, 1)

    def get_search_product_tile_description(self, index):
        return self._get_element_innerText(Search.search_product_tile_description, index)

    def get_text_incorrect_search_query(self):
        return self._get_element_innerText(Search.search_incorrect)
