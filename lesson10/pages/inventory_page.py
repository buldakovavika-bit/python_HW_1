"""Page Object страницы каталога SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import allure


class InventoryPage:
    """Предоставляет методы добавления товаров и перехода в корзину."""

    PRODUCT_BUTTONS = {
        "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
    }

    def __init__(self, driver: WebDriver) -> None:
        """Инициализировать Page Object.

        :param driver: Активный экземпляр Selenium WebDriver.
        :return: None.
        """
        self.driver = driver
        self.cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")

    @allure.step("Добавить товар в корзину: {product_name}")
    def add_product(self, product_name: str) -> None:
        """Добавить товар в корзину по его полному названию.

        :param product_name: Название товара из каталога.
        :return: None.
        :raises ValueError: Если товар отсутствует в поддерживаемом списке.
        """
        button_id = self.PRODUCT_BUTTONS.get(product_name)
        if button_id is None:
            raise ValueError(f"Неизвестный товар: {product_name}")
        self.driver.find_element(By.ID, button_id).click()

    @allure.step("Добавить выбранные товары в корзину")
    def add_products(self, product_names: list[str]) -> None:
        """Добавить в корзину несколько товаров.

        :param product_names: Список полных названий товаров.
        :return: None.
        """
        for product_name in product_names:
            self.add_product(product_name)

    @allure.step("Перейти в корзину")
    def open_cart(self) -> None:
        """Открыть страницу корзины.

        :return: None.
        """
        self.driver.find_element(*self.cart_link).click()
