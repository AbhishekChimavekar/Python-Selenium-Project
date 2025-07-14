import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()


class Config:
    # Time configurations
    WAIT_TIME = 10
    POLL_FREQUENCY = 0.5

    # Environment URLs
    BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/")

    # Test credentials
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "Admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

    # Browser configurations
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    BROWSER = os.getenv("BROWSER", "chrome")

    # Output configurations
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "True").lower() == "true"

    # Logging configuration
    LOG_LEVEL = logging.INFO  # Make sure this is set to INFO or DEBUG
