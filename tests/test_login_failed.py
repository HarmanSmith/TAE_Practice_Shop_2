from user import StandardUser
from pages.login_page import LoginPage


def test_login_failed(browser):
    # Background: username required
    user = StandardUser()

    # Scenario: User should not be able to login with an incorrect password

    # Given the website is displayed
    login_page = LoginPage(browser)
    login_page.load()
    assert login_page.check_login_button()
    # When the user logs in
    login_page.login(user.get_username_standard(), str(user.get_password() + "X"))
    # Then we get a Login error
    assert login_page.check_login_error()
