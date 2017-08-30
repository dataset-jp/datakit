import codecs
import csv
import os
import requests
import xlrd
import numpy as np


# Download (参考表)全国人口の推移 from http://www.e-stat.go.jp/SG1/estat/List.do?lid=000001189063
DOWNLOAD_FILE    = "./raw_data/05k2-2.xls"
OUTPUT_FILE_PATH = '/src/data/output.csv'

wb = xlrd.open_workbook(DOWNLOAD_FILE)
sh = wb.sheet_by_index(0)
rows = []
for rx in range(sh.nrows):
    if 13 <= rx <= 19:
        rows.append(sh.row(rx))

rows = [[x.value for x in row] for row in rows]

# CONVERT data into CSV
with open(OUTPUT_FILE_PATH, 'w', newline='') as output:
    spamwriter = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['年', '月初人口', '増減数', '増減率', '出生児数', '死亡者数', '自然増減', '入国者数', '出国者数', '社会増減'])
    for row in rows:
        spamwriter.writerow([row[i] for i in [1,3,5,6,7,8,9,10,11,12]])
