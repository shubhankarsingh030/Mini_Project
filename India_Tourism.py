import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout='wide')

def clean_2017(x):
    if isinstance(x, (int,float)): return x
    elif isinstance(x, str): return np.nan
    return x

# 3.function to load data

st.cache()
def load_dataset1():
    df = pd.read_csv('Data/Country Quater Wise Visitors.csv')
    df = clean_2017(df)
    return df
def load_dataset2():
    df = pd.read_csv('Data/Country Wise Age group.csv')
    df = clean_2017(df)
    return df
def load_dataset3():
    df = pd.read_csv('Data/Country Wise Airport.csv')
    df = clean_2017(df)
    return df
def load_dataset4():
    df = pd.read_csv('Data/Country Wise Gender.csv')
    return df
def load_dataset5():
    df = pd.read_csv('Data/Country Wise Visitors ways.csv')
    df = clean_2017(df)
    return df
def load_dataset6():
    df = pd.read_csv('Data/Country Wise Yearly Visitors.csv')
    return df
def load_dataset7():
    df = pd.read_csv('Data/General Data 2014-2020.csv')
    return df
def load_dataset8():
    df = pd.read_csv('Data/Top 10 state Visit.csv')
    return df

# 4. setup basic UI

st.title("India Tourism 2014-2020")
with st.spinner("Loading Dataset"):                   
    df = load_dataset1()
    df2 = load_dataset2()
    df3 = load_dataset3()
    df4 = load_dataset4()
    df5 = load_dataset5()
    df6 = load_dataset6()
    df7 = load_dataset7()
    df8 = load_dataset8()

if st.sidebar.checkbox("Display Data 1"):
    st.write(df)
if st.sidebar.checkbox("Display Data 2"):
    st.write(df2)
if st.sidebar.checkbox("Display Data 3"):
    st.write(df3)
if st.sidebar.checkbox("Display Data 4"):
    st.write(df4)
if st.sidebar.checkbox("Display Data 5"):
    st.write(df5)
if st.sidebar.checkbox("Display Data 6"):
    st.write(df6)
if st.sidebar.checkbox("Display Data 7"):
    st.write(df7)
if st.sidebar.checkbox("Display Data 8"):
    st.write(df8)

# 5. give user option to select columns

df.set_index('Country of Nationality', inplace=True)
df.dropna(axis=1, how='all', inplace=True)

# graph
st.header("Select a country to visualize")
sel_country = st.selectbox("Country of Nationality", df.index.tolist())
st.subheader(f'Visitors from {sel_country} to India')
countries = df.loc[sel_country]
fig = px.line(countries, x =countries.index, y= countries.values)
st.plotly_chart(fig, use_container_width=True)

st.header("Select multiple countries to visualize")
sel_countries = st.multiselect("Countries", df.index.tolist())
if len(sel_countries)>1:
    st.subheader(f'Comparing countries {", ".join(sel_countries)}')
    df_countries = df.loc[sel_countries].T
    fig = px.line(df_countries, x =df_countries.index, y= sel_countries)
    st.plotly_chart(fig,use_container_width=True)
else:
    st.warning('Please select at least 2 countries for comparison')

st.subheader('Yehh')
fig = px.line(df, df.index,['2014 1st quarter (Jan-March)','2014 2nd quarter (Apr-June)','2014 3rd quarter (July-Sep)','2014 4th quarter (Oct-Dec))'], title='country quarterly wise visiter')
st.plotly_chart(fig, use_container_width=True)

fig = px.bar(df, df.index,'2020 2nd quarter (Apr-June)')
st.plotly_chart(fig, use_container_width=True)