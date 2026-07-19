"""Page Object страниц оформления заказа SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import allure


class CheckoutPage:
    """Предоставляет методы заполнения данных и чтения итоговой суммы."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализировать Page Object.

        :param driver: Активный экземпляр Selenium WebDriver.
        :return: None.
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CSS_SELECTOR, ".summary_total_label")

    @allure.step("Заполнить данные покупателя: {first_name} {last_name}")
    def fill_customer_data(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> None:
        """Заполнить имя, фамилию и почтовый индекс покупателя.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс покупателя.
        :return: None.
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(
            postal_code)

    @allure.step("Продолжить оформление заказа")
    def click_continue(self) -> None:
        """Перейти на страницу обзора заказа.

        :return: None.
        """
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить итоговую стоимость заказа")
    def get_total(self) -> str:
        """Прочитать итоговую стоимость и вернуть только денежное значение.

        :return: Итоговая сумма в формате ``$58.29``.
        """
        total_text = self.driver.find_element(*self.total_label).text
        return total_text.replace("Total: ", "")
