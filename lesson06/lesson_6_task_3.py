from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()

waiter = WebDriverWait(driver, 20)

waiter.until(
    EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
)

images = waiter.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "#image-container img"))
)
print(f"\nSRC 3-й картинки: {images[2].get_attribute('src')}")

driver.quit()
