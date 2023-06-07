import socket
import os
import subprocess
import sys
import platform
import paramiko
import nmap
import logging

RED = "\033[1;31m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"

logging.basicConfig(filename='security_check.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def print_success(message):
    print(GREEN + message + RESET)

def print_failure(message):
    print(RED + message + RESET)

def check_firewall(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))

        if result == 0:
            print_success("Firewall not detected")
            logging.info("Firewall not detected")
        else:
            print_failure("Firewall detected")
            logging.warning("Firewall detected")
    except Exception as e:
        print_failure("Error while checking firewall: " + str(e))
        logging.error("Error while checking firewall: " + str(e))

def check_ids(host, port):
    try:
        response = os.system("hping3 " + host + " -p " + str(port) + " -c 1")
        if response == 0:
            print_success("Intrusion Detection System not detected")
            logging.info("Intrusion Detection System not detected")
        else:
            print_failure("Intrusion Detection System detected")
            logging.warning("Intrusion Detection System detected")
    except Exception as e:
        print_failure("Error while checking Intrusion Detection System: " + str(e))
        logging.error("Error while checking Intrusion Detection System: " + str(e))

def check_antivirus(host):
    if platform.system() == "Windows":
        try:
            process = subprocess.Popen(['powershell.exe', f'-ComputerName {host}', 'Get-MpComputerStatus'], stdout=subprocess.PIPE)
            stdout = process.communicate()[0]
            if b"Enabled" in stdout:
                print_failure("Antivirus detected")
                logging.warning("Antivirus detected")
            else:
                print_success("Antivirus not detected")
                logging.info("Antivirus not detected")
        except Exception as e:
            print_failure("Error while checking antivirus: " + str(e))
            logging.error("Error while checking antivirus: " + str(e))
    else:
        print("Antivirus check not available on this operating system")

def check_nsg(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print_success("Network Security Group not detected")
            logging.info("Network Security Group not detected")
        else:
            print_failure("Network Security Group detected")
            logging.warning("Network Security Group detected")
    except Exception as e:
        print_failure("Error while checking Network Security Group: " + str(e))
        logging.error("Error while checking Network Security Group: " + str(e))

def check_ips(host, port):
    try:
        response = os.system("hping3 " + host + " -p " + str(port) + " -c 5")
        if response == 0:
            print_success("Intrusion Prevention System not detected")
            logging.info("Intrusion Prevention System not detected")
        else:
            print_failure("Intrusion Prevention System detected")
            logging.warning("Intrusion Prevention System detected")
    except Exception as e:
        print_failure("Error while checking Intrusion Prevention System: " + str(e))
        logging.error("Error while checking Intrusion Prevention System: " + str(e))

def check_website_os(host):
    try:
        nm = nmap.PortScanner()
        nm.scan(host, arguments='-O')
        if 'osclass' in nm[host]:
            for osclass in nm[host]['osclass']:
                print("Operating System: " + osclass['osfamily'])
                logging.info("Operating System: " + osclass['osfamily'])
        else:
            print("Operating System: Unknown")
            logging.info("Operating System: Unknown")
    except Exception as e:
        print("Error: Unable to scan target")
        logging.error("Error: Unable to scan target")

def check_service(service_name):
    try:
        service_status = subprocess.run(["systemctl", "is-active", service_name], capture_output=True, text=True)
        if "active" in service_status.stdout:
            print(service_name, "service is running")
            logging.info(service_name + " service is running")
        else:
            print(service_name, "service is not running")
            logging.warning(service_name + " service is not running")
    except Exception as e:
        print("Error while checking service:", str(e))
        logging.error("Error while checking service: " + str(e))

def check_log4js_remote(host, port=22):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, timeout=20)

        stdin, stdout, stderr = ssh.exec_command("npm list --depth=0")
        log4js = stdout.read().decode("utf-8")

        if "log4js" in log4js:
            print_failure("log4js detected")
            logging.warning("log4js detected")
        else:
            print_success("log4js not detected")
            logging.info("log4js not detected")

        ssh.close()
    except Exception as e:
        print_failure("Error while checking for log4js: " + str(e))
        logging.error("Error while checking for log4js: " + str(e))

def use_nameserver():
    try:
        with open("nameserver.txt", "r") as file:
            nameserver = file.read().strip()
    except FileNotFoundError:
        nameserver = input("Enter nameserver address: ")
        with open("nameserver.txt", "w") as file:
            file.write(nameserver)
    return nameserver

def perform_security_checks():
    try:
        if platform.system() == "Windows":
            host = use_nameserver()
        else:
            host = input("Enter hostname or IP address: ")

        port = int(input("Enter port number: "))

        print("\nPerforming security checks...\n")

        check_website_os(host)
        check_service("ssh")
        check_service("httpd")
        check_firewall(host, port)
        check_ids(host, port)
        check_antivirus(host)
        check_log4js_remote(host, port=22)
        check_nsg(host, port)
        check_ips(host, port)

        print("\nSecurity checks completed.")

    except Exception as e:
        print_failure("Error: " + str(e))
        logging.error("Error: " + str(e))

if __name__ == "__main__":
    print("Uchigatana - The Virus Slayer")
    print("--------------------------")
    logging.info("Security check started")
    perform_security_checks()
