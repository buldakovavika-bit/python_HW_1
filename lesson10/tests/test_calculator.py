"""Автотест медленного калькулятора."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.calculator_page import CalculatorPage


@allure.title("Сложение чисел в медленном калькуляторе")
@allure.description(
    "Проверка вычисления 7 + 8 при установленной задержке 45 секунд."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(chrome_driver: WebDriver) -> None:
    """Проверить, что калькулятор отображает результат 15."""
    calculator = CalculatorPage(chrome_driver)

    calculator.open()
    calculator.set_delay(45)
    calculator.enter_expression(["7", "+", "8", "="])
    actual_result = calculator.wait_for_result("15", timeout=50)

    with allure.step("Проверить, что результат вычисления равен 15"):
        assert actual_result == "15", (
            f"Ожидался результат '15', получен '{actual_result}'"
        )
