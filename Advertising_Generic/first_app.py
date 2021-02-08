import pandas as pd
import streamlit as st
import json



data = pd.read_csv('/Users/shivaneeprajapati/PycharmProjects/Download/datasetfiles/df_final.csv',index_col=None)
print(data.head())
data = pd.DataFrame(data).fillna(0)
data = data.drop(data.columns[0],axis=1)
print(data.head())

#data = data.to_dict('index')
#print(data)

#   print({'Countrycode': data[i],'Country_name':data[3],'latitude': float(data[1]),'longitude':float(data[2]), 'values': data[4:8]})

List1 = list(data["Countrycode"])
List2 = list(data["latitude"])
List3 = list(data["longitude"])
List4 = list(data["Country_name"])
List5 = list(data["Instagram"])
List6 = list(data["Facebook"])
List7 = list(data["Twitter"])
List8 = list(data["LinkedIn"])

for i in range(len(data)):
    print({'latitude':List2[i],'longitude':List3[i], 'values':[List6[i],List5[i],List7[i],List8[i]],'name':List4[i] }, ",")
