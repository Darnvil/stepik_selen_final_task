from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ItemPageLocators.ADD_TO_CART).click()

    def should_be_success_message(self, item_name):
        assert item_name in \
               self.browser.find_element(*ItemPageLocators.ADDED_TO_CART_MESSAGE).text, 'There is no element with info of adding book to cart'

    def should_be_cart_sum_info(self):
        assert self.is_element_present(*ItemPageLocators.CART_SUM), 'There is no element with cart sum'

    def get_item_name(self):
        return self.browser.find_element(*ItemPageLocators.ITEM_NAME).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.ADDED_TO_CART_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ItemPageLocators.ADDED_TO_CART_MESSAGE), 'Message does not disappears'

