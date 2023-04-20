# Logger
Logger is a Python script that logs startup information and the contents of the startup directory to a log file when your PC turns on. This script uses the logging module in Python to create a log file with the startup information and directory contents.

## Getting Started
To use Logger, you will need to have Python installed on your PC. You can download the latest version of Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you can download the Logger script from this repository.

## Usage
To use Logger, simply run the script using Python. You can do this by opening a command prompt or terminal window and navigating to the directory where the script is located. Then, run the following command:

``` python
python logger.py
```
The script will log the startup information and directory contents to a log file located in the same directory as the script.

## Customization
You can customize the log file location, logging level, and log message format by modifying the variables at the top of the script. The default log file location is 'startup_log.txt', and the default logging level is 'INFO'. The log message format is set to '%(asctime)s - %(levelname)s - %(message)s', which logs the timestamp, severity level, and message.

## Security Considerations
Running a script to log everything when your PC turns on may have security and privacy implications. Use this script responsibly and with caution. It is your responsibility to ensure that this script does not violate any laws or regulations and that it does not compromise the security or privacy of any users.

## License
This project is licensed under MIT License - see the LICENSE file for details.
