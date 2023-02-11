import sublist3r

def find_subdomains(url):
    subdomains = set()
    domain = url.split('://')[1].split('/')[0]

    try:
        subdomains = sublist3r.main(domain, savefile='subdomains.txt', silent=True)
    except:
        return subdomains

    return subdomains

url = input("Enter a website URL: ")
subdomains = find_subdomains(url)
print(f"Found {len(subdomains)} subdomains:")

filename = "subdomains.txt"
with open(filename, 'w') as file:
    for subdomain in subdomains:
        file.write(subdomain + '\n')

print(f"Results saved to {filename}")
