import os
import logging.handlers

log_filename = 'startup_log.txt'
log_max_bytes = 1024 * 1024  # 1 MB
log_backup_count = 5  # Keep up to 5 old log files

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=log_max_bytes, backupCount=log_backup_count)
log_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)
