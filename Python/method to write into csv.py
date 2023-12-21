
header=["Name","marks","grade"]
data=[['alex',65,'c'],['brad',75,'b'],['joey',85,'a']]

import csv
file_name="student_data.csv"
with open(file_name,'w',newline="") as file:
    csvwriter=csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(data)
    
#using pandas
import pandas as pd
header=['name','m1 score','m2 score']
data=[['alex',62,80],['brad',75,78],['joe',89,80]]
data=pd.DataFrame(data,columns=header)
data.to_csv('student_marks.csv',index=False)

#using .writelines
header=['name','maths','physics']
data=[['alex',78,80],['brad',80,89],['joey',75,80]]
filename='student_details.csv'
with open(filename,'w') as file:
    for header in header:
        file.write(str(header+', '))
    file.write('\n')
    for row in data:
        for x in row:
            file.write(str(x)+',')
        file.write('\n')
        

#using .dict writer
import csv
with open('stu_data.csv','w',newline='') as file:
    data=[{'name':'alex','m1 score':'80','m2 score':'80'},
          {'name':'brad','m1 score':'70','m2 score':'90'},
          {'name':'joe','m1 score':'80','m2 score':'76'}]
    fieldname=['name','m1 score','m2 score']
    writer=csv.DictWriter(file,fieldnames=fieldname)
    writer.writeheader()
    writer.writerows(data)

