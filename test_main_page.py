import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.item_page import ItemPage

link = 'http://selenium1py.pythonanywhere.com/'


def test_quest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_quest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('offer_number', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_item_add_to_cart(browser, offer_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(offer_number)}'
    page = ItemPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    item_name = page.get_item_name()
    page.should_be_success_message(item_name)
    page.should_be_cart_sum_info()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
    page.add_to_cart()
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
    page.add_to_cart()
    page.should_be_disappeared_message()
