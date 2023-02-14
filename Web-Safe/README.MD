# Web-Safe

Web-Safe is a Python script that recognizes if a website is safe or not based on its HTTP response code.

## Prerequisites

To use Web-Safe, you need to have Python 3 and the `requests` library installed. You can install the `requests` library using pip:

```sh
pip install requests
```

Usage

To use Web-Safe, run the web_safe.py file with Python and enter a website URL when prompted. The script will send an HTTP GET request to the website and print a message indicating whether the website is safe or not based on the response status code.

``` python
python web_safe.py
```
## Example

Here is an example of using Web-Safe to check if the website "https://example.com" is safe:

```python
python web_safe.py
Enter website URL: https://example.com
The website is safe.
```
