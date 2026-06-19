from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value):
        delay = self.driver.find_element(*self.DELAY_INPUT)
        delay.clear()
        delay.send_keys(value)

    def click_button(self, button):
        xpath = f"//span[text()='{button}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def calculate(self, expression):
        """
        expression = ['7', '+', '8', '=']
        """
        for symbol in expression:
            self.click_button(symbol)

    def wait_result(self, result, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.SCREEN,
                str(result)
            )
        )

    def get_result(self):
        return self.driver.find_element(*self.SCREEN).text
