'''
NaN (Not a number)
None(for object data types)

isnull()
True - NaN is missing
False - Value is present

'''


import pandas as pd 

data = {
    
    "Name":['ram',None,'ghanshyam','mohan','sohan','rohan','suresh','ramesh'],
    "Age":[23,None,43,26,75,34,23,35],
    "Salary":[50000,None,34000,23000,24000,23000,24500,23000],
    "Performance Score":[80,None,45,99,45,70,80,90]
}

df  = pd.DataFrame(data)
print(df)

print(df.isnull())

print(df.isnull().sum()) # to count number of missing values in each column
