from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    prices_locator = (By.XPATH, "//div[contains(@class, 'inventory_item_price')]")
    checkout_locator = (By.ID, "checkout")
    remove_buttons_locator = (By.XPATH, "//button[contains(@class, 'btn btn_secondary btn_small cart_button')]")
    remove_buttons_string = ("//button[contains(@class, 'btn btn_secondary btn_small cart_button')]")
    item_name_xpath_string = "//div[contains(@class, 'inventory_item_name')]"

    def __init__(self, browser):
        self.browser = browser

    def check_single_price(self, price):
        '''Checks if the argument price is identical to the cart price
        This is meant for a cart which contains only one item'''
        same_price = False
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.prices_locator))
        if price == float(element.text.lstrip('$')):
            same_price = True
        else:
            same_price = False
        return same_price

    def check_price_in_list(self, price, index):
        '''Checks a single price in the cart
        This is meant for when the cart contains multiple items'''
        same_price = False
        # element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.prices_locator))
        elements = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(self.prices_locator))

        if price == float(elements[index].text.lstrip('$')):
            same_price = True
        else:
            same_price = False
        return same_price

    def check_two_prices(self, price1, price2):
        '''Checks if the prices sent through arguments are the same as the first two items in the cart'''
        test_ok = False
        price1_ok = self.check_price_in_list(price1, 0)
        price2_ok = self.check_price_in_list(price2, 1)
        if price1_ok is True & price2_ok is True:
            test_ok = True
        else:
            test_ok = False
        return test_ok

    def click_remove_item(self, index):
        elements = self.browser.find_elements_by_xpath(self.remove_buttons_string)
        elements[index].click()

    def click_checkout(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.checkout_locator)).click()

    def check_for_item_in_cart(self, partial_string):
        '''Checks the cart for an item which matches the string that was sent'''
        cart_elements = self.browser.find_elements_by_xpath(self.item_name_xpath_string)
        for element_number in range(len(cart_elements)):
            if partial_string in cart_elements[element_number].text:
                return True
            else:
                return False

    def get_item_name(self, index):
        '''returns the name of a specific item in the cart'''
        cart_elements = self.browser.find_elements_by_xpath(self.item_name_xpath_string)
        return cart_elements[index].text

    def check_for_item_removed(self, partial_string):
        '''checks the Removal of an item in the cart
        a string with part of the item name is required
        returns true if the item was NOT present'''
        cart_elements = self.browser.find_elements_by_xpath(self.item_name_xpath_string)
        for element_number in range(len(cart_elements)):
            if partial_string in cart_elements[element_number].text:
                return False
        return True