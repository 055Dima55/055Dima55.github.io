import pytest
from HW_Kramarev_demoqa_com.CheckBoxPage import CheckboxPage


@pytest.mark.usefixtures("chrome_class")
class TestCheckboxPage:
    def setup(self):
        self.page = CheckboxPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.expand_folder("home")
        self.page.expand_folder_documents("documents")
        self.page.mark_folder("desktop")
        self.page.mark_folder("office")
        self.page.collapse_folder("documents")
        self.page.collapse_folder("home")
