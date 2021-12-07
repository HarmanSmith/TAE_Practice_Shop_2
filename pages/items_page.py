from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ItemsPage:

    def __init__(self, browser):
        self.browser = browser

    order_locator = (By.XPATH, "//select[contains(@class, 'product_sort_container')]")
    cart_locator = (By.XPATH, "//a[contains(@class, 'shopping_cart_link')]")
    # the following provide multiple elements per locator
    price_xpath = "//div[contains(@class, 'inventory_item_price')]"
    add_to_cart_xpath = "//button[contains(@class, 'btn_inventory')]"
    item_names_xpath = "//div[contains(@class, 'inventory_item_name']"

    def sort_items(self, option):
        select = Select(self.browser.find_element(*self.order_locator))
        select.select_by_visible_text(option)

    def check_items_sorted(self):
        list_of_elements = self.browser.find_elements_by_xpath(self.add_to_cart_xpath)
        for item_number in range(len(list_of_elements)):
            previous_value = 0
            if int(list_of_elements[item_number].text()) < previous_value:
                return True
            previous_value = int(list_of_elements[item_number].text())
        return False

    def add_to_cart(self, index):
        self.browser.find_element_by_xpath(self.add_to_cart_xpath)[index].click()

    def click_cart(self):
        self.browser.find_element(*self.cart_locator).click()