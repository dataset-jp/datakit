import requests

def download(url, file_path):
    r = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(r.content)

import zipfile
def unzip(original_file_path, dist_dir):
    with zipfile.ZipFile(original_file_path, 'r') as zip_ref:
        zip_ref.extractall(dist_dir)
