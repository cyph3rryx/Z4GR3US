# Z4GR3US -> Automated Recon Script

## Bug Bounty Recon Script

This is a bash script that automates the bug bounty recon process using a variety of tools.

## Prerequisites


- You will need to have the following tools installed:
  - subfinder
  - dirsearch
  - nmap
  - vulners
  - GetJS
  - GoLinkFinder
  - getallurls
  - WayBackUrls
  - WayBackRobots
  - MassDNS
  - Sublist3r
  - FFuF
  - XSSHunter
  - SQLMap
  - XXEInjector
  - SSRFDetector
  - GitTools
  - gitallsecrets
  - RaceTheWeb
  - CORStest
  - EyeWitness
  - parameth

## Usage

1. Clone this repository: 
`git clone https://github.com/user/repo.git`
2. Navigate to the directory: `cd repo`
3. Make the script executable: `chmod +x script.sh`
4. Set the target URL and list of subdomains in the script
5. Run the script: `./script.sh`

## What the script does

1. Performs a subdomain scan using `subfinder`
2. Performs a directory scan using `dirsearch`
3. Performs a port scan using `nmap`
4. Finds vulnerabilities using `vulners`
5. Finds JavaScript files using `GetJS`
6. Finds links using `GoLinkFinder`
7. Finds all URLs using `getallurls`
8. Finds URLs from WayBackMachine using `WayBackUrls`
9. Finds disallowed paths from WayBackMachine using `WayBackRobots`
10. Finds subdomains using `MassDNS`
11. Finds subdomains using `Sublist3r`
12. Finds parameters using `FFuF`
13. Finds XSS vulnerabilities using `XSSHunter`
14. Finds SQL injection vulnerabilities using `SQLMap`
15. Finds XXE vulnerabilities using `XXEInjector`
16. Finds SSRF vulnerabilities using `SSRFDetector`
17. Finds secrets in Git repositories using `GitTools` and `gitallsecrets`
18. Finds race condition vulnerabilities using `RaceTheWeb`
19. Tests for CORS misconfigurations using `CORStest`
20. Takes screenshots of all URLs using `EyeWitness`
21. Finds hidden parameters using `parameth`

## Customization

More customization on the way, so keep an eye on it.

