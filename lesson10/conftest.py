"""Фикстуры Selenium WebDriver для автотестов."""

from collections.abc import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def chrome_driver() -> Generator[WebDriver, None, None]:
    """Создать Chrome WebDriver и закрыть его после теста.

    :return: Генератор, передающий тесту экземпляр Chrome WebDriver.
    """
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver() -> Generator[WebDriver, None, None]:
    """Создать Firefox WebDriver и закрыть его после теста.

    :return: Генератор, передающий тесту экземпляр Firefox WebDriver.
    """
    options = FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
