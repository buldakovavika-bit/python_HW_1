from selenium.webdriver.common.by import By
from store.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
