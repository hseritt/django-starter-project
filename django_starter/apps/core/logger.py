import logging
import sys
from config.settings.settings import (
    LOGGING_FORMAT,
    LOGGING_LEVEL,
    LOG_FILE,
    LOG_FILE_WRITE_MODE,
)


def get_logger(name=None):
    if name is None:
        name = __name__

    logger = logging.getLogger(name)
    log_format = logging.Formatter(LOGGING_FORMAT)
    logger.setLevel(LOGGING_LEVEL)

    if not logger.handlers:
        file_handler = logging.FileHandler(
            filename=LOG_FILE, mode=LOG_FILE_WRITE_MODE
        )
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_format)
        logger.addHandler(console_handler)

    return logger
