import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

# Test Data (Nên lấy từ Config nhưng để đây cho gọn)
FIRST_NAME = "Harry"
LAST_NAME = "Potter"
ZIP_CODE = "12345"


@pytest.mark.usefixtures("driver")
class TestE2E:

    @pytest.fixture(autouse=True)
    def setup(self, driver, app_config):
        """Pre-condition: Luôn phải login trước khi test E2E"""
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.checkout_page = CheckoutPage(driver)

        # Login flow reused
        url = app_config['app_info']['base_url']
        user = app_config['users']['standard_user']
        pwd = app_config['users']['password']

        self.login_page.open_url(url)
        self.login_page.login(user, pwd)

    def test_sort_products_low_to_high(self):
        """TC03: Verify sorting functionality (Price: Low to High)"""
        # Act: Sort by Price (low to high)
        self.inventory_page.sort_products("lohi")

        # Assert: Check if first item price is the lowest (Sauce Labs Onesie - $7.99)
        lowest_price = self.inventory_page.get_first_item_price()
        assert lowest_price == 7.99, f"Sorting failed! Expected 7.99 but got {lowest_price}"

    def test_end_to_end_checkout(self):
        """TC04: Verify successful purchase flow"""
        # 1. Add item to cart
        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.go_to_cart()

        # 2. Start Checkout
        self.checkout_page.click_checkout()

        # 3. Fill Info
        self.checkout_page.fill_information(FIRST_NAME, LAST_NAME, ZIP_CODE)

        # 4. Finish
        self.checkout_page.click_finish()

        # 5. Assert Success Message
        expected_msg = "Thank you for your order!"
        actual_msg = self.checkout_page.get_complete_message()
        assert actual_msg == expected_msg, "Checkout failed or message changed!"