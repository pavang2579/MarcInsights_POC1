import pandas as pd
df = pd.read_csv("/Users/shivaneeprajapati/PycharmProjects/Download/datasetfiles/names.csv")
List = list(df["0"])
print(List)
List_data = []
#for i in range(len(List)):
path = List[0]
df1 = pd.read_csv(path)
print(df1)
df1["Country code"] = List[13:15]
df2 = pd.DataFrame(df1.tail(1).transpose())
List_data.append(list(df2[12]))
print(List_data)