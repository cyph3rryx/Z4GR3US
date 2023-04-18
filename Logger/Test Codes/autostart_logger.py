import os
import logging

log_filename = 'startup_log.txt'

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_handler = logging.FileHandler(log_filename)
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
