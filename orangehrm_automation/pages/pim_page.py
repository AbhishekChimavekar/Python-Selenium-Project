from selenium.webdriver.common.by import By

from orangehrm_automation.pages.base_page import BasePage


class PimPage(BasePage):
    # Locator

    PIM_TAB = (By.XPATH, "//span[normalize-space()='PIM']")

    # Employee Information
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[normalize-space()='Employee Name']/../following-sibling::div//input")
    EMPLOYEE_NAME_OPTION = "//div[@role='option']/span[contains(text(),'{}')]"
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    # checkbox locator = //div[contains(text(),'Timothy')]/../following-sibling::div//i[contains(@class,'pencil')]
    EDIT_ICON = (By.XPATH, "//i[contains(@class,'pencil')]")
    DELETE_ICON = (By.XPATH, "//i[contains(@class,'trash')]")

    # Add User
    ADD_EMPLOYEE = (By.XPATH, "//li/a[normalize-space()='Add Employee']")
    FIRST_NAME = (By.NAME, "firstName")
    MIDDLE_NAME = (By.NAME, "middleName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    SUCCESSFULLY_SAVED = (By.XPATH, "//div/p[normalize-space()='Success']")

    # Enter personal details
    PERSONAL_DETAILS_TAB = (By.XPATH, "//div[@role='tab']/a[normalize-space()='Personal Details']")
    DRIVER_LICENSE_INPUT = (By.XPATH, "//label[contains(text(),'License Number')]/../..//input")
    LICENSE_EXPIRY_DATE = (By.XPATH, "//label[contains(text(),'License Expiry')]/../..//input")
    YEAR_DROPDOWN = (By.XPATH, "//li[contains(@class,'calendar-selector-year')]")
    CALENDAR_OPTION = "//li[contains(text(),'{}')]"
    DATE_OPTION = "//div[contains(@class,'date-wrapper')]/div[normalize-space()='{}']"
    MONTH_DROPDOWN = (By.XPATH, "//li[contains(@class,'calendar-selector-month')]")
    DOB_CALENDAR = (By.XPATH, "//label[contains(text(),'Birth')]/../..//input")
    NATIONALITY_DROPDOWN = (By.XPATH, "//label[contains(text(),'Nationality')]/../following-sibling::div//i")
    NATIONALITY_SELECT = (By.XPATH, "//div/span[contains(text(),'Indian')]")
    MARITAL_STATUS_DROPDOWN = (By.XPATH, "//label[contains(text(),'Marital Status')]/../following-sibling::div")
    MARITAL_STATUS_SELECT = (By.XPATH, "//div/span[contains(text(),'Single')]")
    GENDER_SELECT = (By.XPATH, "//label[normalize-space()='Male']/span")
    PERSONAL_DETAIL_SAVE = (By.XPATH, "//h6[normalize-space()='Personal Details']/..//button[normalize-space()='Save']")

    # Add User
    def click_pim_tab(self):
        self.click(self.PIM_TAB)

    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE)

    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME, first_name)

    def enter_middle_name(self, middle_name):
        self.send_keys(self.MIDDLE_NAME, middle_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME, last_name)

    def click_save_button(self):
        self.click(self.SAVE_BUTTON)

    def click_cancel_button(self):
        self.click(self.CANCEL_BUTTON)

    def successfully_saved_popup(self):
        if self.visibility(self.SUCCESSFULLY_SAVED):
            return True
        else:
            return False

    def add_user(self, first_name, middle_name, last_name):
        self.click_pim_tab()
        self.click_add_employee()
        self.enter_first_name(first_name)
        self.enter_middle_name(middle_name)
        self.enter_last_name(last_name)
        self.click_save_button()
        self.successfully_saved_popup()
        self.click_personal_details_tab()

    # Search Employee
    def enter_employee_name(self, employee_name):
        self.send_keys(self.EMPLOYEE_NAME_INPUT, employee_name)
        option_select = (By.XPATH, self.EMPLOYEE_NAME_OPTION.format(employee_name))
        self.click(option_select)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def click_employee_edit_icon(self):
        self.click(self.EDIT_ICON)

    def click_employee_delete_icon(self):
        self.click(self.DELETE_ICON)

    def edit_employee(self, employee_name):
        self.click_pim_tab()
        self.enter_employee_name(employee_name)
        self.click_search_button()
        self.click_employee_edit_icon()

    def delete_employee(self, employee_name):
        self.click_pim_tab()
        self.enter_employee_name(employee_name)
        self.click_search_button()
        self.click_employee_delete_icon()

    # Enter personal details
    def click_personal_details_tab(self):
        self.click(self.PERSONAL_DETAILS_TAB)

    def enter_license_no(self, license_no):
        self.send_keys(self.DRIVER_LICENSE_INPUT, license_no)

    def click_expiry_date_calendar(self):
        self.click(self.LICENSE_EXPIRY_DATE)

    def year_select(self, year):
        self.click(self.YEAR_DROPDOWN)
        year_select = (By.XPATH, self.CALENDAR_OPTION.format(year))
        self.click(year_select)

    def month_select(self, month):
        self.click(self.MONTH_DROPDOWN)
        month_select = (By.XPATH, self.CALENDAR_OPTION.format(month))
        self.click(month_select)

    def date_select(self, date):
        date_select = (By.XPATH, self.DATE_OPTION.format(date))
        self.click(date_select)

    def calendar_select(self, date, month, year):
        self.year_select(year)
        self.month_select(month)
        self.date_select(date)

    def click_dob_calendar(self):
        self.click(self.DOB_CALENDAR)

    def select_nationality(self):
        self.click(self.NATIONALITY_DROPDOWN)
        self.click(self.NATIONALITY_SELECT)

    def select_marital_status(self):
        self.click(self.MARITAL_STATUS_DROPDOWN)
        self.click(self.MARITAL_STATUS_SELECT)

    def select_gender(self):
        self.click(self.GENDER_SELECT)

    def personal_detail_save(self):
        self.click(self.PERSONAL_DETAIL_SAVE)

    def edit_personal_details(self, first_name, middle_name, last_name, license_date, license_month, license_year,
                              dob_date, dob_month, dob_year):
        self.click_personal_details_tab()
        self.enter_first_name(first_name)
        self.enter_middle_name(middle_name)
        self.enter_last_name(last_name)
        self.click_expiry_date_calendar()
        self.calendar_select(license_date, license_month, license_year)
        self.select_nationality()
        self.select_marital_status()
        self.click_dob_calendar()
        self.calendar_select(dob_date, dob_month, dob_year)
        self.select_gender()
        self.personal_detail_save()
        self.successfully_saved_popup()

