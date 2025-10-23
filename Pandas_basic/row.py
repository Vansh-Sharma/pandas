#head()
#tail()

import pandas as pd 
df = pd.read_json("sample_Data.json")

print(df.head(10))
print('Display first 10 rows')


print(df.tail(10))
print('Display last 10 rows')

