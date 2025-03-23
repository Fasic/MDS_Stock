import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Main logger configuration
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # File handler (rotating logs)
    file_handler = RotatingFileHandler(log_dir / "app.log", maxBytes=1024 * 1024 * 5, backupCount=10)  # 5MB
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Disable Uvicorn's default handlers if needed
    logging.getLogger("uvicorn").handlers = []
    logging.getLogger("uvicorn.access").handlers = []

    # Setup peewee logger
    logger = logging.getLogger("peewee")
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    return logger
