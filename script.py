#!/usr/bin/env python3

import subprocess
import os

# Set target URL and create folder for results
target_url = input("Enter target URL (e.g. https://example.com): ")
folder_name = target_url.split("//")[1]
os.system(f"mkdir /home/user/Desktop/{folder_name}")

# Set list of subdomains to scan
subdomains_list = input("Enter list of subdomains to scan (separated by spaces): ")

# Perform subdomain scan
print("\nZ4GR3US - Performing subdomain scan...")
subprocess.run(["subfinder", "-d", target_url, "-o", f"/home/user/Desktop/{folder_name}/subdomains.txt"])
subprocess.run(["sort", "-u", f"/home/user/Desktop/{folder_name}/subdomains.txt", ">", f"/home/user/Desktop/{folder_name}/subdomains-sorted.txt"])
subprocess.run(["mv", f"/home/user/Desktop/{folder_name}/subdomains-sorted.txt", f"/home/user/Desktop/{folder_name}/subdomains.txt"])

# Perform directory scan
print("\nZ4GR3US - Performing directory scan...")
with open(f"/home/user/Desktop/{folder_name}/subdomains.txt", "r") as f:
    for subdomain in f:
        subdomain = subdomain.strip()
        print(f"Scanning {subdomain}")
        subprocess.run(["dirsearch", "-u", subdomain, "-e", "*", "-t", "50", "-w", "/path/to/wordlist.txt", "-x", "400,403,401,429"])

# Perform port scan
print("\nZ4GR3US - Performing port scan...")
subprocess.run(["nmap", "-sS", "-Pn", "-sV", "-T4", "-p-", target_url, "-o", f"/home/user/Desktop/{folder_name}/nmap-scan.txt"])

# Find vulnerabilities using Vulners
print("\nZ4GR3US - Finding vulnerabilities using Vulners...")
subprocess.run(["vulners", "-c", "bash -c 'cat nmap-scan.txt'", ">", f"/home/user/Desktop/{folder_name}/vulners-scan.txt"])

# Find JavaScript files using GetJS
print("\nZ4GR3US - Finding JavaScript files using GetJS...")
with open(f"/home/user/Desktop/{folder_name}/subdomains.txt", "r") as f:
    for subdomain in f:
        subdomain = subdomain.strip()
        print(f"Scanning {subdomain}")
        subprocess.run(["getjs", "-u", subdomain, "-o", f"/home/user/Desktop/{folder_name}/js-files.txt"])

# Find links using GoLinkFinder
print("\nZ4GR3US - Finding links using GoLinkFinder...")
with open(f"/home/user/Desktop/{folder_name}/subdomains.txt", "r") as f:
    for subdomain in f:
        subdomain = subdomain.strip()
        print(f"Scanning {subdomain}")
        subprocess.run(["golinkfinder", "-u", subdomain, "-o", f"/home/user/Desktop/{folder_name}/links.txt"])

# Find all URLs using getallurls
print("\nZ4GR3US - Finding all URLs using getallurls...")
subprocess.run(["getallurls", "-u", target_url, "-o", f"/home/user/Desktop/{folder_name}/all-urls.txt"])

# Find URLs from WayBackMachine using WayBackUrls
print("\nZ4GR3US - Finding URLs from WayBackMachine using WayBackUrls...")
subprocess.run(["waybackurls", target_url, ">", f"/home/user/Desktop/{folder_name}/wayback-urls.txt"])

# Find disallowed paths from WayBackMachine using WayBackRobots
print("\nZ4GR3US - Finding disallowed paths from WayBackMachine using WayBackRobots...")
subprocess.run(["waybackrobots", target_url, ">", f"/home/user/Desktop/{folder_name}/wayback-robots.txt"])

# Find subdomains using MassDNS
print("\nZ4GR3US - Finding subdomains using MassDNS...")
subprocess.run(["massdns", "-r", "/path/to/resolvers.txt", "-t", "A", "-o", "S", "-w", f"/home/user/Desktop/{folder_name}/massdns-output.txt", "/path/to/subdomains.txt"])

# Find subdomains using Sublist3r
print("\nZ4GR3US - Finding subdomains using Sublist3r...")
subprocess.run(["sublist3r", "-d", target_url, "-o", f"/home/user/Desktop/{folder_name}/sublist3r-output.txt"])

# Find parameters using FFuF
print("\nZ4GR3US - Finding parameters using FFuF...")
subprocess.run(["ffuf", "-u", f"{target_url}/FUZZ", "-w", "/path/to/wordlist.txt", "-mc", "all", "-o", f"/home/user/Desktop/{folder_name}/parameters.txt"])

# Find secrets in Git repositories using GitTools
print("\nZ4GR3US - Finding secrets in Git repositories using GitTools...")
subprocess.run(["gittools", "-u", target_url, "-o", f"/home/user/Desktop/{folder_name}/git-repositories.txt"])
with open(f"/home/user/Desktop/{folder_name}/git-repositories.txt", "r") as f:
    for repo in f:
        repo = repo.strip()
        subprocess.run(["gitallsecrets", "-u", repo, "-o", f"/home/user/Desktop/{folder_name}/secrets-in-git.txt"])

# Find race condition vulnerabilities using RaceTheWeb
print("\nZ4GR3US - Finding race condition vulnerabilities using RaceTheWeb...")
subprocess.run(["racetheweb", "-u", target_url, "-o", f"/home/user/Desktop/{folder_name}/race-conditions.txt"])

# Test for CORS misconfigurations using CORStest
print("\nZ4GR3US - Testing for CORS misconfigurations using CORStest...")
subprocess.run(["corstest", "-u", target_url, "-o", f"/home/user/Desktop/{folder_name}/cors-test.txt"])

# Take screenshots of all URLs using EyeWitness
print("\nZ4GR3US - Taking screenshots of all URLs using EyeWitness...")
subprocess.run(["eyewitness", "-f", f"/home/user/Desktop/{folder_name}/all-urls.txt", "-d", f"/home/user/Desktop/{folder_name}/eyewitness-screenshots"])

# Find hidden parameters using parameth
print("\nZ4GR3US - Finding hidden parameters using parameth...")
subprocess.run(["parameth", "-u", target_url, "-o", f"/home/user/Desktop/{folder_name}/hidden-parameters.txt"])

print("\nZ4GR3US - Bug bounty recon process complete!")
    

