import pandas as pd 

data = {
    
    "Name":['ram','shyam','ghanshyam','mohan','sohan','rohan','suresh','ramesh'],
    "Age":[23,56,43,26,75,34,23,35],
    "Salary":[50000,60000,34000,23000,24000,23000,24500,23000],
    "Performance Score":[80,78,45,99,45,70,80,90]
}


df = pd.DataFrame(data)

print(df)

# #loc[]
# # df.loc[row_index, "Column_Name"] = new_value
# df.loc[3, "Salary"] = 59000
# print(df)

# df.to_json("file.json",index=False)



# updating multiple values at once or  updating entire data


df['Salary'] = df['Salary'] *1.05

print(df)
