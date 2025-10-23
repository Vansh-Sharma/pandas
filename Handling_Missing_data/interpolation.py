'''
linear

1- preserve data integrity 
2- smooth trends
3- avoid data loss 

interpolate()

 methods 
 
 linear, polynomial, spline, time, index, nearest, zero, quadratic, cubic
 
'''

import pandas as pd 

data = {
    
    "Name":['ram','vansh','ghanshyam','mohan','sohan','rohan','suresh','ramesh'],
    "Age":[23,None,43,26,75,34,23,35],
    "Salary":[50000,None,34000,23000,24000,23000,24500,23000],
    "Performance Score":[80,None,45,99,45,70,80,90]
}

df  = pd.DataFrame(data)
print(df)