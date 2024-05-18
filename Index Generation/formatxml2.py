import os
import urllib.parse

def generate_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, directory)
            file_paths.append(relative_path)
    return file_paths

def generate_github_links(username, repository, branch, file_paths):
    base_url = f"https://raw.githubusercontent.com/{username}/{repository}/{branch}/"
    links = [base_url + urllib.parse.quote(path.replace("\\", "/")) for path in file_paths]
    return links

directory = '/path/to/your/files'  # Replace with your directory
username = 'your_github_username'
repository = 'your_repository'
branch = 'main'  # or whatever branch you're using

file_paths = generate_file_paths(directory)
github_links = generate_github_links(username, repository, branch, file_paths)

xml_entries = []

for path, link in zip(file_paths, github_links):
    entry = f'<source file="{path}">{link}</source>'
    xml_entries.append(entry)

with open('xml_entries.txt', 'w') as f:
    for entry in xml_entries:
        f.write(f"{entry}\n")

print("XML entries generated successfully.")

