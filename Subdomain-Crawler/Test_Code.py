import subprocess

def find_subdomains(domain):
    subdomains = set()

    # Use Sublist3r
    result = subprocess.run(['sublist3r', '-d', domain], stdout=subprocess.PIPE)
    subdomains.update(result.stdout.decode().splitlines())

    # Use SubFinder
    result = subprocess.run(['subfinder', '-d', domain], stdout=subprocess.PIPE)
    subdomains.update(result.stdout.decode().splitlines())

    # Use Knockpy
    result = subprocess.run(['knockpy', domain], stdout=subprocess.PIPE)
    subdomains.update(result.stdout.decode().splitlines())

    return list(subdomains)

if __name__ == '__main__':
    domain = input('Enter a website URL: ')
    subdomains = find_subdomains(domain)
    print('Found {} subdomains:'.format(len(subdomains)))
    for subdomain in subdomains:
        print(subdomain)
    with open('subdomains.txt', 'w') as f:
        f.write('\n'.join(subdomains))
    print('Results saved to subdomains.txt')
