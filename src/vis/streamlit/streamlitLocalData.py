import streamlit as st
import pandas as pd
import numpy as np
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'data.csv')

st.title('Data Visualization Demo Using Streamlit')

DATE_COLUMN = 'date/time'
DATA_FILE = (my_file)


def load_data(nrows):
    data = pd.read_csv(DATA_FILE, nrows=nrows)
    return data

data = st.cache(pd.read_csv)('data.csv')
st.write('data:')
st.write(df)

st.write('graph')
st.barchart(data)