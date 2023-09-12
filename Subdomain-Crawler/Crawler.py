import subprocess
import datetime
import time
import os

def print_loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        print("\r" + "Gathering subdomains... " + animation[i % len(animation)], end="")

def find_subdomains(domain):
    try:
        result = subprocess.run(['subfinder', '-d', domain], stdout=subprocess.PIPE, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to find subdomains: {str(e)}")
        return []
    else:
        subdomains = result.stdout.splitlines()
        return subdomains

def save_to_file(subdomains, domain):
    filename = f"subdomains_{domain}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(subdomains))
    except IOError as e:
        print(f"An error occurred while trying to write to the file: {str(e)}")
    else:
        print(f"Results saved to {filename}")

if __name__ == '__main__':
    print("Welcome to the subdomain finder program.")
    domain = input("Enter a website URL: ")
    print_loading_animation()
    subdomains = find_subdomains(domain)
    print(f"Found {len(subdomains)} subdomains:")
    print('\n'.join(subdomains))
    save_to_file(subdomains, domain)
