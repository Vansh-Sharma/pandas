'''
1- sum()
2- mean()
3- count()
4- min()
5- max()
6- std()


'''


'''

logic behind this 

df.grouped("Age")
age = 22>[56000]
age = 23[70000,40000] = 1100000
age = 45[50000,23000] = 73000
age = 76[40000,45000] = 85000

'''


import pandas as pd 

data= {
    
    "Name":['vansh', 'ram', 'shyam','rishu','vishnu','narun','sihsu'],
    "Age":[23,45,23,76,45,76,22],
    "Salary":[70000,50000,40000,40000,23000,45000,56000]

    
}
df = pd.DataFrame(data)

print(df)
#single column

grouped = df.groupby('Age')["Salary"].sum()
print(grouped)





#multiple columns
grouped = df.groupby(['Age','Name'])["Salary"].sum()
print(grouped)


