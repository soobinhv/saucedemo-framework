from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Locators
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    # Actions
    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def fill_information(self, firstname, lastname, zip_code):
        self.enter_text(self.FIRST_NAME_INPUT, firstname)
        self.enter_text(self.LAST_NAME_INPUT, lastname)
        self.enter_text(self.ZIP_INPUT, zip_code)
        self.click(self.CONTINUE_BTN)

    def click_finish(self):
        self.click(self.FINISH_BTN)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)