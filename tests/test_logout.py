from user import StandardUser
from pages.login_page import LoginPage
from pages.items_page import ItemsPage


def test_shopping_cart(browser):
    # Background: username and password required
    # Given username and password
    user = StandardUser()
    # And login into the website

    # Scenario: User should be able to log out of the site

    # Given the website is displayed
    login_page = LoginPage(browser)
    login_page.load()
    assert login_page.check_login_button()
    # When the user logs in
    login_page.login(user.get_username_standard(), user.get_password())
    # Then the item list page loads
    items_page = ItemsPage(browser)
    # When the user clicks log out

    # Then the user is logged out
    # todo assert the user is logged out
    pass
