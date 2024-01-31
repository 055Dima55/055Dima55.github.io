from HW_18_Kramarev.TestBoxPage import TextBoxPage


def test_username_fill_and_check(chrome):
    page = TextBoxPage(chrome)
    page.open()
    page.fill_full_name_field("Dima")
    page.scroll_down()
    page.click_submit()
    name_field = page.get_result_fullname()
    assert name_field.replace("Name:", "") == "Dima"


def test_email_fill_and_check(chrome):
    page = TextBoxPage(chrome)
    page.open()
    page.fill_email_field("adres@gmail.com")
    page.scroll_down()
    page.click_submit()
    email_name = page.get_result_email()
    expected_email = "adres@gmail.com"
    assert expected_email in email_name


def test_curr_addr_fill_and_check(chrome):
    page = TextBoxPage(chrome)
    page.open()
    page.fill_current_address_field("02000, Kiev, str. Revutskogo 2")
    page.scroll_down()
    page.click_submit()
    current_address_text = page.get_result_current_address()
    assert current_address_text == "Current Address :02000, Kiev, str. Revutskogo 2"


def test_perm_addr_fill_and_check(chrome):
    page = TextBoxPage(chrome)
    page.open()
    page.fill_permanent_address_field("Kiev, str. Bagana 2/1, flat 23")
    page.scroll_down()
    page.click_submit()
    perm_address_texr = page.get_result_permanent_address()
    expected_perm_address = "Kiev, str. Bagana 2/1, flat 23"
    assert expected_perm_address in perm_address_texr
