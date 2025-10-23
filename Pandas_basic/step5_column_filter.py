'''
1 - select specific columns
2 - filter rows 
3 - combine multiple conditions

1 - square brackets
2 - boolean conditions

selecting columns
single column - a series
2 - dataframe multiple columns

filtering rows
boolean indexing

#based on a single conditions
filtered_Rows = df[df["Salary"] > 50000]

#combine multiple conditions 
filtered_Rows = df[(df["Column1"] > value) & (df["column2"] < 80000)]

'''

import pandas as pd 

data = {
    
    "Name":['ram','shyam','ghanshyam','mohan','sohan','rohan','suresh','ramesh'],
    "Age":[23,56,43,26,75,34,23,35],
    "Salary":[50000,60000,34000,23000,24000,23000,24500,23000],
    "Performance Score":[80,78,45,99,45,70,80,90]
}

df = pd.DataFrame(data)

print("Sameple Dataframe")

print(df)

print("Name (Single column return series)")
print(df['Name'])


# selecting multiple columns
subset = df[['Name','Age']]
print("subset with Name and Salary")
print (subset)

