import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import os
st.set_page_config(layout='wide')
for i in os.listdir('Data'):
    st.write(i)

def clean_2014(x):
    if isinstance(x, (int,float)): return x
    elif isinstance(x, str): return np.nan
    return x
def clean_2015(x):
    if isinstance(x, (int,float)): return x
    elif isinstance(x, str): return np.nan
    return x
def clean_2016(x):
    if isinstance(x, (int,float)): return x
    elif isinstance(x, str): return np.nan
    return x
def clean_2017(x):
    if isinstance(x, (int,float)): return x
    elif isinstance(x, str): return np.nan
    return x
def clean_2018(x):
    if isinstance(x, (int,float)): return x
    elif isinstance(x, str): return np.nan
    return x
def clean_2019(x):
    if isinstance(x, (int,float)): return x
    elif isinstance(x, str): return np.nan
    return x
def clean_2020(x):
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
    df = pd.read_csv('Data/Top 10 state Visit.csv')
    return df

# 4. setup basic UI

st.title("INDIA Tourism 2014-2020")
st.subheader("Dataset of Foreign visitors into INDIA from 2014 to 2020")
st.header("About Dataset")
st.subheader("Context")
st.text("This dataset deals with the visitors of foreigners to INDIA.")

("It includes foreigners (not Indian), overseas Indian, and crew members, except for some of the foreign arrivals who are not considered tourists (diplomats, soldiers, permanent residents, visiting cohabitation, and residence).")

("The Indian Government has compiled, analyzed, and provided statistics on foreign tourists visiting Indian and overseas tourists by type.")

("The data materials were prepared for the purpose of utilizing them as basic data for establishing tourism policies and marketing strategies.")

("I created this dataset by rebuilding the data provided by the Indian Government for easy analysis.")
with st.spinner("Loading Dataset"):                   
    df =  load_dataset1()
    df2 = load_dataset2()
    df3 = load_dataset3()
    df4 = load_dataset4()
    df5 = load_dataset5()
    df6 = load_dataset6()
    df7 = load_dataset7()

if st.sidebar.checkbox("Country Quater Wise Visitors"):
    st.write(df)
if st.sidebar.checkbox("Country Wise Age group"):
    st.write(df2)
if st.sidebar.checkbox("Country Wise Airport"):
    st.write(df3)
if st.sidebar.checkbox("Country Wise Gender"):
    st.write(df4)
if st.sidebar.checkbox("Country Wise Visitors ways"):
    st.write(df5)
if st.sidebar.checkbox("Country Wise Yearly Visitors"):
    st.write(df6)
if st.sidebar.checkbox("Top 10 state Visit"):
    st.write(df7)

# 5. give user option to select columns

df.set_index('Country of Nationality', inplace=True)
df.dropna(axis=1, how='all', inplace=True)

df2.set_index('Country of Nationality', inplace=True)

df3.set_index('Country of Nationality', inplace=True)

df4.set_index('Country of Nationality', inplace=True)

df5.set_index('Country of Nationality', inplace=True)

df6.set_index('Country', inplace=True)

df7.set_index('year', inplace=True)




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

st.title("Quaterly Wise Visitors From Diffrent Countries to INDIA")

st.subheader('Country Quarterly Wise Visiter in 2014')
fig = px.line(df, df.index,['2014 1st quarter (Jan-March)','2014 2nd quarter (Apr-June)','2014 3rd quarter (July-Sep)','2014 4th quarter (Oct-Dec))'])
st.plotly_chart(fig, use_container_width=True)

st.subheader('Country Quarterly Wise Visiter in 2015')
df['2015 1st quarter (Jan-March) '] = df['2015 1st quarter (Jan-March) '].apply(clean_2015).astype('float')
cols = ['2015 1st quarter (Jan-March) ','2015 2nd quarter (Apr-June)', '2015 3rd quarter (July-Sep) ', '2015 4th quarter (Oct-Dec) ']
fig2 = px.line(df, df.index, cols)
st.plotly_chart(fig2, use_container_width=True)

st.subheader('Country Quarterly Wise Visiter in 2016')
df['2016 1st quarter (Jan-March) '] = df['2016 1st quarter (Jan-March) '].apply(clean_2016).astype('float')
cols = ['2016 1st quarter (Jan-March) ','2016 2nd quarter (Apr-June)', '2016 3rd quarter (July-Sep) ', '2016 4th quarter (Oct-Dec) ']
fig3 = px.line(df, df.index, cols)
st.plotly_chart(fig3, use_container_width=True)

st.subheader('Country Quarterly Wise Visiter in 2017')
df['2017 1st quarter (Jan-March) '] = df['2015 1st quarter (Jan-March) '].apply(clean_2017).astype('float')
cols = ['2017 1st quarter (Jan-March) ','2017 2nd quarter (Apr-June)', '2017 3rd quarter (July-Sep) ', '2017 4th quarter (Oct-Dec) ']
fig4 = px.line(df, df.index, cols)
st.plotly_chart(fig4, use_container_width=True)

st.subheader('Country Quarterly Wise Visiter in 2018')
df['2018 1st quarter (Jan-March) '] = df['2018 1st quarter (Jan-March) '].apply(clean_2018).astype('float')
cols = ['2018 1st quarter (Jan-March) ','2018 2nd quarter (Apr-June)', '2018 3rd quarter (July-Sep) ', '2018 4th quarter (Oct-Dec) ']
fig5 = px.line(df, df.index, cols)
st.plotly_chart(fig5, use_container_width=True)

st.subheader('Country Quarterly Wise Visiter in 2019')
df['2019 1st quarter (Jan-March) '] = df['2019 1st quarter (Jan-March) '].apply(clean_2019).astype('float')
cols = ['2019 1st quarter (Jan-March) ','2019 2nd quarter (Apr-June)', '2019 3rd quarter (July-Sep) ', '2019 4th quarter (Oct-Dec) ']
fig6 = px.line(df, df.index, cols)
st.plotly_chart(fig6, use_container_width=True)

st.subheader('Country Quarterly Wise Visiter in 2020')
df['2020 1st quarter (Jan-March) '] = df['2020 1st quarter (Jan-March) '].apply(clean_2020).astype('float')
cols = ['2020 1st quarter (Jan-March) ','2020 2nd quarter (Apr-June)', '2020 3rd quarter (July-Sep) ', '2020 4th quarter (Oct-Dec) ']
fig7 = px.line(df, df.index, cols)
st.plotly_chart(fig7, use_container_width=True)

st.title("DISTRIBUTION OF NATIONALITY-WISE Foreign Visitors IN INDIA ACCORDING TO AGE-GROUP")

st.subheader('Age group in 2014')
df2['2014 0-14'] = df2['2014 0-14'].apply(clean_2014).astype('float')
cols = ['2014 0-14',
 ' 2014 15-24',
 ' 2014 25-34',
 '2014 35-44',
 '2014 45-54',
 '2014 55-64',
 '2014 65 AND ABOVE']
fig8 = px.bar(df2, df2.index, cols)
st.plotly_chart(fig8, use_container_width=True)

st.subheader('Age group in 2015')
df2['2015 0-14'] = df2['2015 0-14'].apply(clean_2015).astype('float')
cols = ['2015 0-14',
 ' 2015 15-24',
 ' 2015 25-34',
 '2015 35-44',
 '2015 45-54',
 '2015 55-64',
 '2015 65 AND ABOVE']
fig9 = px.bar(df2, df2.index, cols)
st.plotly_chart(fig9, use_container_width=True)

st.subheader('Age group in 2016')
df2['2016 0-14'] = df2['2016 0-14'].apply(clean_2016).astype('float')
cols = ['2016 0-14',
 ' 2016 15-24',
 ' 2016 25-34',
 '2016 35-44',
 '2016 45-54',
 '2016 55-64',
 '2016 65 AND ABOVE']
fig10 = px.bar(df2, df2.index, cols)
st.plotly_chart(fig10, use_container_width=True)

st.subheader('Age group in 2017')
df2['2017 0-14'] = df2['2017 0-14'].apply(clean_2017).astype('float')
df2[' 2017 15-24'] = df2[' 2017 15-24'].apply(clean_2017).astype('float')
df2[' 2017 25-34'] = df2[' 2017 25-34'].apply(clean_2017).astype('float')
df2['2017 35-44'] = df2['2017 35-44'].apply(clean_2017).astype('float')
df2['2017 45-54'] = df2['2017 45-54'].apply(clean_2017).astype('float')
df2['2017 55-64'] = df2['2017 55-64'].apply(clean_2017).astype('float')
df2['2017 65 AND ABOVE'] = df2['2017 65 AND ABOVE'].apply(clean_2017).astype('float')
cols = ['2017 0-14',
 ' 2017 15-24',
 ' 2017 25-34',
 '2017 35-44',
 '2017 45-54',
 '2017 55-64',
 '2017 65 AND ABOVE']
fig10 = px.bar(df2, df2.index, cols)
st.plotly_chart(fig10, use_container_width=True)


st.subheader('Age group in 2018')
df2['2018 0-14'] = df2['2018 0-14'].apply(clean_2018).astype('float')
cols = ['2018 0-14',
 ' 2018 15-24',
 ' 2018 25-34',
 '2018 35-44',
 '2018 45-54',
 '2018 55-64',
 '2018 65 AND ABOVE']
fig11 = px.bar(df2, df2.index, cols)
st.plotly_chart(fig11, use_container_width=True)

st.subheader('Age group in 2019')
df2['2019 0-14'] = df2['2019 0-14'].apply(clean_2019).astype('float')
cols = ['2019 0-14',
 ' 2019 15-24',
 ' 2019 25-34',
 '2019 35-44',
 '2019 45-54',
 '2019 55-64',
 '2019 65 AND ABOVE']
fig12 = px.bar(df2, df2.index, cols)
st.plotly_chart(fig12, use_container_width=True)

st.subheader('Age group in 2020')
df2['2020 0-14'] = df2['2020 0-14'].apply(clean_2020).astype('float')
cols = ['2020 0-14',
 ' 2020 15-24',
 ' 2020 25-34',
 '2020 35-44',
 '2020 45-54',
 '2020 55-64',
 '2020 65 AND ABOVE']
fig13 = px.bar(df2, df2.index, cols)
st.plotly_chart(fig13, use_container_width=True)

st.title("Foreign Tourist Arrivals IN INDIA THROUGH MAJOR PORTS")

st.subheader("Airports of 2014")
fig14 = px.bar(df3,df3.index,['2014 Delhi (Airport)', ' 2014 Mumbai (Airport)',
       ' 2014 Chennai (Airport)', '2014 Calicut (Airport)',
       '2014 Benguluru (Airport)', '2014 Kolkata (Airport)',
       '2014 Hyderabad (Airport)', '2014 Cochin (Airport) '], title='Country wise airport')
st.plotly_chart(fig14, use_container_width=True)

st.subheader("Airports of 2015")
fig15 = px.bar(df3,df3.index,['2015 Delhi (Airport)', ' 2015 Mumbai (Airport)',
       ' 2015 Chennai (Airport)', '2015 Calicut (Airport)',
       '2015 Benguluru (Airport)', '2015 Kolkata (Airport)',
       '2015 Hyderabad (Airport)', '2015 Cochin (Airport)'], title='Country wise airport')
st.plotly_chart(fig15, use_container_width=True)

st.subheader("Airports of 2016")
df3['2016 Delhi (Airport)'] = df3['2016 Delhi (Airport)'].apply(clean_2016).astype('float')
df3[' 2016 Mumbai (Airport)'] = df3[' 2016 Mumbai (Airport)'].apply(clean_2016).astype('float')
df3[' 2016 Chennai (Airport)'] = df3[' 2016 Chennai (Airport)'].apply(clean_2016).astype('float')
df3['2016 Calicut (Airport)'] = df3['2016 Calicut (Airport)'].apply(clean_2016).astype('float')
df3['2016 Benguluru (Airport)'] = df3['2016 Benguluru (Airport)'].apply(clean_2016).astype('float')
df3['2016 Kolkata (Airport)'] = df3['2016 Kolkata (Airport)'].apply(clean_2016).astype('float')
df3['2016 Cochin (Airport)'] = df3['2016 Cochin (Airport)'].apply(clean_2016).astype('float')
df3['2016 Hyderabad (Airport)'] = df3['2016 Hyderabad (Airport)'].apply(clean_2016).astype('float')
cols = ['2016 Delhi (Airport)', ' 2016 Mumbai (Airport)',
       ' 2016 Chennai (Airport)', '2016 Calicut (Airport)',
       '2016 Benguluru (Airport)', '2016 Kolkata (Airport)',
       '2016 Hyderabad (Airport)', '2016 Cochin (Airport)']
fig16 = px.bar(df3, df3.index, cols, title='Country wise airport')
st.plotly_chart(fig16, use_container_width=True)

st.subheader("Airports of 2017")
df3['2017 Delhi (Airport)'] = df3['2017 Delhi (Airport)'].apply(clean_2017).astype('float')
df3[' 2017 Mumbai (Airport)'] = df3[' 2017 Mumbai (Airport)'].apply(clean_2017).astype('float')
df3[' 2017 Chennai (Airport)'] = df3[' 2017 Chennai (Airport)'].apply(clean_2017).astype('float')
df3['2017 Calicut (Airport)'] = df3['2017 Calicut (Airport)'].apply(clean_2017).astype('float')
df3['2017 Benguluru (Airport)'] = df3['2017 Benguluru (Airport)'].apply(clean_2017).astype('float')
df3['2017 Kolkata (Airport)'] = df3['2017 Kolkata (Airport)'].apply(clean_2017).astype('float')
df3['2017 Cochin (Airport)'] = df3['2017 Cochin (Airport)'].apply(clean_2017).astype('float')
df3['2017 Hyderabad (Airport)'] = df3['2017 Hyderabad (Airport)'].apply(clean_2017).astype('float')
cols = ['2017 Delhi (Airport)', ' 2017 Mumbai (Airport)',
       ' 2017 Chennai (Airport)', '2017 Calicut (Airport)',
       '2017 Benguluru (Airport)', '2017 Kolkata (Airport)',
       '2017 Hyderabad (Airport)', '2017 Cochin (Airport)']
fig17 = px.bar(df3, df3.index, cols,title='Country wise airport')
st.plotly_chart(fig17, use_container_width=True)

st.subheader("Airports of 2018")
cols = ['2018 Delhi (Airport)', ' 2018 Mumbai (Airport)',
       ' 2018 Chennai (Airport)', '2018 Calicut (Airport)',
       '2018 Benguluru (Airport)', '2018 Kolkata (Airport)',
       '2018 Hyderabad (Airport)', '2018 Cochin (Airport)']
fig18 = px.bar(df3,df3.index,cols, title='Country wise airport')
st.plotly_chart(fig18, use_container_width=True)

st.subheader("Airports of 2019")
cols = ['2019 Delhi (Airport)', ' 2019 Mumbai (Airport)',
       ' 2019 Chennai (Airport)', '2019 Calicut (Airport)',
       '2019 Benguluru (Airport)', '2019 Kolkata (Airport)',
       '2019 Hyderabad (Airport)', '2019 Cochin (Airport)']
fig19 = px.bar(df3,df3.index,cols, title='Country wise airport')
st.plotly_chart(fig19, use_container_width=True)

st.subheader("Airports of 2020")
cols = ['2020 Delhi (Airport)', ' 2020 Mumbai (Airport)',
       ' 2020 Chennai (Airport)', '2020 Calicut (Airport)',
       '2020 Benguluru (Airport)', '2020 Kolkata (Airport)',
       '2020 Hyderabad (Airport)', '2020 Cochin (Airport)']
fig20 = px.bar(df3,df3.index,cols, title='Country wise airport')
st.plotly_chart(fig20, use_container_width=True)

st.title("NATIONALITY-WISE GENDER-WISE DISTRIBUTION OF Foreign visitors IN INDIA")

st.subheader("In 2014")
cols = ['2014 Male','2014 Female']
fig21 = px.bar(df4, df4.index,cols,title='Gender wise visitor')
st.plotly_chart(fig21, use_container_width=True)

st.subheader("In 2015")
cols = ['2015 Male','2015 Female']
fig22 = px.bar(df4, df4.index,cols,title='Gender wise visitor')
st.plotly_chart(fig22, use_container_width=True)

st.subheader("In 2016")
cols = ['2016 Male','2016 Female']
fig23 = px.bar(df4, df4.index,cols,title='Gender wise visitor')
st.plotly_chart(fig23, use_container_width=True)

st.subheader("In 2017")
cols = ['2017 Male','2017 Female']
fig24 = px.bar(df4, df4.index,cols,title='Gender wise visitor')
st.plotly_chart(fig24, use_container_width=True)

st.subheader("In 2018")
cols = ['2018 Male','2018 Female']
fig25 = px.bar(df4, df4.index,cols,title='Gender wise visitor')
st.plotly_chart(fig25, use_container_width=True)

st.subheader("In 2019")
cols = ['2019 Male','2019 Female']
fig26 = px.bar(df4, df4.index,cols,title='Gender wise visitor')
st.plotly_chart(fig26, use_container_width=True)

st.subheader("In 2020")
cols = ['2020 Male','2020 Female']
fig27 = px.bar(df4, df4.index,cols,title='Gender wise visitor')
st.plotly_chart(fig27, use_container_width=True)

st.title("FOREIGN VISITORS IN INDIA ACCORDING TO MODE OF TRAVEL")

st.subheader("In 2014")
fig28 =px.bar(df5,df5.index,['2014 AIR',
    '2014 SEA',
    '2014 RAIL',
    '2014 LAND'],title='Visitors ways') 
st.plotly_chart(fig28, use_container_width=True)

st.subheader("In 2015")
fig29 =px.bar(df5,df5.index,['2015 AIR',
    '2015 SEA',
    '2015 RAIL',
    '2015 LAND'],title='Visitors ways') 
st.plotly_chart(fig29, use_container_width=True)

st.subheader("In 2016")
fig30 = px.bar(df5,df5.index,['2016 AIR',
    '2016 SEA',
    '2016 RAIL',
    '2016 LAND'],title='Visitors ways') 
st.plotly_chart(fig30, use_container_width=True)

st.subheader("In 2017")
df5['2017 AIR'] = df5['2017 AIR'].apply(clean_2017).astype('float')
df5['2017 SEA'] = df5['2017 SEA'].apply(clean_2017).astype('float')
df5['2017 RAIL'] = df5['2017 RAIL'].apply(clean_2017).astype('float')
df5['2017 LAND'] = df5['2017 LAND'].apply(clean_2017).astype('float')
fig34 =  px.bar(df5,df5.index,['2017 AIR',
    '2017 SEA',
    '2017 RAIL',
    '2017 LAND'],title='Visitors ways')
st.plotly_chart(fig34, use_container_width=True)


st.subheader("In 2018")
fig31 = px.bar(df5,df5.index,['2018 AIR',
    '2018 SEA',
    '2018 RAIL',
    '2018 LAND'],title='Visitors ways') 
st.plotly_chart(fig31, use_container_width=True)

st.subheader("In 2019")
fig32 = px.bar(df5,df5.index,['2019 AIR',
    '2019 SEA',
    '2019 RAIL',
    '2019 LAND'],title='Visitors ways') 
st.plotly_chart(fig32, use_container_width=True)

st.subheader("In 2020")
fig33 = px.bar(df5,df5.index,['2014 AIR',
    '2020 SEA',
    '2020 RAIL',
    '2020 LAND'],title='Visitors ways') 
st.plotly_chart(fig33, use_container_width=True)

st.title("Country Wise Yearly VIsitors")

st.subheader("2014")
fig34 = px.funnel(df6, df6.index, '2014')
st.plotly_chart(fig34, use_container_width=True)

st.subheader("2015")
fig35 = px.funnel(df6, df6.index, '2015')
st.plotly_chart(fig35, use_container_width=True)

st.subheader("2016")
fig36 = px.funnel(df6, df6.index, '2016')
st.plotly_chart(fig36, use_container_width=True)

st.subheader("2017")
fig37 = px.funnel(df6, df6.index, '2017')
st.plotly_chart(fig37, use_container_width=True)

st.subheader("2018")
fig38 = px.funnel(df6, df6.index, '2018')
st.plotly_chart(fig38, use_container_width=True)

st.subheader("2019")
fig39 = px.funnel(df6, df6.index, '2019')
st.plotly_chart(fig39, use_container_width=True)

st.subheader("2020")
fig40 = px.funnel(df6, df6.index, '2020')
st.plotly_chart(fig40, use_container_width=True)

st.title("Share of Top 10 States/UTs of India in Number of Domestic Tourist Visits")

st.subheader("Foreign Tourist Visit 2014-2020")
fig41 = px.funnel(df7, df7.index, ['top1_ftv', 'top2_ftv','top3_ftv', 'top4_ftv','top5_ftv', 'top6_ftv','top7_ftv', 'top8_ftv','top9_ftv', 'top10_ftv'], title='Tourist visit in India per Year 2014-2020')
st.plotly_chart(fig41, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 1 State")
top1 = df7.groupby('top1_state').sum()
fig42 = px.funnel(top1, top1.index, top1.columns)
st.plotly_chart(fig42, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 2 State")
top2 = df7.groupby('top2_state').sum()
fig43 = px.funnel(top2, top2.index, top2.columns)
st.plotly_chart(fig43, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 3 State")
top3 = df7.groupby('top3_state').sum()
fig44 = px.funnel(top3, top3.index, top3.columns)
st.plotly_chart(fig44, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 4 State")
top4 = df7.groupby('top4_state').sum()
fig45 = px.funnel(top4, top4.index, top4.columns)
st.plotly_chart(fig45, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 5 State")
top5 = df7.groupby('top5_state').sum()
fig46 = px.funnel(top5, top5.index, top5.columns)
st.plotly_chart(fig46, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 6 State")
top6 = df7.groupby('top6_state').sum()
fig47 = px.funnel(top6, top6.index, top6.columns)
st.plotly_chart(fig47, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 7 State")
top7 = df7.groupby('top7_state').sum()
fig48 = px.funnel(top7, top7.index, top7.columns)
st.plotly_chart(fig48, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 8 State")
top8 = df7.groupby('top8_state').sum()
fig49 = px.funnel(top8, top8.index, top8.columns)
st.plotly_chart(fig49, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 9 State")
top9 = df7.groupby('top9_state').sum()
fig50 = px.funnel(top9, top9.index, top9.columns)
st.plotly_chart(fig50, use_container_width=True)

st.subheader("Foreign Tourist Visit in Top 10 State")
top10 = df7.groupby('top10_state').sum()
fig51 = px.funnel(top10, top10.index, top10.columns)
st.plotly_chart(fig51, use_container_width=True)








