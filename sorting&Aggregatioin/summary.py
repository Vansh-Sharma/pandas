'''
df['column_name'].mean()
df['column_name'].sum()
df['column_name'].average()
df['column_name'].max()
df['column_name'].min()

'''

import pandas as pd 

data= {
    
    "Name":['vansh', 'ram', 'shyam'],
    "Age":[23,6,76],
    "Salary":[70000,50000,40000]

    
}
df = pd.DataFrame(data)

# print(df)


avg_salary = df['Salary'].mean()

print(avg_salary)
