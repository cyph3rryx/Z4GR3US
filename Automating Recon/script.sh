#!/bin/bash

# Set target URL
echo "Enter target URL (e.g. https://example.com):"
read target_url

# Set list of subdomains to scan
echo "Enter list of subdomains to scan (separated by spaces):"
read -a subdomains_list

# Perform subdomain scan
echo "Performing subdomain scan..."
subfinder -d $target_url -o subdomains.txt
cat subdomains.txt | sort -u > subdomains-sorted.txt
mv subdomains-sorted.txt subdomains.txt

# Perform directory scan
echo "Performing directory scan..."
for subdomain in $(cat subdomains.txt)
do
  echo "Scanning $subdomain"
  dirsearch -u $subdomain -e * -t 50 -w /path/to/wordlist.txt -x 400,403,401,429
done

# Perform port scan
echo "Performing port scan..."
nmap -sS -Pn -sV -T4 -p- $target_url -o nmap-scan.txt

# Find vulnerabilities using Vulners
echo "Finding vulnerabilities using Vulners..."
vulners -c "bash -c 'cat nmap-scan.txt'" > vulners-scan.txt

# Find JavaScript files using GetJS
echo "Finding JavaScript files using GetJS..."
for subdomain in $(cat subdomains.txt)
do
  echo "Scanning $subdomain"
  getjs -u $subdomain -o js-files.txt
done

# Find links using GoLinkFinder
echo "Finding links using GoLinkFinder..."
for subdomain in $(cat subdomains.txt)
do
  echo "Scanning $subdomain"
  golinkfinder -u $subdomain -o links.txt
done

# Find all URLs using getallurls
echo "Finding all URLs using getallurls..."
getallurls -u $target_url -o all-urls.txt

# Find URLs from WayBackMachine using WayBackUrls
echo "Finding URLs from WayBackMachine using WayBackUrls..."
waybackurls $target_url > wayback-urls.txt

# Find disallowed paths from WayBackMachine using WayBackRobots
echo "Finding disallowed paths from WayBackMachine using WayBackRobots..."
waybackrobots $target_url > wayback-robots.txt

# Find subdomains using MassDNS
echo "Finding subdomains using MassDNS..."
massdns -r /path/to/resolvers.txt -t A -o S -w massdns-output.txt /path/to/subdomains.txt

# Find subdomains using Sublist3r
echo "Finding subdomains using Sublist3r..."
sublist3r -d $target_url -o sublist3r-output.txt

# Find parameters using FFuF
echo "Finding parameters using FFuF..."
ffuf -u $target_url/FUZZ -w /path/to/wordlist.txt -fc 403 -o fuf-output.txt

# Find XSS vulnerabilities using XSSHunter
echo "Finding XSS vulnerabilities using XSSHunter..."
for subdomain in $(cat subdomains.txt)
do
  echo "Scanning $subdomain"
  xsshunter -u $subdomain -o xss-vulnerabilities.txt
done

# Find SQL injection vulnerabilities using SQLMap
echo "Finding SQL injection vulnerabilities using SQLMap..."
for subdomain in $(cat subdomains.txt)
do
  echo "Scanning $subdomain"
  sqlmap -u $subdomain --dbs --batch
done

# Find XXE vulnerabilities using XXEInjector
echo "Finding XXE vulnerabilities using XXEInjector..."
for subdomain in $(cat subdomains.txt)
do
  echo "Scanning $subdomain"
  xxeinjector -u $subdomain -o xxe-vulnerabilities.txt
done

# Find SSRF vulnerabilities using SSRFDetector
echo "Finding SSRF vulnerabilities using SSRFDetector..."
for subdomain in $(cat subdomains.txt)
do
  echo "Scanning $subdomain"
  ssrfdetector -u $subdomain -o ssrf-vulnerabilities.txt
done

# Find secrets in Git repositories using GitTools
echo "Finding secrets in Git repositories using GitTools..."
gittools -u $target_url -o git-repositories.txt
for repo in $(cat git-repositories.txt)
do
  gitallsecrets -u $repo -o secrets.txt
done

# Find race condition vulnerabilities using RaceTheWeb
echo "Finding race condition vulnerabilities using RaceTheWeb..."
racetheweb -u $target_url -o race-conditions.txt

# Test for CORS misconfigurations using CORStest
echo "Testing for CORS misconfigurations using CORStest..."
corstest -u $target_url -o cors-test.txt

# Take screenshots of all URLs using EyeWitness
echo "Taking screenshots of all URLs using EyeWitness..."
eyewitness -f all-urls.txt -d eyewitness-screenshots

# Find hidden parameters using parameth
echo "Finding hidden parameters using parameth..."
parameth -u $target_url -o hidden-parameters.txt

echo "Bug bounty recon process complete!"


