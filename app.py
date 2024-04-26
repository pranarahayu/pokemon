import streamlit as st
import requests
import random

row1 = st.columns(5)
row2 = st.columns(5)
row3 = st.columns(5)
row4 = st.columns(5)
row5 = st.columns(5)
row6 = st.columns(5)

for col in row1 + row2 + row3 + row4 + row5 + row6:
    tile = col.container(height=100)
