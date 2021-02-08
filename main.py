# Advertisement related code
import pandas as pd
df = pd.read_csv("Advertising_Generic/datasetfiles/df_final.csv")
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
    import plotly.express as px
    # fig = px.bar(df_plot, x="Social Media", y="Percentage Users", title="Social Media Analysis - " + country)
    fig = px.pie(df_plot, values ="Percentage Users", names ="Social Media", title="Social Media Analysis - " + country)
    return fig
# competitor analysis
def searchfunction(query):
    from googlesearch import search
    import pandas as pd
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    #query = "Top Global Edtech Companies"
    list_of_urls = []
    for j in search(query, tld="co.uk", num=5, stop=5, pause=2):
        list_of_urls.append(j)
    print(list_of_urls)
    df = pd.DataFrame(list_of_urls, columns=["Source"])

    def make_clickable(link):
        # target _blank to open new window
        # extract clickable text to display for your link
        return f'<a target="_blank" href="{link}">{link}</a>'

    # link is the column with hyperlinks
    df['Source'] = df['Source'].apply(make_clickable)
    df = df.to_html(escape=False)
    return df
# FRONT END APPLICATION
import streamlit as st
import base64
import pandas as pd
from PIL import Image
import requests
import streamlit.components.v1 as components
main_bg = "images/images-bg1.png"
main_bg_ext = "png"
side_bg = "images/images-2.jpg"
side_bg_ext = "jpg"
main_bg1 = "images/template.png"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.image("images/company.png",width = 250)
st.sidebar.markdown(" ** MARC Insights - Visualisation Panel **")
st.sidebar.image("images/mainbg.png",width=300)
username = st.sidebar.text_input("Username", "Enter your username")
password = st.sidebar.text_input("Password", "Enter the password")
if st.sidebar.checkbox("Login"):
    if username == "Robokalam" and password == "20202020":
        st.sidebar.success("Your login is successful \n scroll down for dashboard options")
        dropdown = st.sidebar.selectbox("Select a Vertical",["Dropdown to select","Market Research","Advertising & Promotions","Risk Analysis","Competitor Analysis"])
        # Market Research
        if dropdown == "Market Research":
            st.markdown(
                f"""
                <style>
                .reportview-container {{
                    background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg1, "rb").read()).decode()});
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
            template = """
               <div style = "background-color : blue; padding : 1px;">
               <h2 style = "color:white;text-align:center;"> Market Research Insights </h2>
               </div>
               """
            st.markdown(template, unsafe_allow_html=True)
            Research = st.sidebar.radio("Select the Article",["Choose one","RS-online UK","Grand View Review"])
            if Research == "RS-online UK":
                st.sidebar.write("Select the view")
                if st.sidebar.checkbox("Market Stats"):
                    st.success("Here is your report of stats - use slider to view next")
                    df = pd.read_csv("Market Research/report_imageurls_rsonline.csv",index_col= False)
                    List = df['image_urls'].to_list()
                    def display(i):
                        return Image.open(requests.get(List[i], stream=True).raw)
                    x = st.slider("Move slider to view stats",0,11)
                    st.image(display(x),width = 700)
                if st.sidebar.checkbox ("Executive Summary"):
                    with open("Market Research/report_rsonline.txt","r") as file:
                        summary = file.read()
                        st.success(summary)
            if Research == "Grand View Review":
                st.sidebar.write("Select the view")
                if st.sidebar.checkbox ("Executive Summary"):
                    with open("Market Research/report_grandviewreview.txt","r") as file:
                        summary = file.read()
                        st.success(summary)
                if st.sidebar.checkbox("Market Stats"):
                    st.success("Here is your report of stats - use slider to view next")
                    df = pd.read_csv("Market Research/report_grandviewreview.csv")
                    df = df.to_html(escape=False)
                    st.write(df,unsafe_allow_html=True)
        if dropdown == "Advertising & Promotions":
            st.markdown(
                f"""
                <style>
                .reportview-container {{
                    background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg1, "rb").read()).decode()});
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
            template = """
               <div style = "background-color : blue; padding : 1px;">
               <h2 style = "color:white;text-align:center;"> Advertisements and Promotions Insights </h2>
               </div>
               """
            st.markdown(template, unsafe_allow_html=True)
            Research = st.sidebar.radio("Select type of Insights",["Choose one","Specific","Generic"])
            if Research == "Specific":
                st.sidebar.write("Select the view")
                if st.sidebar.checkbox("Facebook : Summary Insights"):
                    st.success("Here is the Facebook summary stats")
                    st.image("Advertising_specific/images/Facebook: Reach & Impression.png",width = 700)
                if st.sidebar.checkbox("Facebook : Reach and Impressions Insights"):
                    st.success("Here is the Facebook Reach and Impression stats")
                    st.image("Advertising_specific/images/Facebook: Reach & Impression.png",width = 700)
                if st.sidebar.checkbox("Instagram : Summary Insights"):
                    st.success("Here is the Instagram summary stats")
                    st.image("Advertising_specific/images/Instagram: Summary.png",width = 700)
            if Research == "Generic":
                dropdown1 = st.sidebar.selectbox("Select the Country",name)
                i = name.index(dropdown1)
                st.plotly_chart(plot(i))
        if dropdown == "Risk Analysis":
            st.markdown(
                f"""
                <style>
                .reportview-container {{
                    background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg1, "rb").read()).decode()});
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
            template = """
               <div style = "background-color : blue; padding : 1px;">
               <h2 style = "color:white;text-align:center;"> Risk Analysis </h2>
               </div>
               """
            st.markdown(template, unsafe_allow_html=True)
            HtmlFile = open("Risk_Analysis/10.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read()
            components.html(source_code, width=700, height=800, scrolling=True)
        if dropdown == "Competitor Analysis":
            st.markdown(
                f"""
                <style>
                .reportview-container {{
                    background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg1, "rb").read()).decode()});
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
            template = """
               <div style = "background-color : blue; padding : 1px;">
               <h2 style = "color:white;text-align:center;"> Competitor Analysis </h2>
               </div>
               """
            st.markdown(template, unsafe_allow_html=True)
            Research = st.sidebar.radio("Select type of Insights", ["Choose one", "know your competitors", "Check the trend"])
            if Research == "know your competitors":
                m = st.text_input("Enter the search term", "Top Global Edtech Companies")
                x = searchfunction(m)
                st.write(x, unsafe_allow_html=True)


