'''

use cases for interpolation:


1- timer series data 
2- numeric data with trends 
3- avoid dropping rows 

'''

import pandas as pd 

data = {

    
    "Time":[1,2,3,4,5],
    "Value":[10,20,None,None,50]
}

df = pd.DataFrame(data)

print(df)

df['Value'] = df['Value'].interpolate(method='linear')

print("After interpolation")
print(df)


