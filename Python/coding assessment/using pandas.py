#reading a file using pandas

import pandas as pd
data=pd.read_csv('annual_enterprise.csv')
print(data)

print(data.columns)

print(data.industry_name_ANZSIC)

#writing a file using pandas

header=['Name',"profeesion",'salary']
data=[['Virat','cricket',3000000],['ronaldo','football',5000000,],['viswanath anand','chess',200000]]
data=pd.DataFrame(data,columns=header)
data.to_csv('athelets.csv',index=False)