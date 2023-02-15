import requests
from typing import Tuple

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
                    return (True, 'Website is safe')
            else:
                return (False, 'Website may be unsafe (content type is not HTML)')
        else:
            return (False, 'Website may be unsafe (bad response code: {})'.format(response.status_code))
    except requests.exceptions.Timeout:
        return (False, 'Website may be unsafe (timeout)')
    except requests.exceptions.RequestException:
        return (False, 'Website may be unsafe (request exception)')

# Example usage
url = input("Enter website URL: ")
is_safe, message = check_website_safety(url)
print(message)
