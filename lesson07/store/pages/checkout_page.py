from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = driver.wait

    def fill_user_data(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)

        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_price(self):
        return self.wait.until(
            EC.presence_of_element_located(self.TOTAL_PRICE)
        ).text
