import csv

dataset1 = []
dataset2 = []

with open("scrapper.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("scrapper_1.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

header1=dataset1[0]
planet_data1=dataset1[1:]

header2=dataset2[0]
planet_data2=dataset2[1:]

headers = header1 + header2
planet_data = []

for i, dr in enumerate(planet_data1):
    planet_data.append(planet_data1[i]+planet_data2[i])

with open("final.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)