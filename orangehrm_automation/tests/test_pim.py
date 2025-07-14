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


def test_add_user(setup):
    set_current_test_name("test_add_user")
    logger = setup_logger()
    logger.info("Starting test_add_user")
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    pim_page = PimPage(driver)
    pim_page.add_user("Victor", "Van", "Doom")
    assert "viewpersonaldetails" in driver.current_url.lower()
    logger.info("test_add_user completed successfully")


def test_edit_user(setup):
    set_current_test_name("test_edit_user")
    logger = setup_logger()
    logger.info("Starting test_edit_user")
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    pim_page = PimPage(driver)
    pim_page.edit_employee("Victor Van")
    pim_page.edit_personal_details("Vincent", "Van", "Doom","7",
                                   "Oct", "2020", "7", "Oct", "1999")
    logger.info("test_edit_user completed successfully")


