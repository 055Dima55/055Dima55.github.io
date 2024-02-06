import pytest
from selenium.webdriver.remote.webelement import WebElement

from HW_Kramarev_demoqa_com.ElementPage import ElementsPage


class TestElementsPage:
    def test_amount_of_elements(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33

    def test_elements_number_0(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert elements[0] == "Text Box"

    def test_elements_number_1(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert elements[1] == "Check Box"

    def test_elements_number_10(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        for i in range(10, len(elements)):
            assert elements[i] == ''

    def test_elements_number_11(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        for i in range(11, len(elements)):
            assert elements[i] == ''

# тут перевірив відразу всі 33 елементи
    def test_all_elements(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        expected_elements = ['Text Box', 'Check Box', 'Radio Button',
                             'Web Tables', 'Buttons', 'Links',
                             'Broken Links - Images', 'Upload and Download',
                             'Dynamic Properties', '', '', '', '', '', '',
                             '', '', '', '', '', '', '', '', '', '', '', '',
                             '', '', '', '', '', '']
        for i, expected_element in enumerate(expected_elements):
            assert elements[i] == expected_element

# тут перевірив відразу всі 33 елементи та ігноруючи порожні
    def test_all_elements_2(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        expected_elements = ['Text Box', 'Check Box', 'Radio Button',
                             'Web Tables', 'Buttons', 'Links',
                             'Broken Links - Images', 'Upload and Download',
                             'Dynamic Properties']
        for i, expected_element in enumerate(expected_elements):
            if expected_element == '':
                continue
            assert elements[i] == expected_element

# тут перевірив відразу всі 33, parametrize
@pytest.mark.parametrize("expected_elements", [
    'Text Box', 'Check Box', 'Radio Button',
    'Web Tables', 'Buttons', 'Links',
    'Broken Links - Images', 'Upload and Download',
    'Dynamic Properties', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', ''])
def test_all_elements_3(chrome, expected_elements):
    page = ElementsPage(chrome)
    page.open()
    elements = page.get_elements_page_categories()
    assert expected_elements in elements



    # def test_is_button_enabled(self, chrome):
    #     page = PageDynamicProperties(chrome)
    #     page.open()
    #     button: WebElement = page.disable_enable_button()
    #     button.click()
    #
    # def test_is_button_shown(self, chrome):
    #     page = PageDynamicProperties(chrome).open()  # короткий запис
    #     button: WebElement = page.button_invisible_visible()
    #     button.click()
