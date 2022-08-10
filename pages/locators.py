from selenium.webdriver.common.by import By

class TestPageLocators():
    OPTION_NUMBER = (By.CSS_SELECTOR, ".par-options.clearfix >li")
    OPTION_NUMBER_PLACEHOLDER = (By.CSS_SELECTOR, "#range-value-input")


def NUMBER_BUTTON_ACTIVATE(option):
    return (By.CSS_SELECTOR, '.par-options.clearfix > li[data-value="'+ option + '"] >button')