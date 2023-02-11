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
    result = subprocess.run(['subfinder', '-d', domain], stdout=subprocess.PIPE)
    subdomains = result.stdout.decode().splitlines()
    return subdomains

def save_to_file(subdomains, domain):
    filename = f"subdomains_{domain}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(filename, 'w') as file:
        file.write('\n'.join(subdomains))
    print(f"Results saved to {filename}")

if __name__ == '__main__':
    print("Welcome to the subdomain finder program.")
    domain = input("Enter a website URL: ")
    print_loading_animation()
    subdomains = find_subdomains(domain)
    print(f"Found {len(subdomains)} subdomains:")
    print('\n'.join(subdomains))
    save_to_file(subdomains, domain)
