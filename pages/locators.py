from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini * a.btn')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > .btn')

class ItemPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    BASKET_SUM = (By.CSS_SELECTOR, '.alert-info')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '.page_inner * p')
