"""Page Object страницы корзины SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import allure


class CartPage:
    """Предоставляет методы проверки корзины и перехода к оформлению."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализировать Page Object.

        :param driver: Активный экземпляр Selenium WebDriver.
        :return: None.
        """
        self.driver = driver
        self.item_names = (By.CSS_SELECTOR, ".inventory_item_name")
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Получить названия товаров в корзине")
    def get_product_names(self) -> list[str]:
        """Получить список названий всех товаров в корзине.

        :return: Список названий товаров.
        """
        return [element.text for element in self.driver.find_elements(
            *self.item_names)]

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """Перейти к первому этапу оформления заказа.

        :return: None.
        """
        self.driver.find_element(*self.checkout_button).click()
