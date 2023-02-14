import time

import pytest

from .pages.item_page import ItemPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.usertest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + '@fakegmail.com', str(time.time()) + '5678')
        page.should_be_authorized_user()

    def test_user_can_add_item_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ItemPage(browser, link)
        page.open()
        page.add_to_basket()
        item_name = page.get_item_name()
        page.should_be_success_message(item_name)
        page.should_be_basket_sum_info()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ItemPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()





@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_message()


def test_guest_should_see_login_link_on_item_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_item_page(browser):
    page = ItemPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()