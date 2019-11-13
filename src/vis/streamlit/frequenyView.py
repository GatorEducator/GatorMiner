#!/usr/bin/env python3

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# Title
st.title('Frequency Using Streamlit')
x = st.slider('x')
st.write(x, 'squared is', x*x)

st.write('creating a simple table')
st.write(pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
}))

# Creating simple bar graph
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.bar_chart(chart_data)


# Creating random data
data = pd.DataFrame(
    np.random.randn(10,5),
    columns=('col %d' % i for i in range(5)))
st.table(data)
st.line_chart(data)
st.write(data)


# Writing with jason
st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
    ],
})

# Mathplot must run: 
# echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
arr = np.random.normal(1,1, size=50)
plt.hist(arr, bins=10)
st.pyplo()
