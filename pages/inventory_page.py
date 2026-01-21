from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Locators
    TITLE_LABEL = (By.CLASS_NAME, "title")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    FIRST_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    FIRST_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    # Actions
    def get_title(self):
        return self.get_text(self.TITLE_LABEL)

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def sort_products(self, sort_option_value):
        """
        Sort options: 'az', 'za', 'lohi', 'hilo'
        """
        select_element = self.find_element(self.SORT_DROPDOWN)
        select = Select(select_element)
        select.select_by_value(sort_option_value)

    def get_first_item_price(self):
        # Lấy giá trị text (vd: "$7.99") và bỏ dấu $ để so sánh số học
        price_text = self.get_text(self.FIRST_ITEM_PRICE)
        return float(price_text.replace("$", ""))