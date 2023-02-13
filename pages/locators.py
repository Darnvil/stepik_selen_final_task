from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini * a.btn')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ItemPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    BASKET_SUM = (By.CSS_SELECTOR, '.alert-info')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '.page_inner * p')
