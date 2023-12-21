import csv
with open("business-financial-data-september-2023-quarter.csv",'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)