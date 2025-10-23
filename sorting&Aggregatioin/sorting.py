#sorting data 
#SORTING DATA 1 COLUMN sort_values()
#df.sort_values(by="Column_Name",ascending/descending = True/False, inplace = True/False)
# ascending = True  # for ascending order
# descending = False # for descending order

import pandas as pd 

data= {
    
    "Name":['vansh', 'ram', 'shyam'],
    "Age":[23,6,76],
    "Salary":[70000,50000,40000]

    
}
df = pd.DataFrame(data)

print(df)

# #sorting by single column

# df.sort_values(by="Age",ascending=True, inplace= True)
# print("sorted age by Descending order ")

# print(df)

#sorting by multiple columns
print("sorting by multiple columns")

df.sort_values(by=["Age","Salary"],ascending=[True,False], inplace= True)
print(df)

