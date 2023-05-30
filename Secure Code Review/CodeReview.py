import re

class SecureCodeReviewTool:
    def __init__(self, rules=None):
        self.rules = rules or []
    
    def add_rule(self, rule):
        self.rules.append(rule)
    
    def detect_vulnerabilities(self, code):
        vulnerabilities = []
        for rule in self.rules:
            matches = re.findall(rule, code)
            if matches:
                vulnerabilities.append(matches)
        return vulnerabilities
    
    def process_code(self, code):
        vulnerabilities = []
        detected_vulnerabilities = self.detect_vulnerabilities(code)
        if detected_vulnerabilities:
            vulnerabilities.append(detected_vulnerabilities)
        return vulnerabilities

# Example usage
php_code = '''
$user_input = $_GET['username'];
$sql = "SELECT * FROM users WHERE username = '" . $user_input . "'";
$result = mysql_query($sql);
echo $_GET['search'];
$password = md5('password');
'''

tool = SecureCodeReviewTool()
tool.add_rule(r'\$sql\s*\=\s*".*?\'\s*\.\s*\$.*?".*?;')
tool.add_rule(r'echo\s*\$.*?;')
tool.add_rule(r'crypt\s*\(.*?,\s*.*?\)')
tool.add_rule(r'echo\s*\$_(GET|POST|REQUEST|COOKIE|SERVER|ENV|FILES|SESSION)\[.*?\]\s*;')
tool.add_rule(r'(md5|sha1)\s*\(.+?\)')

results = tool.process_code(php_code)
if results:
    print("Vulnerabilities found:")
    for vulnerability in results:
        print(vulnerability)
else:
    print("No vulnerabilities found.")
