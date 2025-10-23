'''
1- how big is your dataset
2- what are the names of columns

'''

import pandas as pd 

data = {
    
    "Name":['ram','shyam','ghanshyam','mohan','sohan','rohan','suresh','ramesh'],
    "Age":[23,56,43,26,75,34,23,35],
    "Salary":[50000,60000,340000,230000,240000,230000,234500,23000],
    "Performance Score":[80,78,45,99,45,70,80,90]
}

df = pd.DataFrame(data)
print(df)

print(f'Shape :{df.shape}')
print(f'Columns :{df.columns}')
