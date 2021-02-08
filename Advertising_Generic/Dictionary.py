import pandas as pd
import numpy as np
import xlrd
import openpyxl

# importing the file that has list of countries and their latitudes and longitudes
df = pd.read_csv('Advertising_Generic/datasetfiles/lattitude_longitude.csv')
                 #columns = ["Country_name","Lattitude_Longitude"])
#print(df)
df1 = pd.read_excel('Advertising_Generic/datasetfiles/Codes_EXCEL.xlsx')

df = pd.DataFrame(df)
#print(df)
print('*********** New DF renamed : ***********')
df = df.rename(columns={'Australia': 'Country_name'})
print(df.head(2))

print('******** Country_name and Country code : ********')
print(df1.head(2))
print('********  New DF merged : **********')

df2 = pd.merge(df, df1)
print(df2)

