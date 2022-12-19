# 1. import libraries

import numpy as np
import pandas as pd
import plotly.express as px # simple graphs
import plotly.graph_objects as go # complex graphs
import streamlit as st

# 2. create function to clean data

def clean_2017(x):
    if isinstance(x, (int,float)): return x
    elif isinstance(x, str): return np.nan
    return x

# 3. create function to load data

st.cache()                                # helps to make the app faster
def load_dataset1():
    df = pd.read_csv('Mini_Project/Data/Country Quater Wise Visitors.csv')
    df = clean_2017(df)
    return df
#def load_dataset2():
    df = pd.read_csv('Mini_Project/Data/Country Wise Age group.csv')
    df = clean_2017(df)
    return df
#def load_dataset3():
    df = pd.read_csv('Mini_Project/Data/Country Wise Airport.csv')
    df = clean_2017(df)
    return df
#def load_dataset4():
    df = pd.read_csv('Mini_Project/Data/Country Wise Gender.csv')
    return df
#def load_dataset5():
    df = pd.read_csv('Mini_Project/Data/Country Wise Visitors ways.csv')
    df = clean_2017(df)
    return df
#def load_dataset6():
    df = pd.read_csv('Mini_Project/Data/Country Wise Yearly Visitors.csv')
    return df
#def load_dataset7():
    df = pd.read_csv('Mini_Project/Data/General Data 2014-2020.csv')
    return df
#def load_dataset8():
    df = pd.read_csv('Mini_Project/Data/Top 10 state Visit.csv')
    return df

# 4. setup basic UI

st.title("India Tourism 2014-2020")
with st.spinner("Loading Dataset"):                        # show a loading message
    df = load_dataset1()
#    df = load_dataset2()
#    df = load_dataset3()
#    df = load_dataset4()
#    df = load_dataset5()
#    df = load_dataset6()
#    df = load_dataset7()
#    df = load_dataset8()

if st.sidebar.checkbox("Show full dataframe"):     # show raw data if checkbox is checked
    st.write(df)

# 5. give user option to select columns

st.sidebar.header("Select a country to visualize")
df.set_index('Country of Nationality', inplace=True)
df.dropna(axis=1, how='all', inplace=True)
df
countries = df.index.tolist()
sel_country = st.sidebar.selectbox("Country of Nationality", countries)

years = list(range(2014, 2020))

# graph
st.header(f'visitors from {sel_country} to India')
countries = df.loc[sel_country, years ] # subset
fig = px.line(df, x =df.index, y= df.values)
st.plotly_chart(fig)

st.sidebar.header("Select multiple countries to visualize")
sel_countries = st.sidebar.multiselect("Countries", countries)
if len(sel_countries)>1:
    st.header(f'Comparing countries {", ".join(sel_countries)}')
    df_countries = df.loc[sel_countries, years].T # subset
    fig = px.line(df, x =df.index, y= df.values)
    st.plotly_chart(fig)
else:
    st.warning('Please select at least 2 countries for comparison')


# 6. give user option display graphs

# 0. Run the app run the command below
# streamlit run Mini_Project/India_Tourism.py