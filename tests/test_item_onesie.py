from user import StandardUser
from pages.login_page import LoginPage
from pages.items_page import ItemsPage
from pages.cart_page import CartPage


def test_item_onesie(browser):
    # Background: username and password required
    # Given username and password
    user = StandardUser()
    # And login into the website

    # Scenario: User should be able to add onesie to the shopping cart

    # Given the website is displayed
    login_page = LoginPage(browser)
    login_page.load()
    assert login_page.check_login_button()
    # When the user logs in
    login_page.login(user.get_username_standard(), user.get_password())
    # Then the item list page loads
    items_page = ItemsPage(browser)
    # When the user adds onesie to the shopping cart

    # And clicks the cart button

    # Then the cart displays the onesie inside
    # todo asssert the onesie is in the cart