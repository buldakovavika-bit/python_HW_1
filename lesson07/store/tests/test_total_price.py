from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_total_price(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )

    products_page.add_products()
    products_page.open_cart()

    cart_page.checkout()

    checkout_page.fill_user_data(
        first_name="Виктория",
        last_name="Полевая",
        postal_code="613200"
    )

    total_price = checkout_page.get_total_price()

    assert total_price == "Total: $58.29", (
        f"Ожидалось 'Total: $58.29', получено '{total_price}'"
    )
