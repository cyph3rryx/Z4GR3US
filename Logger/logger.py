import logging
import os

# Define the log file location and format
log_file = 'startup_log.txt'
log_format = '%(asctime)s - %(levelname)s - %(message)s'

# Set up the logging configuration
logging.basicConfig(filename=log_file, level=logging.INFO, format=log_format)

# Log the startup information
logging.info('PC started up')

# Log the contents of the startup directory
startup_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
logging.info('Startup directory contents:')
for file in os.listdir(startup_dir):
    logging.info(file)
