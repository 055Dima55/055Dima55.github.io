import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from HW_Kramarev_demoqa_com.src_pages.page_buttons import PageButtons


@pytest.mark.usefixtures("firefox")
class TestButtons:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageButtons(driver=self.driver)

    def test_doubleclick_button(self):
        self.page.open()
        self.page.button_doubleclick().doubleclick()
        assert self.page.get_button_doubleclick_message() == 'You have done a double click'

    def test_right_click_button(self):
        self.page.open()
        self.page.button_right_clik().right_click()
        assert self.page.get_button_right_click_message() == 'You have done a right click'

    def test_dynamic_id_click_button(self):
        self.page.open()
        self.page.button_clik_me().click()
        assert self.page.get_button_dynamic_id_click_message() == 'You have done a dynamic click'
