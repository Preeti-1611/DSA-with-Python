import numpy as np
import pandas as pd

path = r"C:\Users\PREETI NAGARALE\Downloads\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv"
dataframe = pd.read_csv(path, encoding="latin1")

print(dataframe)

print(dataframe.columns)
print(dataframe.head(1)) #one row info is provided head(1) gives 1 row 
print(dataframe.shape)




