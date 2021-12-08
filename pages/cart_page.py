from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    price_locator = (By.XPATH, "//div[contains(@class, 'inventory_item_price')]")
    checkout_locator = (By.ID, "checkout")

    def __init__(self, browser):
        self.browser = browser

    def check_price(self, price):
        same_price = False
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.price_locator))
        if price == float((element.text).lstrip('$')):
            same_price = True
        else:
            same_price = False
        return same_price

    def click_checkout(self):
        pass