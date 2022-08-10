import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
    yield browser
    browser.quit()


@pytest.fixture()
def api():
    print("API test start")
    yield
    print("API test end")