# from behave import *
from user import StandardUser
from pages.login_page import LoginPage
from pages.items_page import ItemsPage


def test_shopping_cart(browser):
    # Background: username and password required
    # Given username and password
    user = StandardUser()
    # And login into the website

    # Scenario: User should not be able to login with an incorrect password

    # Given the website is displayed
    login_page = LoginPage(browser)
    login_page.load()
    assert login_page.check_login_button()
    # When the user logs in
    login_page.login(user.get_username_standard(), str(user.get_password() + "X"))
    # Then we get a Login error
    # todo assert login error screen
    pass
