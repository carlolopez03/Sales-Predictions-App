import streamlit as st
import pandas as pd
from io import StringIO

#Loading data
@st.cache_data
def load_data():
    df = pd.read_csv('Data/cleaned_sales_predictions_2023.csv')
    return df

df = load_data()

#Title
st.title('Sales Analysis')

#Interactive Pandas dataframe of the prepared dataset from above
st.header('Product Sales Datframe')
st.dataframe(df)

#A button to trigger the display of a dataframe of Descriptive Statistics
st.header('Descriptive Statistics')
show_stats = st.button('Show Descriptive Statistics')
if show_stats:
    stats = df.describe()
    st.dataframe(stats)

#String buffer
buffer = StringIO()

#A button to trigger the display of the summary information (the output of .info)
st.header('Summary Information')
summary = st.button('Show Summary Info')
if summary:
    df.info(buf=buffer)
    info = buffer.getvalue()
    st.text(info)

#A button to trigger the display of the Null values 
st.header('Null Values')
null_button = st.button('Show Null Values')
if null_button:
    df.isna().sum().to_string(buffer)
    nulls = buffer.getvalue()
    st.text(nulls)