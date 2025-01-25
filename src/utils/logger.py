"""Structured logging."""
import logging

def setup_logger(name="devforge"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

# Updated: 2025-01-25T11:00:00