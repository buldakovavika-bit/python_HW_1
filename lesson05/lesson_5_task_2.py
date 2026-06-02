from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    old_url = driver.current_url

    name_fild = driver.find_element(By.NAME, "custname")
    name_fild.send_keys("Viktoriia")

    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit order']")
    submit_button.click()

    WebDriverWait(driver, 30).until(
            lambda d: d.current_url != old_url
        )

    print("Старый URL:", old_url)
    print("Новый URL:", driver.current_url)

    assert driver.current_url != old_url

    driver.quit()


if __name__ == "__main__":
    test_form_submission()
