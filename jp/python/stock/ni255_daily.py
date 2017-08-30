import codecs
import csv
import os
import requests
import zipfile

URL              = 'http://k-db.com/indices/I101?download=csv'
OUTPUT_FILE_PATH = '/src/data/output.csv'

# GET raw data
r = requests.get(URL)
with open('/tmp/raw.csv', 'wb') as file:
    file.write(r.content)

# CONVERT data into utf8 CSV
with open(OUTPUT_FILE_PATH, 'w', newline='') as output:
    with codecs.open('/tmp/raw.csv', 'r', 'shiftjis') as input:
        output.write(input.read())
