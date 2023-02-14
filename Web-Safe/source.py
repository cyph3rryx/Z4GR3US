import requests

url = input("Enter website URL: ")

try:
    response = requests.get(url)
    if response.status_code >= 200 and response.status_code < 300:
        print("The website is safe.")
    elif response.status_code >= 400 and response.status_code < 500:
        print("The website is unsafe.")
    else:
        print("The safety of the website could not be determined.")
except requests.exceptions.RequestException:
    print("The website could not be reached.")
