file_paths = [line.strip() for line in open('file_paths.txt')]
github_links = [line.strip() for line in open('github_links.txt')]

xml_entries = []

for path, link in zip(file_paths, github_links):
    entry = f'<source file="{path}">{link}</source>'
    xml_entries.append(entry)

with open('xml_entries.txt', 'w') as f:
    for entry in xml_entries:
        f.write(f"{entry}\n")

