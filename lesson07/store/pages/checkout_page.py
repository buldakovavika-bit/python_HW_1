from selenium.webdriver.common.by import By
from store.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.find(self.FIRST_NAME).send_keys(first_name)
        self.find(self.LAST_NAME).send_keys(last_name)
        self.find(self.POSTAL_CODE).send_keys(postal_code)
        self.click(self.CONTINUE)

    def get_total(self):
        return self.find(self.TOTAL).text
