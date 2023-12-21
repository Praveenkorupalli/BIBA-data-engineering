import csv

file=open('Salary_Data.csv')
type(file)

csvreader=csv.reader(file)

header=[]
header=next(csvreader)
print(header)

rows=[]
for row  in csvreader:
    rows.append(row)
print(rows)

file.close()

import csv
rows=[]
with open("Salary_Data.csv",'r') as file:
    csvreader = csv.reader(file)
    header=next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)


#using .readlines() method
"""""""""
with open('Salary_Data.csv') as file:
    content=file.readlines()
header = content[:1]
rows=content[1:]
print(header)
print(rows)
"""""""""