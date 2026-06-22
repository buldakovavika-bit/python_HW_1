from pages.calculator_page import CalculatorPage


def test_calculator(driver):
    calculator = CalculatorPage(driver)

    calculator.open()
    calculator.set_delay("45")

    calculator.calculate(["7", "+", "8", "="])

    calculator.wait_result("15")

    assert calculator.get_result() == "15"
