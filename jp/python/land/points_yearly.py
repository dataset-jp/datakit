import codecs
import csv
import os
import requests

# URL = 'http://ykaku.com/ginkokensaku/ginkositen.zip'
# Download from http://nlftp.mlit.go.jp/
DOWNLOAD_FILE = "L01-29P-48-01.0a.zip"
OUTPUT_DIR       = '/tmp/build'
OUTPUT_FILE_PATH = OUTPUT_DIR + '/output.csv'

# UNZIP data
os.system('unzip ' + DOWNLOAD_FILE + ' -d ' + OUTPUT_DIR)

# CONVERT data into CSV

with open(OUTPUT_FILE_PATH, 'w', newline='') as output:
    spamwriter = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with codecs.open(OUTPUT_DIR + '/L01-29P-2K.csv' , 'r', 'shiftjis') as input:
        try:
            spamreader = csv.reader(input, delimiter=',', quotechar='"')
            for row in spamreader:
                spamwriter.writerow([x.strip() for x in row])
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
