#pd.merge(df1,df2, on= 'column_name', how = 'type of join')

import pandas as pd 


# custumer dataframe

df_customer= pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['vansh','vishnu','rishi']
    
})

#order dataframe

df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[230,340,450]
})

#merge 

df_merged1 = pd.merge(df_customer,df_orders,on = 'CustomerID',how = 'inner')
df_merged2 = pd.merge(df_customer,df_orders,on = 'CustomerID',how = 'outer')
df_merged3 = pd.merge(df_customer,df_orders,on = 'CustomerID',how = 'left')
df_merged4 = pd.merge(df_customer,df_orders,on = 'CustomerID',how = 'right')

print(df_merged1)
print('hello')
print(df_merged2)
print("world")
print(df_merged3)
print('hy')
print(df_merged4)
