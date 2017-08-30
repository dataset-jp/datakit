import codecs
import csv
import os
import requests

URL = 'http://ykaku.com/ginkokensaku/ginkositen.zip'
OUTPUT_DIR       = '/src/data'
OUTPUT_FILE_PATH = OUTPUT_DIR + '/output.csv'

# GET raw data
r = requests.get(URL)
with open(OUTPUT_DIR + '/raw.zip', 'wb') as file:
    file.write(r.content)

# UNZIP data
os.system('unzip ' + OUTPUT_DIR + '/raw.zip -d ' + OUTPUT_DIR)

# CONVERT data into CSV
with open(OUTPUT_FILE_PATH, 'w', newline='') as output:
    spamwriter = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with codecs.open(OUTPUT_DIR + '/ginkositen.txt', 'r', 'shiftjis') as input:
        spamreader = csv.reader(input, delimiter=',', quotechar='"')
        for row in spamreader:
            spamwriter.writerow([x.strip() for x in row])
