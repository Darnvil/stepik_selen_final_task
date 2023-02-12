from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ItemPageLocators.ADD_TO_CART).click()

    def should_be_success_message(self):
        assert "the shellcoder's handbook" in \
               self.browser.find_element(*ItemPageLocators.ADDED_TO_CART_MESSAGE).text.lower(), 'There is no element with info of adding book to cart'

    def should_be_cart_sum_info(self):
        assert self.is_element_present(*ItemPageLocators.CART_SUM), 'There is no element with cart sum'
