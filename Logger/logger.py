import os
import logging
import logging.handlers
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

log_filename = 'startup_log.txt'
log_max_bytes = 1024 * 1024  # 1 MB
log_backup_count = 5  # Keep up to 5 old log files
gmail_user = 'your-gmail-username'
gmail_password = 'your-gmail-password'
recipient = 'recipient-email-address'

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=log_max_bytes, backupCount=log_backup_count)
log_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

# Add the following lines to run the script at startup
startup_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startup_script_path = os.path.abspath(__file__)
startup_script_link_path = os.path.join(startup_path, 'Logger.lnk')

if not os.path.exists(startup_script_link_path):
    from win32com.client import Dispatch
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(startup_script_link_path)
    shortcut.Targetpath = startup_script_path
    shortcut.WorkingDirectory = os.path.dirname(startup_script_path)
    shortcut.save()

# Add the following lines to send the log file via email
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = recipient
msg['Subject'] = 'Startup Log'

with open(log_filename, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='txt')
    attachment.add_header('Content-Disposition', 'attachment', filename=log_filename)
    msg.attach(attachment)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user, recipient, msg.as_string())
server.quit()
