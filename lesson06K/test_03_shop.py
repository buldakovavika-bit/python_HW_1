import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSauceDemoShop(unittest.TestCase):
    """Автотест для проверки итоговой стоимости корзины"""

    def setUp(self):
        # """Настройка перед тестом: открытие браузера Firefox"""
        options = Options()
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_total_price(self):
        # """Основной тест: авторизация, добавление товаров, проверка суммы"""
        self.driver.get("https://www.saucedemo.com/")

        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        backpack_btn = self.wait.until(
            EC.element_to_be_clickable((
                By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        backpack_btn.click()

        tshirt_btn = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_btn.click()

        onesie_btn = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_btn.click()

        cart_icon = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()

        first_name = self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name.send_keys("Виктория")

        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys("Полевая")

        postal_code = self.driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("613200")

        continue_btn = self.driver.find_element(By.ID, "continue")
        continue_btn.click()

        total_element = self.wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        print(f"Итоговая стоимость: {total_text}")

        # Проверка, что итоговая сумма равна $58.29
        self.assertEqual(total_text, "Total: $58.29",
                         f"Ожидалось 'Total: $58.29', получено '{total_text}'")

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
