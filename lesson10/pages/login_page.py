"""Page Object страницы авторизации SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import allure


class LoginPage:
    """Предоставляет методы авторизации в интернет-магазине SauceDemo."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализировать Page Object.

        :param driver: Активный экземпляр Selenium WebDriver.
        :return: None.
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации SauceDemo")
    def open(self) -> None:
        """Открыть страницу авторизации.

        :return: None.
        """
        self.driver.get(self.URL)

    @allure.step("Ввести логин: {username}")
    def enter_username(self, username: str) -> None:
        """Ввести имя пользователя.

        :param username: Логин пользователя.
        :return: None.
        """
        self.driver.find_element(*self.username_input).send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """Ввести пароль пользователя.

        :param password: Пароль пользователя.
        :return: None.
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    @allure.step("Нажать кнопку Login")
    def click_login(self) -> None:
        """Нажать кнопку входа.

        :return: None.
        """
        self.driver.find_element(*self.login_button).click()

    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """Заполнить форму авторизации и выполнить вход.

        :param username: Логин пользователя.
        :param password: Пароль пользователя.
        :return: None.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
