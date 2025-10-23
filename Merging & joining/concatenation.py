'''

vertically 
horizontly

'''

import pandas as pd 

#region1

df_Region1 = pd.DataFrame({
    'CustomerID': [1,2],
    'Name':['Gopal','Raju']
})

#region2

df_Region2 = pd.DataFrame({
    'CustomerID': [3,4],
    'Name':['gaju','guddu']
})

# concatenate vertically 

df_concat = pd.concat([df_Region1,df_Region2],axis =0 , ignore_index = True)
df_concat = pd.concat([df_Region1,df_Region2],axis =1 , ignore_index = True)


print(df_concat)

