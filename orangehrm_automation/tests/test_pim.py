import pytest
from orangehrm_automation.pages.pim_page import PimPage
from orangehrm_automation.utilities.logger import setup_logger, set_current_test_name
from orangehrm_automation.pages.login_page import LoginPage
from orangehrm_automation.utilities.webdriver_factory import get_driver


@pytest.fixture(scope="function")
def setup():
    driver = get_driver()
    yield driver
    driver.quit()


def test_add_employee(setup):
    set_current_test_name("test_add_employee")
    logger = setup_logger()
    logger.info("Starting test_add_employee")
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    pim_page = PimPage(driver)
    pim_page.add_employee("Victor", "Van", "Doom")
    assert "viewpersonaldetails" in driver.current_url.lower()
    logger.info("test_add_employee completed successfully")


def test_edit_employee(setup):
    set_current_test_name("test_edit_employee")
    logger = setup_logger()
    logger.info("Starting test_edit_employee")
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    pim_page = PimPage(driver)
    pim_page.edit_employee("Victor Van")
    pim_page.edit_personal_details("Vincent", "Van", "Doom","7",
                                   "Oct", "2020", "7", "Oct", "1999")
    logger.info("test_edit_employee completed successfully")


def test_delete_employee(setup):
    set_current_test_name("test_delete_employee")
    logger = setup_logger()
    logger.info("Starting test_delete_employee")
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    pim_page = PimPage(driver)
    pim_page.delete_employee("Victor Van")
    logger.info("test_delete_employee completed successfully")
