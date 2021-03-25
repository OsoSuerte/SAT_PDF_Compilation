from bs4 import BeautifulSoup
import requests
import pandas as pd
import tabula
import csv
import glob, os
from urllib.parse import urljoin

url = "https://reports.collegeboard.org/sat-suite-program-results"  # url for website with target PDFS

# Location to store PDFs. If there is no such folder, the script will create one
folder_location = r'C:\Coding\Pycharm projects\SATS\pdfs'
if not os.path.exists(folder_location):os.mkdir(folder_location)

# Locate, download and rename the pdf files using a unique portion of each link.
response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")
for link in soup.select("a[href$='.pdf']"):
    filename = os.path.join(folder_location,link['href'].split('-')[-6] +'.pdf')
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)

# Iterates through all downloaded PDFs and converts a selected portion of each to an individual .csv file
all_pdf = []
os.chdir("C:\Coding\Pycharm projects\SATS\pdfs")
for file in glob.glob("*.pdf"):
    all_pdf.append(file)
for pdf in all_pdf:
    tabula.convert_into(os.path.join(r"C:\Coding\Pycharm projects\SATS\pdfs", pdf), os.path.join(r"C:\Coding\Pycharm projects\SATS\csvs", pdf.split('.')[0] + '.csv'), output_format="csv", pages='4')

# lines 32-62 iterates through csv files to clean data and create a dictionary with all data.
all_csv = []
os.chdir("C:\Coding\Pycharm projects\SATS\csvs")
for file in glob.glob("*.csv"):
    all_csv.append(file)

all_states = {}  # Dictionary containing all cleaned data
for each in all_csv:
    if each == 'group.csv':  # 'group' is not used for this part of project.
        continue
    state = str(each.split('.')[0])
    temp = []
    with open(os.path.join(r"C:\Coding\Pycharm projects\SATS\csvs", each)) as data_csv:
        data = csv.reader(data_csv)
        for i in data:
            if i[0] == '':
             continue
            if i[1] == 'Test Takers':
                continue
            temp.append(i)
    stats = []
    statdic = {}
    current = {}
    #temp = list(filter(None, stats))
    #list(filter(None, i))  temp =
    for i in temp:
        ele = [item for item in i if item != '']
        stats.append(ele)

    #print(stats)
    for i in stats: # used to select desired data individual csv files combined for dictionary
        try:
            statdic[i[0]] = {'group': i[0], 'total': i[1].split()[0], 'percent_of_test_takers': i[1].split()[-1], 'total_mean_score': i[2], 'erw_mean_score': i[3], 'math_mean_score': i[4], 'met_both_benchmarks': i[5], 'met_erw_bench_mark': i[6].split(' ')[0], 'met_math_bench_mark': i[6].split(' ')[-1], 'met_niether_bench_mark': i[7]}
        except: continue # could be worked out but is currently used if a PDF has format discrepancies
        current.update(statdic)
        try:
            all_states.update({state: current})
        except: pass

al = all_states['montana']['Total'] #['total_mean_score']
print(al)
# Used to export data to two files for further use. One is formatted as a dictionary other as DataFrame
with open(r'C:\Coding\Pycharm projects\SATS\dict_output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in all_states.items():
       writer.writerow([key, value])
all_states_df = pd.DataFrame(all_states)
all_states_df.to_csv(r'C:\Coding\Pycharm projects\SATS\dataframe_output.csv', index = False)