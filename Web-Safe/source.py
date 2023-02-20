import requests
import ssl
import datetime
from typing import Tuple
from googlesearch import search
import urllib.request
import urllib.error
import re
from bs4 import BeautifulSoup
import virustotal_api

#Initialize the VirusTotal API
VT_API_KEY = 'YOUR_API_KEY'
vt = virustotal_api.Client(API_KEY)

def check_website_safety(url: str) -> Tuple[bool, str]:
    """
    Checks if a website is safe or not by sending an HTTP GET request to the URL
    and analyzing the response. Returns a tuple containing a boolean indicating
    whether the website is safe or not, and a string describing the result.
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == requests.codes.ok:
            content_type = response.headers.get('Content-Type')
            if 'text/html' in content_type:
                if 'Not Found' in response.text or 'Error' in response.text:
                    return (False, 'Website may be unsafe (page not found or error message)')
                else:
                    return (check_ssl_certificate(response), check_for_malware(url))
            else:
                return (False, 'Website may be unsafe (content type is not HTML)')
        else:
            return (False, 'Website may be unsafe (bad response code: {})'.format(response.status_code))
    except requests.exceptions.Timeout:
        return (False, 'Website may be unsafe (timeout)')
    except requests.exceptions.RequestException:
        return (False, 'Website may be unsafe (request exception)')

def check_ssl_certificate(response: requests.Response) -> Tuple[bool, str]:
    """
    Checks if the website's SSL/TLS certificate is valid.
    Returns a tuple containing a boolean indicating whether the certificate is valid or not,
    and a string describing the result.
    """
    try:
        ssl_info = ssl.get_server_certificate((response.url, 443))
        x509 = ssl.load_certificate(ssl_info.encode())
        expire_date = x509.get_notAfter().decode("utf-8")
        expire_date_obj = datetime.datetime.strptime(expire_date, '%Y%m%d%H%M%SZ')
        if expire_date_obj < datetime.datetime.now():
            return (False, 'Website may be unsafe (SSL certificate expired on {})'.format(expire_date_obj.strftime('%d %B %Y')))
        else:
            return (True, 'Website has a valid SSL certificate (expires on {})'.format(expire_date_obj.strftime('%d %B %Y')))
    except Exception as e:
        return (False, 'Unable to check SSL certificate: {}'.format(str(e)))

def check_for_malware(url: str) -> Tuple[bool, str]:
    """
    Checks if the website is infected with any malware or viruses using VirusTotal API.
    Returns a tuple containing a boolean indicating whether the website is infected or not,
    and a string describing the result.
    """
    try:
        # Scan the URL using VirusTotal API
        scan_result = vt.scan_url(url)
        scan_id = scan_result['scan_id']
        # Retrieve the scan report using the scan ID
        report = vt.get_report(scan_id)
        if report['results']['positives'] > 0:
            return (False, 'Website may be unsafe (detected as malware by VirusTotal)')
        else:
            return (True, 'Website is safe (not detected as malware by VirusTotal)')
    except Exception as e:
        return (False, 'Unable to check for malware: {}'.format(str(e)))

# Example usage
url = input("Enter website URL: ")
is_safe, message = check_website_safety(url)
print(message)
