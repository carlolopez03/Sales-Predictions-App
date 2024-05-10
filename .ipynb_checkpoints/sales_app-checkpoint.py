import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import plotly.express as px
import functions as fn

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

#Columns for plotting
columns = df.columns
target = 'Item_Outlet_Sales'
features = [col for col in columns if col != target]

#Selectbox for columns
eda_column = st.selectbox('Column to Explore', columns, index=None)

#Function for models
if eda_column:
    if df[eda_column].dtype == 'object':
        fig = fn.explore_categorical(df, eda_column)
    else:
        fig = fn.explore_numeric(df, eda_column)

#Plotting columns
    st.header(f'Display Plots for {eda_column}')
    st.pyplot(fig)

## Select box for features vs target
feature = st.selectbox('Compare Feature to Target', features, index=None)

## Conditional: if feature was chosen
if feature:
    ## Check if feature is numeric or object
    if df[feature].dtype == 'object':
        comparison = df.groupby('Item_Outlet_Sales').count()
        title = f'Count of {feature} by {target}'
    else:
        comparison = df.groupby('Item_Outlet_Sales').mean()
        title = f'Mean {feature} by {target}'

    ## Display appropriate comparison
    pfig = px.bar(comparison, y=feature, title=title)
    st.plotly_chart(pfig)

























