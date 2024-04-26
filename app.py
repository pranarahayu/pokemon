import streamlit as st
import requests
import random

st.set_page_config(page_title='Match Center', layout='centered')
st.markdown('# Guess Who? - Pokemon Edition')

idx = random.sample(range(1, 1026), 25)

row1 = st.columns(5)
row2 = st.columns(5)
row3 = st.columns(5)
row4 = st.columns(5)
row5 = st.columns(5)

'''
for col in row1 + row2 + row3 + row4 + row5 + row6:
    tile = col.container(height=100)
    for i in idx:
        url = "https://github.com/PokeAPI/sprites/blob/ca5a7886c10753144e6fae3b69d45a4d42a449b4/sprites/pokemon/{id}.png?raw=true"
        pokemon_id = str(i)
        response = requests.get(url.format(id=pokemon_id))
    tile.image(response.content)
'''
for i in idx:
    url = "https://github.com/PokeAPI/sprites/blob/ca5a7886c10753144e6fae3b69d45a4d42a449b4/sprites/pokemon/{id}.png?raw=true"
    pokemon_id = str(i)
    response = requests.get(url.format(id=pokemon_id))
    for col in row1 + row2 + row3 + row4 + row5 + row6:
        tile = col.container(height=100)
        tile.image(response.content, width=100)
