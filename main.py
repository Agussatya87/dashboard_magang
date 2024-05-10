import pandas as pd
import streamlit as st
from plotly import graph_objs as go
import pymongo


st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.title('Dashboard Siswa')

data = pd.read_csv("combine_final.csv")

st.subheader('Raw data')
st.write(data.tail(50))
