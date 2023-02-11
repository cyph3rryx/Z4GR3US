import dns.resolver

def find_subdomains(url):
    subdomains = set()
    domain = url.split('://')[1].split('/')[0]
    try:
        answers = dns.resolver.resolve(domain, 'A')
    except dns.resolver.NXDOMAIN:
        return subdomains
    except dns.resolver.NoAnswer:
        return subdomains

    for rdata in answers:
        subdomains.add(domain)

    return subdomains

url = input("Enter a website URL: ")
subdomains = find_subdomains(url)
print(f"Found {len(subdomains)} subdomains:")

filename = "subdomains.txt"
with open(filename, 'w') as file:
    for subdomain in subdomains:
        file.write(subdomain + '\n')

print(f"Results saved to {filename}")
