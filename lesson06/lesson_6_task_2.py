from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 40, 0.1)
driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

element.send_keys("SkyPro")

updating_button = driver.find_element(
    By.CSS_SELECTOR, "#updatingButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(content)
