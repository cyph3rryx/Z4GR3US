# Wordpress Bruteforcer

## Overview

**Wordpress Bruteforcer** is a Python script designed for web application security testing. It attempts to brute force login credentials for WordPress websites by trying different combinations of usernames and passwords against a target URL. This tool is intended for ethical and legal use only, such as testing the security of your own WordPress websites or with explicit permission from the target site owner.

## Features

- Brute force login attempts for WordPress websites using a list of usernames and passwords.
- Supports different modes for sending login requests:
  - **'body' mode**: Sends credentials in the request body.
  - **'cookie' mode**: Sends credentials as cookies in the request.
- Logs successful login attempts.
- Uses the `requests` library for HTTP communication.

## Prerequisites

Before using the Wordpress Bruteforcer, make sure you have:

- Python installed (3.7 or higher).
- The `requests` library installed. You can install it using `pip install requests`.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/cyph3rryx/Wordpress%20Bruteforcer.git
   cd Wordpress Bruteforcer
   ```

2. Customize the configuration:

   Open the `bruteforcer.py` file and configure the following variables in the `BruteForcer` class constructor:
   - `target_url`: The URL of the target WordPress login page.
   - `usernames`: A list of usernames to try.
   - `password_list`: A list of passwords to try.
   - `pw_field_name`: The name of the password field in the WordPress login form (default: 'pw').
   - `pw_to_check_type`: The mode for sending login requests ('body' or 'cookie', default: 'body').

3. Run the script:

   ```bash
   python bruteforcer.py
   ```

## License

This project is licensed under the MIT License - see the LICENSE.MD file for details.
