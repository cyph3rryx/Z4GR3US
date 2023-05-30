import re

# Define the SQL injection detection rule
def detect_sql_injection(code):
    pattern = r'\$sql\s*\=\s*".*?\'\s*\.\s*\$.*?".*?;'
    matches = re.findall(pattern, code)
    if matches:
        return True
    return False

# Main function to process the code
def process_code(code):
    vulnerabilities = []
    
    # Check for SQL injection
    if detect_sql_injection(code):
        vulnerabilities.append("Potential SQL Injection found!")
    
    # Add more rules for other security vulnerabilities
    
    return vulnerabilities

# Example usage
php_code = '''
$user_input = $_GET['username'];
$sql = "SELECT * FROM users WHERE username = '" . $user_input . "'";
$result = mysql_query($sql);
'''

results = process_code(php_code)
if results:
    print("Vulnerabilities found:")
    for vulnerability in results:
        print(vulnerability)
else:
    print("No vulnerabilities found.")
