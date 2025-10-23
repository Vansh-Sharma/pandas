'''
1 - columns,row ?
2 - what type of ?
3 - missing data?

info()
method

1 - number of rows and columns
2 - columns
3 - int64 , float64 , object
4 - non null counts
5 - memory usage of the data frame

'''


import pandas as pd 

# df = pd.read_json("sample_Data.json")

# print('Displaying the info of data set')


data = {
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[10,20,30],
    "city":['Nagpur','Mumbai','Delhi']

}

df = pd.DataFrame(data)
print(df.info())