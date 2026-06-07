from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()

def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10/10")

    # Ждем, пока на странице появится хотя бы одна ссылка
    links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
    )

    links = driver.find_elements(By.TAG_NAME, 'a')
    visible_links = [link for link in links if link.is_displayed()]
    assert len(visible_links) == 10, (
        f"Expected 10 visible links, but found {len(visible_links)}"
    )

    for index, link in enumerate(links, start=1):
        assert link.is_displayed(), (
            f"Ссылка №{index} не отображается"
        )

    assert "1" in links[0].text, (
        f'Текст первой ссылки "{links[0].text}" не содержит "1"'
    )

    driver.quit()


if __name__ == "__main__":
    test_multiple_elements()
