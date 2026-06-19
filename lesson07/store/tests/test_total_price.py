import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from store.pages.login_page import LoginPage
from store.pages.products_page import ProductsPage
from store.pages.cart_page import CartPage
from store.pages.checkout_page import CheckoutPage


class TestSauceDemoShop(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_total_price(self):

        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        products_page.add_products()
        products_page.open_cart()

        cart_page.checkout()

        checkout_page.fill_customer_info(
            "Виктория",
            "Полевая",
            "613200"
        )

        total_text = checkout_page.get_total()

        self.assertEqual(
            total_text,
            "Total: $58.29",
            f"Ожидалось 'Total: $58.29', получено '{total_text}'"
        )


if __name__ == "__main__":
    unittest.main()
