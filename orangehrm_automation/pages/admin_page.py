from orangehrm_automation.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AdminPage(BasePage):

    ADMIN_TAB = (By.XPATH, "//span[normalize-space()='Admin']")
    # Add User Locator
    ADD_USER_BUTTON = (By.XPATH, "//i[@class='oxd-icon bi-chevron-left']")
    ADD_USER_TITLE = (By.XPATH, "//h6[normalize-space()='Add User']")
    USER_ROLE_DROPDOWN = (By.XPATH, "//label[contains(text(),'User Role')]/../../..//div[@class='oxd-select-text-input']")
    USER_ADMIN_ROLE = (By.XPATH, "//div[@role='option']/span[normalize-space()='Admin']")
    USER_ESS_ROLE = (By.XPATH, "//div[@role='option']/span[normalize-space()='ESS']")
    STATUS_DROPDOWN = (By.XPATH, "//label[contains(text(),'Status')]/../../..//div[@class='oxd-select-text-input']")
    STATUS_ENABLED = (By.XPATH, "//div[@role='option']/span[normalize-space()='Enabled']")
    STATUS_DISABLED = (By.XPATH, "//div[@role='option']/span[normalize-space()='Disabled']")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Password']/../../..//input[@type='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//label[text()='Confirm Password']/../../..//input[@type='password']")
    USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/../../..//input")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/../../..//input")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")

    def click_admin_tab(self):
        self.click(self.ADMIN_TAB)

    def click_add_user_button(self):
        self.click(self.ADD_USER_BUTTON)

    def user_role_dropdown(self):
        self.click(self.USER_ROLE_DROPDOWN)

    def click_user_role_option(self, role):
        role = role.lower()
        if role == 'admin':
            self.click(self.USER_ADMIN_ROLE)
        elif role == 'ess':
            self.click(self.USER_ESS_ROLE)
        else:
            raise ValueError("User Role must be either 'Admin' or 'ESS'")

    def click_status_option(self, status):
        status = status.lower()
        if status == 'enabled':
            self.click(self.STATUS_ENABLED)
        elif status == 'disabled':
            self.click(self.STATUS_DISABLED)
        else:
            raise ValueError("Status must be either 'Enabled' or 'Disabled'")

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def enter_confirm_password(self, confirm_password):
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, confirm_password)

    def enter_employee_name(self, employee_name):
        self.send_keys(self.EMPLOYEE_NAME_INPUT, employee_name)

    def enter_username(self, username):
        self.send_keys(self.USERNAME_INPUT, username)

    def click_save(self):
        self.click(self.SAVE_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)



