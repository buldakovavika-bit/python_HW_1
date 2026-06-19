from selenium.webdriver.common.by import By
from store.base_page import BasePage


class ProductsPage(BasePage):

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def add_products(self):
        self.click(self.BACKPACK)
        self.click(self.TSHIRT)
        self.click(self.ONESIE)

    def open_cart(self):
        self.click(self.CART)
