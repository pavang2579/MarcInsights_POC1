from os import walk
mypath = "./Stats"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
print(f)
import pandas as pd
df = pd.DataFrame(f)
#print(df)
#df.to_csv('datasetfiles/names.csv')