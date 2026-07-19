"""Автотест оформления заказа в SauceDemo."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.title("Оформление заказа из трех товаров в SauceDemo")
@allure.description(
    "Авторизация standard_user, добавление трех товаров, оформление заказа "
    "и проверка итоговой стоимости $58.29."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total(firefox_driver: WebDriver) -> None:
    """Проверить итоговую стоимость заказа из трех выбранных товаров."""
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]

    login_page = LoginPage(firefox_driver)
    inventory_page = InventoryPage(firefox_driver)
    cart_page = CartPage(firefox_driver)
    checkout_page = CheckoutPage(firefox_driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_products(products)
    inventory_page.open_cart()

    actual_products = cart_page.get_product_names()
    with allure.step("Проверить содержимое корзины"):
        assert actual_products == products, (
            f"Ожидались товары {products}, получены {actual_products}"
        )

    cart_page.click_checkout()
    checkout_page.fill_customer_data("Ivan", "Ivanov", "600000")
    checkout_page.click_continue()
    actual_total = checkout_page.get_total()

    with allure.step("Проверить, что итоговая стоимость равна $58.29"):
        assert actual_total == "$58.29", (
            f"Ожидалась сумма '$58.29', получена '{actual_total}'"
        )
