import pytest

from .pages.item_page import ItemPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.skip
@pytest.mark.parametrize('offer_number', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_item_add_to_basket(browser, offer_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(offer_number)}'
    page = ItemPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    item_name = page.get_item_name()
    page.should_be_success_message(item_name)
    page.should_be_basket_sum_info()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
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