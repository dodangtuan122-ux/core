"""Structured logging."""
import logging

def setup_logger(name="devforge"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
