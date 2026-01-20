from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        """Wrapper tìm element với Explicit Wait"""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Wrapper click an toàn"""
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """Wrapper nhập liệu an toàn"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Lấy text của element"""
        element = self.find_element(locator)
        return element.text