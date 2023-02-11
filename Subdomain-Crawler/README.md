# Subdomain Finder
A tool to find and save subdomains of a given website.

## Introduction
Subdomain Finder is a program that takes a website URL as input, finds all its subdomains and saves the result in a text file with date, time, and domain name. The program uses various tools to gather subdomains information and optimize the user's time. During the loading time, an ASCII text is displayed to remove the boring loading screen.

## Requirements
- Python 3
- Subfinder (can be installed using `go get -u github.com/projectdiscovery/subfinder/cmd/subfinder`)

## Usage
1. Clone the repository: `git clone https://github.com/YOUR_USERNAME/Subdomain-Finder.git`
2. Change the directory: `cd Subdomain-Finder`
3. Run the program: `python main.py`
4. Enter the website URL you want to find subdomains for
5. The result will be saved in a text file `subdomains.txt` in the same directory

## Note: 
You need to install the subfinder program on your system, and ensure that it's installed in a directory that's in your PATH environment variable. I am working on that part but feel free to contribute on this project.

## Contributions
Feel free to contribute to the project by opening a pull request or by reporting issues.

## License
This project is licensed under the MIT License.
