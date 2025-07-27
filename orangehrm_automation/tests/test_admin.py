import pytest
from orangehrm_automation.pages.admin_page import AdminPage
from orangehrm_automation.pages.login_page import LoginPage
from orangehrm_automation.pages.pim_page import PimPage
from orangehrm_automation.utilities.webdriver_factory import get_driver
from orangehrm_automation.utilities.logger import setup_logger


@pytest.fixture(scope='function')
def setup():
    driver = get_driver()
    yield driver
    driver.quit()


def test_add_user(setup):
    logger = setup_logger()
    logger.info("Starting test_add_user")
    driver = setup
    try:
        login_page = LoginPage(driver, logger)
        pim_page = PimPage(driver, logger)
        admin_page = AdminPage(driver, logger)
        login_page.login("Admin", "admin123")
        pim_page.add_employee("Peter", "Ben", "Parker")
        admin_page.add_user("Peter Ben Parker", "ESS", "Enabled", "Spiderman",
                            "spiderman@1", "spiderman@1")
        logger.info("test_add_user completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise
