# from behave import *
from user import StandardUser
from pages.login_page import LoginPage
from pages.items_page import ItemsPage
from pages.cart_page import CartPage


def test_shopping_cart(browser):
    # Background: username and password required
    # Given username and password
    user = StandardUser()
    # And login into the website

    # Scenario: User should be able to sort and add items to cart

    # Given the website is displayed
    login_page = LoginPage(browser)
    login_page.load()
    assert login_page.check_login_button()
    # When the user logs in
    login_page.login(user.get_username_standard(), user.get_password())
    # Then the item list page loads
    items_page = ItemsPage(browser)
    # When the user selects order by price
    items_page.sort_items("Price (low to high)")
    # Then the items are sorted by price
    items_page.check_items_sorted()
    # When the user adds the cheapest item to the cart
    items_page.add_to_cart(0)
    # And clicks in the cart icon
    items_page.click_cart()
    # Then the cart page loads with the selected item
    cart_page = CartPage(browser)
    cart_page.check_item("item_name")

    pass
