import pandas as pd
import numpy as np
import xlrd
import openpyxl


df = pd.read_csv("datasetfiles/names.csv")
List = list(df["0"])
print(List)
List_media = []
for i in range(len(List)):
    path = "Stats/"+str(List[i])
    df1 = pd.read_csv(path)
    try:
        instagram =  list(df1['Instagram'])[-1]
    except:
        instagram = None
    try:
        facebook = list(df1['Facebook'])[-1]
    except:
        facebook = None
    try:
        twitter = list(df1['Twitter'])[-1]
    except:
        twitter = None
    try:
        linkedIn = list(df1['LinkedIn'])[-1]
    except:
        linkedIn = None
    Countrycode = List[i][13:15]
    List_final = [Countrycode,instagram,facebook,twitter,linkedIn]
    List_media.append(List_final)
print(List_media)

df_media = pd.DataFrame(List_media, columns = ["Countrycode","Instagram","Facebook","Twitter","LinkedIn"])
print(df_media)
df_media.to_csv("datasetfiles/Countrycode_mediadata.csv")

df_county_LL = pd.read_csv('datasetfiles/Country_code and name.csv',delimiter=",")
print(df_county_LL)

df_final = pd.merge(df_county_LL,df_media, on="Countrycode")
print(df_final)

df_final.to_csv("datasetfiles/df_final.csv")

