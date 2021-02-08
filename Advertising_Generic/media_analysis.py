import pandas as pd
df = pd.read_csv("datasetfiles/df_final.csv")
df1 = df.drop("Unnamed: 0",axis=1)
print(df1)
Row_list = []
# Iterate over each row
for index, rows in df1.iterrows():
    # Create list for the current row
    my_list = [rows.Country_name, rows.Instagram, rows.Facebook, rows.Twitter, rows.LinkedIn]

    # append the list to the final list
    Row_list.append(my_list)
name = list(df1["Country_name"])
def plot(i):
    country = name[i]
    x_axis = ["Instagram", "Facebook", "Twitter", "Linkedin"]
    y_axis = Row_list[i][1:5]
    df_plot = pd.DataFrame(list(zip(x_axis, y_axis)), columns=["Social Media", "Percentage Users"])
    print(df_plot)
    import plotly.express as px
    fig = px.bar(df_plot, x="Social Media", y="Percentage Users", title="Social Media Analysis - " + country)
    fig.show()
i = name.index("Angola")
plot(i)