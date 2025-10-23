#read data from CSV file into a dataframe

# import pandas as pd 


# df = pd.read_csv("sales_data_sample.csv",encoding ="latin1")
# df = pd.read_excel("SampleSuperstore.xlsx")
# print(df)


#read data from json file into a dataframe
import pandas as pd 

df = pd.read_json("sample_Data.json")
print(df)


