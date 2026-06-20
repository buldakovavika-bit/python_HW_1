from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = driver.wait

    def add_products(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK)
        ).click()

        self.driver.find_element(*self.TSHIRT).click()
        self.driver.find_element(*self.ONESIE).click()

    def open_cart(self):
        self.driver.find_element(*self.CART).click()
