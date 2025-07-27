import pytest
from selenium import webdriver
from orangehrm_automation.pages.login_page import LoginPage
from orangehrm_automation.utilities.webdriver_factory import get_driver
from orangehrm_automation.utilities.logger import setup_logger


@pytest.fixture(scope="function")
def setup():
    driver = get_driver()
    yield driver
    driver.quit()


def test_successful_login(setup):
    logger = setup_logger()
    logger.info("Starting test_successful_login")
    driver = setup
    try:
        login_page = LoginPage(driver, logger)
        login_page.login("Admin", "admin123")
        assert "dashboard" in driver.current_url.lower()
        logger.info("test_successful_login completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise


def test_invalid_login(setup):
    logger = setup_logger()
    logger.info("Starting test_invalid_login")
    driver = setup
    try:
        login_page = LoginPage(driver)
        login_page.login("wrong", "credentials")
        error_message = login_page.get_error_message()
        assert "invalid" in error_message.lower()
        logger.info("test_invalid_login completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise
