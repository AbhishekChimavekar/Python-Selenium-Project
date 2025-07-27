import logging
import os
import inspect
from pathlib import Path

_logger_registry = {}


def get_test_script_name():
    """Safely extracts the test script name"""
    try:
        # Get the frame of the test function
        stack = inspect.stack()
        for frame in stack:
            if frame.function.startswith('test_'):
                return Path(frame.filename).name  # Returns just the filename (test_admin.py)
        # Fallback for cases where test detection fails
        return "pytest_run"
    except Exception:
        return "pytest_run"


def setup_logger(test_name=None):
    """Configures a logger with test-specific file output"""
    try:
        script_name = get_test_script_name()
        script_base = Path(script_name).stem  # test_admin.py → test_admin

        # Use explicit test name if provided, otherwise try to detect
        if not test_name:
            stack = inspect.stack()
            for frame in stack:
                if frame.function.startswith('test_'):
                    test_name = frame.function
                    break

        # Default names if detection fails
        test_name = test_name or "test_case"
        logger_name = f"orangehrm.{script_base}.{test_name}"

        if logger_name in _logger_registry:
            return logging.getLogger(logger_name)

        # Create log directory: orangehrm_automation/logs/test_admin/
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logs_dir = os.path.join(project_root, "logs", script_base)
        os.makedirs(logs_dir, exist_ok=True)

        # Log file path: orangehrm_automation/logs/test_admin/test_add_user.log
        log_file = os.path.join(logs_dir, f"{test_name}.log")

        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        logger.handlers = []

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # File handler (overwrite mode)
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        _logger_registry[logger_name] = True
        logger.info(f"Logger initialized for {test_name}")
        return logger

    except Exception as e:
        print(f"Failed to configure logger: {str(e)}")
        # Fallback to basic logger
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger("orangehrm_fallback")
