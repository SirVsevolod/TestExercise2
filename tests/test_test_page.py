from pages.test_page import TestPage
from pages.locators import TestPageLocators
from pages.api import *


def test_number_is_option(browser):
    link = 'http://HR:test@qa.digift.ru/'
    page = TestPage(browser, link)

    page.open()
    options = page.get_all_options_number()
    res = []
    res2 = []
    for option in options:
        option.click()
        res.append(page.get_attr_placeholder())
        res2.append(page.check_activate(page.get_attr_placeholder()))
    assert res == ['500', '1000', '2000', '3000', '5000', '10000'] and all(res2), f'EROOR {res}, {res2}'


def test_api(api):
    res = check_name("https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name")
    assert all(res), f'EROOR: {res}'

def test_sort_check(api):
    assert check_sort("https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name"), f"ERROR {check_sort('https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name')}"