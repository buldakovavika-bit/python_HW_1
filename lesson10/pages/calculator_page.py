"""Page Object страницы медленного калькулятора."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import allure


class CalculatorPage:
    """Предоставляет методы для работы со страницей Slow Calculator."""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализировать Page Object.

        :param driver: Активный экземпляр Selenium WebDriver.
        :return: None.
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу медленного калькулятора")
    def open(self) -> None:
        """Открыть страницу калькулятора.

        :return: None.
        """
        self.driver.get(self.URL)

    @allure.step("Установить задержку вычисления: {delay} секунд")
    def set_delay(self, delay: int) -> None:
        """Очистить поле задержки и ввести новое значение.

        :param delay: Задержка вычисления в секундах.
        :return: None.
        """
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(delay))

    @allure.step("Нажать кнопку калькулятора: {button_text}")
    def click_button(self, button_text: str) -> None:
        """Нажать кнопку калькулятора по отображаемому тексту.

        :param button_text: Текст кнопки, например ``7``, ``+`` или ``=``.
        :return: None.
        """
        locator = (
            By.XPATH,
            ("//span[contains(@class, 'btn') "
             f"and normalize-space()='{button_text}']"),
        )
        self.driver.find_element(*locator).click()

    @allure.step("Выполнить последовательность нажатий: {buttons}")
    def enter_expression(self, buttons: list[str]) -> None:
        """Последовательно нажать переданные кнопки калькулятора.

        :param buttons: Список обозначений кнопок в порядке нажатия.
        :return: None.
        """
        for button in buttons:
            self.click_button(button)

    @allure.step("Дождаться результата: {expected_result}")
    def wait_for_result(self, expected_result: str, timeout: int) -> str:
        """Дождаться появления ожидаемого результата на экране.

        :param expected_result: Ожидаемый текст результата.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Текст, отображаемый на экране калькулятора.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.result_screen, expected_result)
        )
        return self.driver.find_element(*self.result_screen).text
