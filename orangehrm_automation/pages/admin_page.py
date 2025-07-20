from orangehrm_automation.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AdminPage(BasePage):

    ADMIN_TAB = (By.XPATH, "//span[normalize-space()='Admin']")
    ADMIN_PAGE_TITLE = (By.XPATH, "//h5[normalize-space()='System Users']")
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
    EMPLOYEE_NAME_OPTION = "//div[@role='option']/span[contains(text(),'{}')]"
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    SUCCESSFULLY_SAVED = (By.XPATH, "//div/p[normalize-space()='Success']")

    # Search User
    SEARCH_USERNAME_INPUT = (By.XPATH, "//label[normalize-space()='Username']/../following-sibling::div//input")
    SEARCH_USERNAME_OPTION = "//div[@role='option']/span[contains(text(),'{}')]"
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    # checkbox locator = //div[contains(text(),'Timothy')]/../following-sibling::div//i[contains(@class,'pencil')]
    EDIT_ICON = (By.XPATH, "//i[contains(@class,'pencil')]")
    DELETE_ICON = (By.XPATH, "//i[contains(@class,'trash')]")

    def click_admin_tab(self):
        self.click(self.ADMIN_TAB)

    def assert_admin_page(self):
        if self.visibility(self.ADMIN_PAGE_TITLE):
            return True
        else:
            return False

    def assert_add_user_page(self):
        if self.visibility(self.ADD_USER_TITLE):
            return True
        else:
            return False

    def click_add_user_button(self):
        self.click(self.ADD_USER_BUTTON)

    def click_user_role_dropdown(self):
        self.click(self.USER_ROLE_DROPDOWN)

    def click_user_role_option(self, role):
        role = role.lower()
        if role == 'admin':
            self.click(self.USER_ADMIN_ROLE)
        elif role == 'ess':
            self.click(self.USER_ESS_ROLE)
        else:
            raise ValueError("User Role must be either 'Admin' or 'ESS'")

    def click_status_dropdown(self):
        self.click(self.STATUS_DROPDOWN)

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
        option_select = (By.XPATH, self.EMPLOYEE_NAME_OPTION.format(employee_name))
        self.click(option_select)

    def enter_username(self, username):
        self.send_keys(self.USERNAME_INPUT, username)

    def click_save(self):
        self.click(self.SAVE_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)

    def successfully_saved_popup(self):
        if self.visibility(self.SUCCESSFULLY_SAVED):
            return True
        else:
            return False

    def add_user(self, employee_name, user_role, status, username, password, confirm_password):
        self.click_admin_tab()
        self.assert_admin_page()
        self.click_add_user_button()
        self.assert_add_user_page()
        self.click_user_role_dropdown()
        self.click_user_role_option(user_role)
        self.enter_employee_name(employee_name)
        self.click_status_dropdown()
        self.click_status_option(status)
        self.enter_username(username)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_save()
        self.successfully_saved_popup()

    # Search User
    def enter_search_username(self, username):
        self.send_keys(self.SEARCH_USERNAME_INPUT, username)
        option_select = (By.XPATH, self.SEARCH_USERNAME_OPTION.format(username))
        self.click(option_select)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def click_employee_edit_icon(self):
        self.click(self.EDIT_ICON)

    def click_employee_delete_icon(self):
        self.click(self.DELETE_ICON)


