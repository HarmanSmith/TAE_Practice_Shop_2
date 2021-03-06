from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    url = "https://www.saucedemo.com"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_locator = (By.ID, "login-button")
    error_locator = (By.XPATH, "//h3[contains(@data-test, 'error')]")
    error_xpath = "//h3[contains(@data-test, 'error')]"

    def check_login_button(self):
        """"checks for the visibility of the login button"""
        wait = WebDriverWait(self.browser, 10)
        login_button = self.browser.find_element(*self.login_locator)
        return wait.until(EC.visibility_of(login_button))

    def enter_username(self, username):
        self.browser.find_element(*self.username_locator).send_keys(username)

    def enter_password(self, password):
        self.browser.find_element(*self.password_locator).send_keys(password)

    def click_login(self):
        self.browser.find_element(*self.login_locator).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def check_login_error(self):
        """checks for the visibility of an error message
        returns true when the user was unable to login"""
        try:
            self.browser.find_element_by_xpath(self.error_xpath)
        except NoSuchElementException:
            return False
        return True
