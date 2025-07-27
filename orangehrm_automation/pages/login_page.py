from selenium.webdriver.common.by import By
from orangehrm_automation.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver, logger=None):
        super().__init__(driver, logger)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'oxd-alert')]")

    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

