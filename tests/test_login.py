import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:

    def test_login_success(self, driver, app_config):
        """TC01: Verify login successful"""
        # Lấy data từ config
        url = app_config['app_info']['base_url']
        user = app_config['users']['standard_user']
        pwd = app_config['users']['password']

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open_url(url)
        login_page.login(user, pwd)

        assert inventory_page.get_title() == "Products"