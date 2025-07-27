from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from orangehrm_automation.utilities.logger import setup_logger


class BasePage:
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logger or setup_logger()

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.logger.info(f"Clicking on element: {locator}")
            element.click()
        except ElementClickInterceptedException:
            self.logger.info(f"Click Intercepted, attempting to scroll into view: {locator}")
            if self.scroll_element_into_view(locator):
                try:
                    element = self.wait.until(EC.element_to_be_clickable(locator))
                    self.logger.info(f"Clicking on element: {locator}")
                    element.click()
                except Exception as e:
                    self.logger.info(f"Unable to Click on element: {locator}. Error: {str(e)}")
            else:
                self.logger.info(f"Failed to scroll element into view: {locator}")
                raise
        except Exception as e:
            self.logger.info(f"Unable to Click on element: {locator}. Error: {str(e)}")

    def send_keys(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Entering text '{text}' in element: {locator}")
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.logger.info(f"Unable to enter text '{text}' into element: {locator}. Error: {str(e)}")

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text
            self.logger.info(f"Got text '{text}' from element: {locator}")
            return text
        except Exception as e:
            self.logger.info(f"Unable to get text for element: {locator}. Error: {str(e)}")

    def visibility(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"The element '{locator}' is visible.")
        except Exception as e:
            self.logger.info(f"The element '{locator}' is not visible. Error: {str(e)}")

    def scroll_element_into_view(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            strategies = [
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                "arguments[0].scrollIntoView(true);",
                "arguments[0].scrollIntoViewIfNeeded(true);",  # Non-standard but works in many browsers
                "window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.pageYOffset - 100);"
            ]

            for strategy in strategies:
                try:
                    self.driver.execute_script(strategy, element)
                    # Verify element is in viewport
                    if element.is_displayed():
                        self.logger.info(f"Successfully scrolled to element using strategy: {strategy.split('(')[0]}")
                        return True
                except Exception:
                    continue
            self.logger.warning("All scrolling strategies failed")
            return False
        except NoSuchElementException:
            self.logger.info(f"Element not found for scrolling: {locator}")
            return False
        except Exception as e:
            self.logger.info(f"Failed to scroll to element: {locator}. Error: {str(e)}")
            return False

