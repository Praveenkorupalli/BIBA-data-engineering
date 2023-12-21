import csv
rows=[]
with open("business-financial-data-september-2023-quarter.csv",'r') as file:
    csvreader = csv.reader(file)
    header=next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
