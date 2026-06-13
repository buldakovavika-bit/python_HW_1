import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFormValidation:
    """Автотест для проверки валидации формы"""

    @pytest.fixture
    def driver(self):
        """Фикстура для настройки и закрытия драйвера Edge"""
        # Настройка опций Edge
        edge_options = Options()
        edge_options.add_argument("--start-maximized")

        # Инициализация драйвера
        driver = webdriver.Edge(options=edge_options)
        driver.implicitly_wait(10)

        yield driver

        # Закрытие браузера после теста
        driver.quit()


def test_fill_form():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

# заполняем поля:
    driver.find_element(
        By.CSS_SELECTOR, "[name=first-name]").send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "[name=last-name]").send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "[name=address]").send_keys("Ленинаб 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "[name=e-mail]").send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "[name=phone]").send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, "[name=city]").send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "[name=country]").send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "[name=job-position]").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "[name=company]").send_keys("SkyPro")
# нажимаем кнопку:
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
# ждём отклика
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.ID, 'zip-code')))
# проверяем, что поле Zip Code подсвечивается красным
    zip_code_element = wait.until(
        EC.visibility_of_element_located((By.ID, "zip-code")))
    zip_code_color = zip_code_element.value_of_css_property("background-color")
    expected_color = "rgba(248, 215, 218, 1)"
    assert zip_code_color == expected_color  # проверка на красный цвет
    print("Поле Zip code не заполнено - подсвечивается красным")
# проверяем, что остальные поля подсвечены зелёным
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city",
              "country", "job-position", "company"]

    for field_name in fields:
        field = driver.find_element(By.ID, field_name)
        field_color = field.value_of_css_property("background-color")
        mean_color = "rgba(209, 231, 221, 1)"
    assert field_color in mean_color
    print("Заполненные поля - подсвечиваются зелёным")

    driver.quit()


if __name__ == "__main__":
    test_fill_form()
