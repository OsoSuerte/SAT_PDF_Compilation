from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import PyPDF2
import pdfminer
import tabula
import csv
import sqlite3
import glob, os
from pdfminer import high_level
import os
from urllib.parse import urljoin


url = "https://reports.collegeboard.org/sat-suite-program-results"

#If there is no such folder, the script will create one automatically
folder_location = r'C:\Coding\Pycharm projects\SATS\pdfs'
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")
for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('-')[-6] +'.pdf')
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)


all_pdf = []
os.chdir("C:\Coding\Pycharm projects\SATS\pdfs")
for file in glob.glob("*.pdf"):
    all_pdf.append(file)

# convert PDF into CSV file
for pdf in all_pdf:

    tabula.convert_into(os.path.join(r"C:\Coding\Pycharm projects\SATS\pdfs", pdf), os.path.join(r"C:\Coding\Pycharm projects\SATS\csvs", pdf.split('.')[0] + '.csv'), output_format="csv", pages='4')


all_csv = []
os.chdir("C:\Coding\Pycharm projects\SATS\csvs")
for file in glob.glob("*.csv"):
    all_csv.append(file)

all_states = {

}

for each in all_csv:

    if each == 'group.csv':
        continue
    if each == 'iowa.csv':
        continue
    state = str(each.split('.')[0])

    stats = []
    with open(os.path.join(r"C:\Coding\Pycharm projects\SATS\csvs", each)) as data_csv:
        data = csv.reader(data_csv)

        for x in data:
            if x[0] == '':
             continue
            if x[1] == 'Test Takers':
                continue
            stats.append(x)

    statdic = {
    }
    current = {}
    for i in stats:
        try:
            statdic[i[0]] = {'group': i[0], 'total': i[1].split()[0], 'percent_of_test_takers': i[1].split()[-1], 'total_mean_score': i[2], 'erw_mean_score': i[3], 'math_mean_score': i[4], 'met_both_benchmarks': i[5], 'met_erw_bench_mark': i[6].split(' ')[0], 'met_math_bench_mark': i[6].split(' ')[-1], 'met_niether_bench_mark': i[7]}

        except: continue

        current.update(statdic)

        try:
            all_states.update({state: current})
        except: pass

with open(r'C:\Coding\Pycharm projects\SATS\fin.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in all_states.items():
       writer.writerow([key, value])
all_states_df = pd.DataFrame(all_states)
all_states_df.to_csv(r'C:\Coding\Pycharm projects\SATS\findf.csv', index = False)

