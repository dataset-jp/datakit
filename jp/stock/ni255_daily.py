import codecs
import csv
import os
import requests

URL = 'http://k-db.com/indices/I101?download=csv'
OUTPUT_DIR       = '/tmp/build'
OUTPUT_FILE_PATH = OUTPUT_DIR + '/output.csv'

# GET raw data
r = requests.get(URL)
with open(OUTPUT_DIR + '/raw.csv', 'wb') as file:
    file.write(r.content)

# CONVERT data into utf8 CSV
with open(OUTPUT_FILE_PATH, 'w', newline='') as output:
    with codecs.open(OUTPUT_DIR + '/raw.csv', 'r', 'shiftjis') as input:
        output.write(input.read())
