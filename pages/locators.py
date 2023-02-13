from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ItemPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    CART_SUM = (By.CSS_SELECTOR, '.alert-info')
