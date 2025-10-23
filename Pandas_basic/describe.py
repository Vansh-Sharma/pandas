#step - 1 sample data frame

import pandas as pd 

data = {
    
    "Name":['ram','shyam','ghanshyam','mohan','sohan','rohan','suresh','ramesh'],
    "Age":[23,56,43,26,75,34,23,35],
    "Salary":[50000,60000,34000,23000,24000,23000,24500,23000],
    "Performance Score":[80,78,45,99,45,70,80,90]
}

df = pd.DataFrame(data)
print("sameple Dataframe")
print(df)
print('Descriptive Statistics')
print(df.describe())
