from user import StandardUser
from pages.login_page import LoginPage
from pages.items_page import ItemsPage


def test_login_successful(browser):
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
    # Then the item list page loads
    assert items_page.check_page_loaded()
