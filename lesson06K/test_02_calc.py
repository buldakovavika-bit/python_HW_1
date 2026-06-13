import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    buttons = ["7", "+", "8", "="]
    for button in buttons:
        xpath = f"//span[text()='{button}']"
        driver.find_element(By.XPATH, xpath).click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    actual_result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert actual_result == "15"


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
