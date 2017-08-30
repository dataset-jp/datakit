import codecs
import csv
import os
import requests
import zipfile

URL              = 'http://ykaku.com/ginkokensaku/ginkositen.zip'
OUTPUT_FILE_PATH = '/src/data/output.csv'

# GET raw data
r = requests.get(URL)
with open('/tmp/raw.zip', 'wb') as file:
    file.write(r.content)

# UNZIP data
with zipfile.ZipFile('/tmp/raw.zip', 'r') as zip_ref:
    zip_ref.extractall('/tmp')

# CONVERT data into CSV
with open(OUTPUT_FILE_PATH, 'w', newline='') as output:
    spamwriter = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with codecs.open('/tmp/ginkositen.txt', 'r', 'shiftjis') as input:
        spamreader = csv.reader(input, delimiter=',', quotechar='"')
        for row in spamreader:
            spamwriter.writerow([x.strip() for x in row])
