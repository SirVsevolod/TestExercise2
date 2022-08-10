from .base_page import BasePage
from .locators import TestPageLocators, NUMBER_BUTTON_ACTIVATE
from selenium.webdriver.remote.webelement import WebElement
import allure


class TestPage(BasePage):
    @allure.feature("get_all_options_number")
    @allure.story('Получение вариантов наминала карт')
    @allure.severity("trivial")
    def get_all_options_number(self) -> list[WebElement]:
        options = self.wait_elements(TestPageLocators.OPTION_NUMBER)
        return options

    @allure.feature("get_attr_placeholder")
    @allure.story('Получение значения из input')
    @allure.severity("trivial")
    def get_attr_placeholder(self):
        element = self.wait_visible(TestPageLocators.OPTION_NUMBER_PLACEHOLDER)
        return element.get_attribute("value")

    @allure.feature("check_activate")
    @allure.story('Получение статуса кнопки')
    @allure.severity("trivial")
    def check_activate(self, option):
        element = self.wait_visible(NUMBER_BUTTON_ACTIVATE(option))
        return "active" in element.get_attribute("class")
