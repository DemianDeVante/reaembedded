import os

def generate_github_links(username, repository, branch, file_paths):
    base_url = f"https://raw.githubusercontent.com/{username}/{repository}/{branch}/"
    links = [base_url + path.replace("\\", "/") for path in file_paths]
    return links

username = 'DemianDeVante'
repository = 'reaembedded'
branch = 'main'  # or whatever branch you're using
file_paths = [line.strip() for line in open('file_paths.txt')]

github_links = generate_github_links(username, repository, branch, file_paths)

with open('github_links.txt', 'w') as f:
    for link in github_links:
        f.write(f"{link}\n")

