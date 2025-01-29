"""
Module: logger.py
======================

Custom logger for logging. Users can use this CustomLogger class to log or use python's logging module.
"""
import logging
from typing import Union
from pathlib import Path

from paystackease.src._api_errors import PayStackError


class CustomLogger:
    """
    A custom logger class that provides logging functionality with configurable file and console output.
    """
    def __init__(
        self,
        log_file_name: str = "default.log",
        log_dir_path: Union[str, Path] = None,
        log_dir_name: str = "PayStackLogs",
        logging_name: str = "logging",
        console_logging: bool = False
    ) -> None:
        """
        Initialize the CustomLogger.

        Args:
            log_file_name (str, optional): Name of the log file. Defaults to "default.log".
            log_dir_path (Union[str, Path], optional): Directory path for storing log files.
                If None, uses a default directory. Defaults to None.
            log_dir_name (str, default=PayStackLogs): Name of the directory to store log files
            logging_name (str, optional): Name for the logger. Defaults to "logging".
            console_logging (bool, optional): Whether to enable console logging. Defaults to False.

        Returns:
            None
        """
        try:
            # if no log directory is provided, use a default directory to the current path
            if log_dir_path is None:
                log_dir_path = Path(__file__).resolve().parent.parent.parent / log_dir_name
            else:
                log_dir_path = Path(log_dir_path)

            # Convert string paths to Path objects, if necessary.
            if isinstance(log_dir_path, str):
                log_dir_path = Path(log_dir_path)

            # checks if the directory exists
            if not log_dir_path.exists():
                log_dir_path.mkdir(parents=True, exist_ok=True)

            # Validate the log file name
            if not log_file_name.endswith(".log"):
                raise PayStackError("Log file name must end with '.log'")

            # construct full path to the log file
            log_file_path = log_dir_path / log_file_name

            self.logger = logging.getLogger(logging_name)
            self.logger.setLevel(logging.DEBUG)

            # Define a log format
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            # Prevent additional multiple logging handlers
            self.logger.handlers = []

            # Create a file handler and set level to debug
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            # Add handlers to the logger
            self.logger.addHandler(file_handler)

            # To log on console
            if console_logging:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.DEBUG)
                console_handler.setFormatter(formatter)
                self.logger.addHandler(console_handler)

            self.logger.info("Logger initialized successfully.")

        except (FileNotFoundError, PermissionError) as error:
            raise RuntimeError(f"Error setting up log directory or file: {error}")

        except PayStackError as error:
            raise PayStackError(f"Invalid log directory or file name: {error}")

    def _log_with_status(self, level, message, status) -> None:
        """
        Internal method to log messages with a status code.

        Args:
            level: The logging level (e.g., logging.DEBUG, logging.INFO, etc.).
            message (str): The message to be logged.
            status (int): The status code associated with the log message.

        Returns:
            None
        """
        extra = {"status": status}  # Provide 'status' as extra info for formatter
        if level == logging.DEBUG:
            self.logger.debug(message, extra=extra)
        elif level == logging.INFO:
            self.logger.info(message, extra=extra)
        elif level == logging.WARNING:
            self.logger.warning(message, extra=extra)
        elif level == logging.ERROR:
            self.logger.error(message, extra=extra)
        elif level == logging.CRITICAL:
            self.logger.critical(message, extra=extra)

    def debug(self, message: str, status: int = 100) -> None:
        """
        Log a debug message.

        Args:
            message (str): The debug message to be logged.
            status (int, optional): The status code for the debug message. Defaults to 100.

        Returns:
            None
        """
        self._log_with_status(logging.DEBUG, message, status)

    def info(self, message: str, status: int = 200) -> None:
        """
        Log an info message.

        Args:
            message (str): The info message to be logged.
            status (int, optional): The status code for the info message. Defaults to 200.

        Returns:
            None
        """
        self._log_with_status(logging.INFO, message, status)

    def warning(self, message: str, status: int = 400) -> None:
        """
        Log a warning message.

        Args:
            message (str): The warning message to be logged.
            status (int, optional): The status code for the warning message. Defaults to 400.

        Returns:
            None
        """
        self._log_with_status(logging.WARNING, message, status)

    def error(self, message: str, status: int = 401) -> None:
        """
        Log an error message.

        Args:
            message (str): The error message to be logged.
            status (int, optional): The status code for the error message. Defaults to 401.

        Returns:
            None
        """
        self._log_with_status(logging.ERROR, message, status)

    def critical(self, message: str, status: int = 500) -> None:
        """
        Log a critical message.

        Args:
            message (str): The critical message to be logged.
            status (int, optional): The status code for the critical message. Defaults to 500.

        Returns:
            None
        """
        self._log_with_status(logging.CRITICAL, message, status)
