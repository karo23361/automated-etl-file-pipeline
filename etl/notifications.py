import logging

logger = logging.getLogger(__name__)

def notify_error(message: str):
    logger.error(f"Error: {message}")