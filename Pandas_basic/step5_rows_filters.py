import pandas as pd 

data = {
    
    "Name":['ram','shyam','ghanshyam','mohan','sohan','rohan','suresh','ramesh'],
    "Age":[23,56,43,26,75,34,23,35],
    "Salary":[50000,60000,74000,83000,24000,23000,24500,23000],
    "Performance Score":[80,78,45,99,45,70,80,90]
}

df = pd.DataFrame(data)



#filter rows based on single condition 
# high_salary = df[df['Salary']>50000]

# print("person over 50000 salary")
# print(high_salary)


#filter rows based on multiple conditions 

# high_salary = df[(df['Salary']>50000) & (df['Age']> 30)]

# print("person over 50000 salary and age more than 30 ")

# print(high_salary)

# using OR condition

filtered_or = df[(df['Age']>35) | (df['Performance Score']>70)]

print(filtered_or)
