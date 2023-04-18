import os
import logging
import dropbox

log_filename = 'startup_log.txt'
dropbox_access_token = 'your-dropbox-access-token'

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_handler = logging.FileHandler(log_filename)
log_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

# Add the following lines to upload the log file to Dropbox
with open(log_filename, 'rb') as f:
    dbx = dropbox.Dropbox(dropbox_access_token)
    dbx.files_upload(f.read(), '/' + log_filename)
