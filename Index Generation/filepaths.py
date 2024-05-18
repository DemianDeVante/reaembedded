import os

def generate_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, directory)
            file_paths.append(relative_path)
    return file_paths

directory = '/home/demian/Documents/GitHub/reaembedded/D JSFX/'
file_paths = generate_file_paths(directory)

with open('file_paths.txt', 'w') as f:
    for path in file_paths:
        f.write(f"{path}\n")

