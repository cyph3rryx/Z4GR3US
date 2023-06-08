# Uchigatana

Uchigatana is a powerful security tool that allows you to perform various security checks on a target system or network. It helps identify potential vulnerabilities and security measures in place. The tool is designed to provide an easy-to-use interface for conducting basic security assessments.

## Features

- Firewall detection: Checks if a firewall is detected on the target system.
- Intrusion Detection System (IDS) detection: Identifies if an IDS is detected on the target system.
- Antivirus detection: Determines if an antivirus software is detected on the target system.
- Network Security Group (NSG) detection: Checks if an NSG is detected on the target system.
- Intrusion Prevention System (IPS) detection: Identifies if an IPS is detected on the target system.
- Website OS detection: Scans the target website to determine the operating system it is running on.
- Service status check: Checks the status of specified services (e.g., SSH, HTTP) on the target system.
- log4js detection: Checks if the log4js package is detected on a remote system through SSH.

## Installation

1. Clone the Uchigatana repository:

   ```
   git clone https://github.com/your-username/Uchigatana.git
   ```

2. Install the required dependencies:

   Ensure that you have the necessary packages such as `paramiko` and `nmap` installed.

3. Run the tool:

   ```
   python uchigatana.py
   ```

## Usage

1. Enter the hostname or IP address of the target system when prompted.
2. Provide the port number to connect to on the target system.
3. Uchigatana will perform a series of security checks and display the results on the console.
4. The results will also be logged in the "security_check.log" file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the Uchigatana repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Uchigatana is a tool meant for security assessments and should only be used with proper authorization. The developers assume no liability and are not responsible for any misuse or damages caused by the tool. Use it at your own risk.

