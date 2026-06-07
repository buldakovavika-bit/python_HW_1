from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_navigation_to_html_forms():
    driver = webdriver.Chrome()

    print("Открываем главную страницу")
    driver.get("https://httpbin.org/")
    initial_url = driver.current_url
    time.sleep(2)

    print("Ищем ссылку HTML form")
    link = driver.find_element(By.LINK_TEXT, "HTML form")

    print("Кликаем по ссылке")
    link.click()
    time.sleep(2)

    print("URL после клика:", driver.current_url)
    assert "/forms/post" in driver.current_url

    print("Возвращаемся назад")
    driver.back()
    time.sleep(2)

    print("URL после возврата:", driver.current_url)
    assert driver.current_url == initial_url

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    test_navigation_to_html_forms()
