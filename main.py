import pandas as pd
import streamlit as st
from plotly import graph_objs as go
import pymongo


st.set_page_config(layout='wide', initial_sidebar_state='expanded')


st.title('Dashboard Siswa :student:')

data = pd.read_csv("combine_final.csv")

# Sidebar for user input
st.sidebar.title("Masukan Data Siswa :books:")
input_data = st.sidebar.text_input(label="Nama", placeholder="masukan nama")


if input_data:
    filtered_data = data[data['name'].str.contains(input_data, case=False, na=False)]
    st.subheader('Raw Data: Filtered by Name')
    st.write(filtered_data)
else:
    st.subheader('Raw Data: Last 50 Entries')
    st.write(data.tail(50))
