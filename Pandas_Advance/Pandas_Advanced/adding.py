import pandas as pd 

data = {
    
    "Name":['ram','shyam','ghanshyam','mohan','sohan','rohan','suresh','ramesh'],
    "Age":[23,56,43,26,75,34,23,35],
    "Salary":[50000,60000,34000,23000,24000,23000,24500,23000],
    "Performance Score":[80,78,45,99,45,70,80,90]
}

df  = pd.DataFrame(data)
print(df)
#square brackets df["column_Name"] = some_Data

print("Adding a new column Bonus which is 10 % of salary")

df['Bonus'] = df['Salary']*0.1

print(df)


#using insert() more usefull in company 


# df.insert(loc, "column_Name", some_data)
df.insert(2, "Employee_ID", [23,54,23,64,76,43,23,54])

print(df)

