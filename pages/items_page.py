from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ItemsPage:

    def __init__(self, browser):
        self.browser = browser

    order_locator = (By.XPATH, "//select[contains(@class, 'product_sort_container')]")
    cart_locator = (By.XPATH, "//a[contains(@class, 'shopping_cart_link')]")
    price_xpath_first = "(//div[contains(@class, 'inventory_item_price')])[1]"
    # the following provide multiple elements per locator
    price_xpath = "//div[contains(@class, 'inventory_item_price')]"
    add_to_cart_xpath = "//button[contains(@class, 'btn_inventory')]"
    item_names_xpath = "//div[contains(@class, 'inventory_item_name']"

    def sort_items(self, option):
        select = Select(self.browser.find_element(*self.order_locator))
        select.select_by_visible_text(option)

    def check_page_loaded(self):
        # wait = WebDriverWait(self.browser, 10)
        # price_element = self.browser.find_element_by_xpath(self.price_xpath_first)
        # return wait.until(EC.visibility_of_element_located(price_element))
        # return wait.until(EC._element_if_visible(self.browser.find_element(price_element)))
        try:
            element = self.browser.find_element_by_xpath("//a[contains(@class, 'shopping_cart_link')]")
        except NoSuchElementException:
            return False
        return True

    def check_items_sorted_lowest(self):
        """Checks that the items are ordered with the cheapest first."""
        list_of_elements = self.browser.find_elements_by_xpath(self.price_xpath)
        test_ok = False
        def extract_value(index):
            return float(list_of_elements[index].text.lstrip('$'))
        previous_value = extract_value(0)
        for item_number in range(len(list_of_elements)):
            current_value = extract_value(item_number)
            if current_value >= previous_value:
                test_ok = True
            else:
                test_ok = False
            previous_value = current_value
        return test_ok

    def get_item_price(self, index):
        return float(self.browser.find_elements_by_xpath(self.price_xpath)[index].text.lstrip('$'))
        pass

    def add_to_cart(self, index):
        self.browser.find_elements_by_xpath(self.add_to_cart_xpath)[index].click()

    def click_cart(self):
        self.browser.find_element(*self.cart_locator).click()
