import codecs
import csv
import os
import requests
import zipfile

# Download from http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-L01-v2_3.html
DOWNLOAD_FILE    = './raw_data/L01-29P-48-01.0a.zip'
OUTPUT_FILE_PATH = '/src/data/output.csv'

# UNZIP data
with zipfile.ZipFile(DOWNLOAD_FILE, 'r') as zip_ref:
    zip_ref.extractall('/tmp')

# CONVERT data into CSV

with open(OUTPUT_FILE_PATH, 'w', newline='') as output:
    spamwriter = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with codecs.open('/tmp/L01-29P-2K.csv' , 'r', 'shiftjis') as input:
        try:
            spamreader = csv.reader(input, delimiter=',', quotechar='"')
            for row in spamreader:
                spamwriter.writerow([x.strip() for x in row])
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
