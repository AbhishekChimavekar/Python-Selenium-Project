import pytest
from orangehrm_automation.pages.admin_page import AdminPage
from orangehrm_automation.pages.login_page import LoginPage
from orangehrm_automation.pages.pim_page import PimPage
from orangehrm_automation.utilities.webdriver_factory import get_driver
from orangehrm_automation.utilities.logger import set_current_test_name, setup_logger


@pytest.fixture(scope='function')
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
    pim_page.add_employee("Wade", "Winston", "Wilson")
    assert "viewpersonaldetails" in driver.current_url.lower()
    admin_page = AdminPage(driver)
    admin_page.add_user("Wade Winston Wilson", "ESS", "Enabled", "Deadpool",
                        "deadpool@1", "deadpool@1")
