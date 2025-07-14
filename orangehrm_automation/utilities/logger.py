import logging
import os
import inspect
from pathlib import Path
from orangehrm_automation.utilities.config import Config

# Global variable to store current test name
current_test_name = None


def set_current_test_name(test_name):
    global current_test_name
    current_test_name = test_name


def get_test_script_name():
    """Get the name of the test script being executed"""
    stack = inspect.stack()
    for frame in stack:
        frame_path = frame.filename
        if 'site-packages' in frame_path:
            continue
        if 'test_' in frame_path.lower() or '_test' in frame_path.lower():
            return os.path.basename(frame_path)
    return "global"


def setup_logger(name=None):
    """
    Configure and return a logger instance
    :param name: Optional name for the logger (for page objects)
    """
    global current_test_name

    # Use test name if available, otherwise use provided name
    logger_name = f'orangehrm_{current_test_name}' if current_test_name else f'orangehrm_{name}'

    # Get script name for directory structure
    script_name = get_test_script_name()
    script_base = Path(script_name).stem

    # Create logs directory
    logs_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        'logs',
        script_base
    ))
    os.makedirs(logs_dir, exist_ok=True)

    # Create log file path
    log_file = os.path.join(logs_dir, f"{current_test_name or name}.log")

    # Create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(Config.LOG_LEVEL)
    logger.handlers = []

    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    try:
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        logger.info(f"Logger initialized for {logger_name}")
    except Exception as e:
        print(f"Failed to create logger: {str(e)}")
        raise

    return logger
