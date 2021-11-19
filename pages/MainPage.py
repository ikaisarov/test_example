from .BasePage import BasePage
from locators import Main


class MainPage(BasePage):

    def get_src_main_banner(self):
        return self._get_element_src(Main.main_banner_img)

    def get_innerText_main_sections_site(self, index):
        return self._get_element_innerText(Main.sections_site, index).strip()

    def get_href_main_sections_site(self, index):
        return self._get_element_href(Main.sections_site_a, index)