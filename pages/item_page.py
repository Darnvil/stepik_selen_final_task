from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ItemPageLocators.ADD_TO_BASKET).click()

    def should_be_success_message(self, item_name):
        assert item_name in \
               self.browser.find_element(*ItemPageLocators.ADDED_TO_BASKET_MESSAGE).text, 'There is no element with info of adding book to basket'

    def should_be_basket_sum_info(self):
        assert self.is_element_present(*ItemPageLocators.BASKET_SUM), 'There is no element with basket sum'

    def get_item_name(self):
        return self.browser.find_element(*ItemPageLocators.ITEM_NAME).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ItemPageLocators.ADDED_TO_BASKET_MESSAGE), 'Message does not disappears'

