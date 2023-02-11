import dns.resolver

def find_subdomains(domain):
    subdomains = set()
    try:
        answers = dns.resolver.query(domain, 'NS')
    except dns.resolver.NXDOMAIN:
        return subdomains
    except dns.resolver.NoAnswer:
        return subdomains

    for server in answers:
        subdomain = str(server).rstrip('.')
        subdomains.add(subdomain)

    return subdomains

domain = input("Enter a website domain: ")
subdomains = find_subdomains(domain)
print(f"Found {len(subdomains)} subdomains:")

filename = "subdomains.txt"
with open(filename, 'w') as file:
    for subdomain in subdomains:
        file.write(subdomain + '\n')

print(f"Results saved to {filename}")
