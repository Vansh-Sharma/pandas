#dropna()

#aixs=0  # drop rows
#aixs=1  # drop columns

import pandas as pd 

data = {
    
    "Name":['ram',None,'ghanshyam','mohan','sohan','rohan','suresh','ramesh'],
    "Age":[23,None,43,26,75,34,23,35],
    "Salary":[50000,None,34000,23000,24000,23000,24500,23000],
    "Performance Score":[80,None,45,99,45,70,80,90]
}

df  = pd.DataFrame(data)
print(df)



# print ("after dropping missing values")

# df.dropna(inplace = True)
# print(df)




#fillna() for filling missing values

#fillna(value, inplace = True)

df['Age'].fillna(df['Age'].mean(),inplace = True)
df['Salary'].fillna(df['Salary'].mean(),inplace = True)

print(df)

