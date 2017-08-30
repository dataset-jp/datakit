import codecs
import csv
from datetime import datetime
import os
import requests
import zipfile

# '2014-12-23' => '1419292800'
def str2unixtime(s):
    try:
        datetime.strptime(s, '%Y-%m-%d').strftime("%s")
    except ValueError:
        print('ValueError')
        ''

# Please update your quandl key
URL              = 'https://www.quandl.com/api/v3/datasets/CUR/JPY.csv?api_key=mCkqGja_5orzQJxF5RhQ'
OUTPUT_FILE_PATH = '/src/data/output.csv'

# GET raw data
r = requests.get(URL)
with open('/tmp/raw.csv', 'wb') as file:
    file.write(r.content)

# CONVERT data into CSV along with converting date to unixtime
with open(OUTPUT_FILE_PATH, 'w', newline='') as output:
    spamwriter = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with codecs.open('/tmp/raw.csv', 'r') as input:
        spamreader = csv.reader(input, delimiter=',', quotechar='"')
        for row in spamreader:
            spamwriter.writerow([str2unixtime(row[0]), row[1]])
